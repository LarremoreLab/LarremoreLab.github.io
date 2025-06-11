from collections import defaultdict
from webweb import Web
from pathlib import Path
import yaml

DATA_PATH = Path(__file__).parent.joinpath('_data')
PAPERS_PATH = DATA_PATH.joinpath('papers.yml')
PEOPLE_PATH = DATA_PATH.joinpath('people.yml')
CODE_PATH = DATA_PATH.joinpath('code.yml')
EXTRA_WEBWEB_PATH = DATA_PATH.joinpath('extra_webweb.yml')
WEBWEB_JSON_PATH = DATA_PATH.joinpath('index_web.json')

KIND_TO_COLOR_MAP = {
    'collaborator': '#999999',
    # 'collaborator': '#78C81F',
    'lab member': '#E01E7B',     # Pink for current lab members
    'alumni': '#9d1557',         # Yellow for alumni

    'paper_scieco': '#8ebef1',   # Pink for scieco papers
    'paper_idepi': '#1C7BE0',    # Blue for idepi papers  
    'paper_complex': '#14579f',  # Grey for complex papers

    'code_scieco': '#8ebef1',    # Pink for scieco code
    'code_idepi': '#1C7BE0',     # Blue for idepi code
    'code_complex': '#14579f',   # Grey for complex code
}



def load_yaml(path):
    return yaml.load(path.read_text(), Loader=yaml.FullLoader)


def clean_name(name):
    if name.endswith('*') or name.endswith('.'):
        name = name[:-1]
    return name


# def people_to_aliases(all_people):
#     aliases = dict()
#     for person in all_people['people'] + all_people['alumni']:
#         person_name = person['name']
#         aliases[person_name] = person_name

#         for alias in person.get('aliases', []):
#             aliases[alias] = person_name

#     return aliases

def people_to_aliases(all_people):
    aliases = dict()
    
    # Process current people
    for person in all_people['people']:
        person_name = person['name']
        aliases[person_name] = person_name

        for alias in person.get('aliases', []):
            aliases[alias] = person_name

    # Process alumni - now organized by category
    alumni_data = all_people.get('alumni', {})
    for category, people_list in alumni_data.items():
        if isinstance(people_list, list):
            for person in people_list:
                person_name = person['name']
                aliases[person_name] = person_name

                for alias in person.get('aliases', []):
                    aliases[alias] = person_name

    return aliases


def clean_all_names(data):
    aliases = people_to_aliases(data['people'])

    for category in data['papers']['categories']:
        for i, paper in enumerate(category['pubs']):
            for j, name in enumerate(paper['authors']):
                name = clean_name(name)
                name = aliases.get(name, name)
                paper['authors'][j] = name

    for project in data['code']['repos']:
        for i, name in enumerate(project['authors']):
            name = clean_name(name)
            name = aliases.get(name, name)
            project['authors'][i] = name

    for item in data['extra']['projects']:
        for i, person in enumerate(item.get('people', [])):
            item['people'][i] = aliases.get(person, person)

    # Process current people
    for person in data['people']['people']:
        name = clean_name(person['name'])
        person['name'] = aliases.get(name, name)
    
    # Process alumni - now organized by category
    alumni_data = data['people'].get('alumni', {})
    for category, people_list in alumni_data.items():
        if isinstance(people_list, list):
            for person in people_list:
                name = clean_name(person['name'])
                person['name'] = aliases.get(name, name)


def make_network(data):
    nodes = defaultdict(dict)
    edges = []
    collaborator_connections = defaultdict(set)  # To track unique connections per collaborator

    dan = data['people']['people'][0]['name']
    print(f"Main person: {dan}")

    # Process papers - build nodes and count connections
    for category in data['papers']['categories']:
        for paper in category['pubs']:
            title = paper['title']
            paper_type = paper.get('type', 'scieco')  # Default to scieco if no type
            nodes[title] = {
                'name': title,
                'kind': f'paper_{paper_type}'  # Use paper_scieco, paper_idepi, or paper_complex
            }

            if 'links' in paper:
                nodes[title]['url'] = paper['links'][0]['url']

            for name in paper['authors']:
                if name == dan:
                    continue

                # Add this paper to the collaborator's connections
                collaborator_connections[name].add(title)
                edges.append([title, name])


    # Process code repos
    for project in data['code']['repos']:
        title = project['title']
        code_type = project.get('type', 'scieco')  # Default to scieco if no type
        nodes[title] = {
            'name': title,
            'kind': f'code_{code_type}'  # Use code_scieco, code_idepi, or code_complex
        }
        for name in project['authors']:
            if name == dan:
                continue
            
            # Add this code project to the collaborator's connections
            collaborator_connections[name].add(title)
            edges.append([title, name])

    # Process extra projects
    for project in data['extra']['projects']:
        project_name = project['name']
        project_type = project.get('type', 'scieco')  # Default to scieco if no type
        nodes[project_name] = {
            'name': project_name,
            'kind': f'code_{project_type}'  # Use code_scieco, code_idepi, or code_complex
        }

        if project.get('url'):
            nodes[project_name]['url'] = project['url']

        for name in project['people']:
            if name == dan:
                continue
            
            # Add this project to the collaborator's connections
            collaborator_connections[name].add(project_name)
            edges.append([project_name, name])

    # Set up collaborator nodes
    for name, connections in collaborator_connections.items():
        nodes[name]['name'] = name
        nodes[name]['kind'] = 'collaborator'
        
        # Add URL if available
        for person in data['people'].get('collaborators', []):
            if person['name'] == name and person.get('url'):
                nodes[name]['url'] = person['url']
                break

    # Set up lab member nodes
    for person in data['people']['people']:
        name = person['name']
        if name == dan:
            continue

        nodes[name]['name'] = name
        nodes[name]['kind'] = 'lab member'

        url = person.get('url')
        if url and url != '/':
            nodes[name]['url'] = url

    # Set up alumni nodes
    alumni_data = data['people'].get('alumni', {})
    for category, people_list in alumni_data.items():
        if isinstance(people_list, list):
            for person in people_list:
                name = person['name']
                if name in nodes:  # Only if they appear in collaborations
                    nodes[name]['kind'] = 'alumni'
                    
                    url = person.get('url')
                    if url and url != '/':
                        nodes[name]['url'] = url

    # Print connection counts for debugging
    print("\nCollaborator connection counts:")
    for name, connections in sorted(collaborator_connections.items()):
        print(f"{name}: {len(connections)}")
    
    # Set size based on connection count
    for node in nodes:
        kind = nodes[node]['kind']
        if kind.startswith('paper_'):  # Any paper type
            size = 1.0  # Papers are larger
        elif kind.startswith('code_'):  # Any code type
            size = 0.7  # Code/data contributions are smaller
        elif kind == 'lab member':
            size = 1.0  # Same size as high-frequency collaborators
        elif kind == 'alumni':
            size = 1.0  # Same size as lab members
        elif kind == 'collaborator':
            connection_count = len(collaborator_connections.get(node, set()))
            
            if connection_count < 2:  # One-off collaborators
                size = 0.7  # Just a little smaller
            elif connection_count < 5:  # 2-4 papers
                size = 0.85  # A little smaller
            else:  # 5+ papers
                size = 1.0  # Just a little smaller than original
                
            print(f"Setting size for {node} with {connection_count} connections: {size}")
        
        nodes[node]['size'] = size
        nodes[node]['color'] = KIND_TO_COLOR_MAP[kind]

    web = Web(adjacency=edges, nodes=dict(nodes))
    web.display.sizeBy = 'size'
    web.display.colorBy = 'color'
    web.display.hideMenu = True
    web.display.showLegend = False
    web.display.gravity = 0.7
    web.display.width = 400
    web.display.height = 400
    web.display.scaleLinkOpacity = True
    web.display.scaleLinkWidth = True
    web.display.scales = {
        'nodeSize': {
            'min': 0.7,  # Adjusted minimum size
            'max': 1.0,  # Maximum size for frequent collaborators and lab members
        }
    }

    print(f"Writing network data to {WEBWEB_JSON_PATH}")
    WEBWEB_JSON_PATH.write_text(web.json)
    print("File written successfully!")
    # web.show()


if __name__ == '__main__':
    print("Loading data files...")
    data = {
        'papers': load_yaml(PAPERS_PATH),
        'people': load_yaml(PEOPLE_PATH),
        'code': load_yaml(CODE_PATH),
        'extra': load_yaml(EXTRA_WEBWEB_PATH),
    }
    print("Data loaded successfully")
    
    print("Cleaning names...")
    clean_all_names(data)
    print("Names cleaned successfully")
    
    print("Building network...")
    make_network(data)
    print("Network built and saved successfully")