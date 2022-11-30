import readchar

def multiple_choice_selection_list(text_prompt, *options):
    """
    Allow selection of 0, 1, or more items from a selection list
    """

    selection_items = {
        str(key): item
        for key, item in enumerate(options, 1)
    }

    prompt = text_prompt + '\nHit enter or return key when done:\n' + \
              '\n'.join(f' {key}) {item}' for key, item in selection_items.items()) + \
              '\n[' + '/'.join(selection_items.keys()) + ']? :'

    ret = {}
    print(prompt)
    while True:
        key = readchar.readkey()
        name = selection_items.get(key)
        if name is not None:
            print(f"Selected '{name}'. Hit return key or enter to stop.")
            ret[key] = name
        else:
            return ret

def select_entities(people, places, organizations):
    "should return something like: \
    \
{'entities': ['Bill Gates || William Henry Gates III (born October 28, 1955) ' \
              'is an American busines...', \
              'Seattle || Washington (/ˈwɒʃɪŋtən/), officially the State of ' \
              'Washington, is a sta...', \
              'Apple || Hot Chocolate are a British soul band popular during ' \
              'the 1970s and 198...', \
              'Microsoft || Microsoft Corporation is an American multinational ' \
              'technology corporat...']} "

    ret = {'people': [], 'places': [], 'organizations': []}
    if len(people) > 0:
        ret['people'] = list(multiple_choice_selection_list("People", *people).values())
    if len(places) > 0:
        ret['places'] = list(multiple_choice_selection_list("Places", *places).values())
    if len(people) > 0:
        ret['organizations'] = list(multiple_choice_selection_list("Organizations", *organizations).values())
    return {'entities': ret['people'] + ret['places'] + ret['organizations']}


def get_query():
    return input('Enter a list of entities: ')

