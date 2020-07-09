import json

states = json.loads(open('StateAbbreviations.json').read())

for state in states:
    open(state + 'Cities.json', 'w+')