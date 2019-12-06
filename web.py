from collections import defaultdict
from webweb import Web
from pathlib import Path
import yaml

DATA_PATH = Path.cwd().joinpath('_data')
PAPERS_PATH = DATA_PATH.joinpath('papers.yml')
PEOPLE_PATH = DATA_PATH.joinpath('people.yml')
CODE_PATH = DATA_PATH.joinpath('code.yml')
WEBWEB_JSON_PATH = DATA_PATH.joinpath('index_web.json')


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

    for person in data['people']['people'] + data['people']['alumni']:
        name = clean_name(person['name'])
        person['name'] = aliases.get(name, name)


def make_network(data):
    nodes = defaultdict(dict)
    edges = []

    dan = data['people']['people'][0]['name']
    nodes[dan]['kind'] = 'PI'

    for category in data['papers']['categories']:
        for paper in category['pubs']:
            title = paper['title']
            nodes[title] = {
                'name': title,
                'kind': 'paper'
            }

            for name in paper['authors']:
                nodes[name]['name'] = name

                if name != dan:
                    nodes[name]['kind'] = 'collaborator'

                edges.append([title, name])

    for project in data['code']['repos']:
        title = project['title']
        nodes[title] = {
            'name': title,
            'kind': 'code'
        }
        for name in project['authors']:
            nodes[name]['name'] = name

            if name != dan:
                nodes[name]['kind'] = 'collaborator'

            edges.append([title, name])

    for person in data['people']['people']:
        name = person['name']
        if name == dan:
            continue

        title = person['title'].lower()
        kind = 'collaborator'
        if title.startswith('phd'):
            kind = 'PhD'
        elif title.startswith('ms'):
            kind = 'Masters'
        elif title.startswith('undergrad'):
            kind = 'Undergraduate'

        nodes[name]['name'] = name
        nodes[name]['kind'] = kind
        edges.append([dan, name])

    web = Web(adjacency=edges, nodes=dict(nodes))
    web.display.colorBy = 'kind'
    web.display.colorPalette = 'Dark2'
    web.display.hideMenu = True
    web.display.showLegend = False

    WEBWEB_JSON_PATH.write_text(web.json)
    web.show()


if __name__ == '__main__':
    data = {
        'papers': load_yaml(PAPERS_PATH),
        'people': load_yaml(PEOPLE_PATH),
        'code': load_yaml(CODE_PATH),
    }
    clean_all_names(data)

    make_network(data)
