from .sparql import dbpedia_sparql
from .colorize import colorize_sparql

def dbpedia_get_entities_by_name(name, dbpedia_type):
    sparql = (
        'select distinct ?s ?comment {{ ?s ?p "{0}"@en . ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> {1} . OPTIONAL {{ ?s <http://dbpedia.org/ontology/description> ?desc . FILTER (lang(?desc) = "en") }} OPTIONAL {{ ?s <http://www.w3.org/2000/01/rdf-schema#comment> ?comm . FILTER (lang(?comm) = "en") }} BIND(COALESCE(?desc, ?comm, "No description available") AS ?comment) }} limit 15'
        .format(name, dbpedia_type))
    print('Generated SPARQL to get DBPedia entity URIs from a name:')
    print(colorize_sparql(sparql))
    return dbpedia_sparql(sparql)

