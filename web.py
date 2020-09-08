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
    'collaborator': '#78C81F',
    'lab member': '#E01E7B',
    'paper': '#1C7BE0',
    'code': '#D2D215',
}


def load_yaml(path):
    return yaml.load(path.read_text(), Loader=yaml.FullLoader)


def clean_name(name):
    if name.endswith('*') or name.endswith('.'):
        name = name[:-1]
    return name


def people_to_aliases(all_people):
    aliases = dict()
    for person in all_people['people'] + all_people['alumni']:
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

    for person in data['people']['people'] + data['people']['alumni']:
        name = clean_name(person['name'])
        person['name'] = aliases.get(name, name)


def make_network(data):
    nodes = defaultdict(dict)
    edges = []

    dan = data['people']['people'][0]['name']

    for category in data['papers']['categories']:
        for paper in category['pubs']:
            title = paper['title']
            nodes[title] = {
                'name': title,
                'kind': 'paper'
            }

            if 'links' in paper:
                nodes[title]['url'] = paper['links'][0]['url']

            for name in paper['authors']:
                if name == dan:
                    continue

                nodes[name]['name'] = name

                nodes[name]['kind'] = 'collaborator'

                for person in data['people']['collaborators']:
                    if person['name'] == name:
                        if person.get('url'):
                            nodes[name]['url'] = person['url']
                            break

                edges.append([title, name])

    for project in data['code']['repos']:
        title = project['title']
        nodes[title] = {
            'name': title,
            'kind': 'code'
        }
        for name in project['authors']:
            if name == dan:
                continue

            nodes[name]['name'] = name
            nodes[name]['kind'] = 'collaborator'

            edges.append([title, name])

    for project in data['extra']['projects']:
        project_name = project['name']
        nodes[project_name] = {
            'name': project_name,
            'kind': 'code'
        }

        if project.get('url'):
            nodes[project_name]['url'] = project['url']

        for name in project['people']:
            if name == dan:
                continue
            edges.append([project_name, name])

    for person in data['people']['people']:
        name = person['name']
        if name == dan:
            continue

        title = person['title'].lower()

        nodes[name]['name'] = name
        nodes[name]['kind'] = 'lab member'

        url = person.get('url')

        if url and url != '/':
            nodes[name]['url'] = url

    for node in nodes:
        kind = nodes[node]['kind']
        size = 1
        if kind == 'lab member':
            size = 1.5
        elif kind == 'collaborator':
            size = 1.25

        nodes[node]['size'] = size
        nodes[node]['color'] = KIND_TO_COLOR_MAP[kind]

    web = Web(adjacency=edges, nodes=dict(nodes))
    web.display.sizeBy = 'size'
    web.display.colorBy = 'color'
    web.display.hideMenu = True
    web.display.showLegend = False
    web.display.gravity = 0.4
    web.display.width = 400
    web.display.height = 400
    web.display.scaleLinkOpacity = True
    web.display.scaleLinkWidth = True
    web.display.scales = {
        'nodeSize': {
            'min': 0.65,
            'max': 1.1,
        }
    }

    WEBWEB_JSON_PATH.write_text(web.json)
    # web.show()


if __name__ == '__main__':
    data = {
        'papers': load_yaml(PAPERS_PATH),
        'people': load_yaml(PEOPLE_PATH),
        'code': load_yaml(CODE_PATH),
        'extra': load_yaml(EXTRA_WEBWEB_PATH),
    }
    clean_all_names(data)

    make_network(data)
