import json


def find(obj, phrase):
    for k, v in enumerate(obj) if isinstance(obj, list) else obj.items():
        if v == phrase:
            return str(k)

        elif isinstance(v, (list, dict)):
            found = find(v, phrase)
            if found:
                return '{phrase} -> {found}'.format(phrase=phrase, found=found)

file = json.loads(open('input.txt').read())
print(find(file, 'dailyprogrammer'))
