from pprint import pprint
from textui import select_entities, get_query
from kgnutils import dbpedia_get_entities_by_name
from relationships import entity_results_to_relationship_links
import spacy

nlp_model = spacy.load('en_core_web_sm')

def entities_in_text(s):
    doc = nlp_model(s)
    ret = {}
    for [ename, etype] in [[entity.text, entity.label_] for entity in doc.ents]:
        if etype in ret:
            ret[etype] = ret[etype] + [ename]
        else:
            ret[etype] = [ename]
    return ret


entity_type_to_type_uri = {'PERSON': '<http://dbpedia.org/ontology/Person>',
    'GPE': '<http://dbpedia.org/ontology/Place>', 'ORG':
    '<http://dbpedia.org/ontology/Organisation>'}
short_comment_to_uri = {}


def shorten_comment(comment, uri):
    sc = comment[0:70:None] + '...'
    short_comment_to_uri[sc] = uri
    return sc


query = ''


def kgn():
    print("Knowledge Graph Navigator (note: only runs in a terminal)")
    while True:
        query = get_query()
        if query == 'quit' or query == 'q':
            break
        elist = entities_in_text(query)
        people_found_on_dbpedia = []
        places_found_on_dbpedia = []
        organizations_found_on_dbpedia = []
        global short_comment_to_uri
        short_comment_to_uri = {}
        for key in elist:
            type_uri = entity_type_to_type_uri[key]
            for name in elist[key]:
                dbp = dbpedia_get_entities_by_name(name, type_uri)
                for d in dbp:
                    short_comment = shorten_comment(d[1][1], d[0][1])
                    people_found_on_dbpedia.extend([name + ' || ' +
                        short_comment]) if key == 'PERSON' else None
                    places_found_on_dbpedia.extend([name + ' || ' +
                        short_comment]) if key == 'GPE' else None
                    organizations_found_on_dbpedia.extend([name + ' || ' +
                        short_comment]) if key == 'ORG' else None
        user_selected_entities = select_entities(people_found_on_dbpedia,
            places_found_on_dbpedia, organizations_found_on_dbpedia)
        uri_list = []
        for entity in user_selected_entities['entities']:
            short_comment = entity[4 + entity.index(' || '):None:None]
            uri_list.extend([short_comment_to_uri[short_comment]])
        print("\n\nEntity data:")
        pprint(user_selected_entities)
        print("\n\n")
        relation_data = (
            entity_results_to_relationship_links(uri_list))
        print('\n\nDiscovered relationship links:\n')
        for relationship in relation_data:
            print(relationship[0] + ' --> ' + relationship[2][1] + ' --> ' + relationship[1])

def kgn_console(query, use_gui):
    print("kgn_console is not implemented")

kgn()

