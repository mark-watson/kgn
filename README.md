# kgn

[![PyPI](https://img.shields.io/pypi/v/kgn.svg)](https://pypi.org/project/kgn/)
[![Changelog](https://img.shields.io/github/v/release/mark-watson/kgn?include_prereleases&label=changelog)](https://github.com/mark-watson/kgn/releases)
[![Tests](https://github.com/mark-watson/kgn/workflows/Test/badge.svg)](https://github.com/mark-watson/kgn/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/mark-watson/kgn/blob/master/LICENSE)

# Interactive exploration of Knowledge Graphs using natural language

This is a tool that interactively explores the DBPedia Knowledge Graph. The user inputs a list of people, companies, places, etc. and entities in DBPedia are identified using SPARQL queries and a spaCy language deep learning language model and relations are also found between these entities. A local SQlite3 database is used to cache SPARQL query results.

This code is an example program in my book "Practical Python Artificial Intelligence Programming" [https://leanpub.com/pythonai](https://leanpub.com/pythonai). You can read this book and all of my recent eBooks at my website [https://markwatson.com](https://markwatson.com).

This code is derived from a Common Lisp example in my book "Loving Common Lisp, or the Savvy Programmer's Secret Weapon" [https://leanpub.com/lovinglisp](https://leanpub.com/lovinglisp) and in my Hy (hylang) book "A Lisp Programmer Living in Python-Land: The Hy Programming Language" [https://leanpub.com/hy-lisp-python](https://leanpub.com/hy-lisp-python).


## Installation

Install this tool using `pip`:

    pip install kgn

## Usage

For help, run:

    kgn --help

You can also use:

    python -m kgn --help

## Example output

Most output is removed fro brevity:

```
$ python kgn.py 
table dbpedia already exists
Knowledge Graph Navigator (note: only runs in a terminal)
Enter a list of entities: Bill Gates, Steve Jobs, IBM, Apple, Microsoft, Seattle
Generated SPARQL to get DBPedia entity URIs from a name:
select distinct ?s ?comment { ?s ?p "Bill Gates"@en . ?s <http://www . w3 . org/2000/01/rdf-schema#comment> ?comment . FILTER (lang(?comment) = 'en') . ?s <http://www . w3 . org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia . org/ontology/Person> . } limit 15 
Using cached query results
Generated SPARQL to get DBPedia entity URIs from a name:
select distinct ?s ?comment { ?s ?p "Steve Jobs"@en . ?s <http://www . w3 . org/2000/01/rdf-schema#comment> ?comment . FILTER (lang(?comment) = 'en') . ?s <http://www . w3 . org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia . org/ontology/Person> . } limit 15 
Using cached query results

...

People
Hit enter or return key when done:
 1) Bill Gates || Harry Roy Lewis (born 1947) is an American computer scientist, mathe­m...
 2) Bill Gates || Cascade Investment, L.L.C. is an American holding company and private ...
 3) Bill Gates || Simon Wood is a British cook and winner of the 2015 edition of MasterC...
 4) Bill Gates || Jerry P. Dyer (born May 3, 1959) is an American politician and former ...
 5) Bill Gates || William Henry Gates III (born October 28, 1955) is an American busines...
 6) Steve Jobs || Steven Paul Jobs (February 24, 1955 – October 5, 2011) was an American...
[1/2/3/4/5/6]? :
Selected 'Bill Gates || William Henry Gates III (born October 28, 1955) is an American busines...'. Hit return key or enter to stop.
Selected 'Steve Jobs || Steven Paul Jobs (February 24, 1955 – October 5, 2011) was an American...'. Hit return key or enter to stop.
Places
Hit enter or return key when done:
 1) Seattle || Washington (/ˈwɒʃɪŋtən/), officially the State of Washington, is a sta...
 2) Seattle || Medina (/məˈdaɪnə/) is a mostly residential city in Eastside, King Cou...
 3) Seattle || Northeast 130th Street Beach is a 60-foot-wide (18 m) public beach in ...
 4) Seattle || Seattle (/siˈætəl/ see-AT-əl) is a seaport city on the West Coast of t...
 5) Seattle || The Troy Laundry Building is a 1927 building in the South Lake Union/C...
 6) Seattle || Louisa Boren Park is a 7.2-acre (29,000 m2) park in Seattle, Washingto...
 7) Seattle || Bitter Lake is a neighborhood in Seattle, Washington, United States, n...
 8) Seattle || King County is located in the U.S. state of Washington. The population...
 9) Seattle || Formerly known as Diocese of Nesqually, 1850-1907. The Roman Catholic ...
[1/2/3/4/5/6/7/8/9]? :
Selected 'Seattle || Washington (/ˈwɒʃɪŋtən/), officially the State of Washington, is a sta...'. Hit return key or enter to stop.
Organizations

...

Entity data:
{'entities': ['Bill Gates || William Henry Gates III (born October 28, 1955) '
              'is an American busines...',
              'Steve Jobs || Steven Paul Jobs (February 24, 1955 – October 5, '
              '2011) was an American...',
              'Seattle || Washington (/ˈwɒʃɪŋtən/), officially the State of '
              'Washington, is a sta...',
              'IBM || International Business Machines Corporation (IBM) is an '
              'American multi...',
              'IBM || Sequent Computer Systems was a computer company that '
              'designed and manu...',
              'IBM || Applix Inc. was a computer software company founded in '
              '1983 based in W...']}

Generated SPARQL to get relationships between two entities:
SELECT DISTINCT ?p { <http://dbpedia . org/resource/Bill_Gates> ?p <http://dbpedia . org/resource/Steve_Jobs> . FILTER (!regex(str(?p), 'wikiPage', 'i')) } LIMIT 5 

...

Generated SPARQL to get relationships between two entities:
SELECT DISTINCT ?p { <http://dbpedia . org/resource/Bill_Gates> ?p <http://dbpedia . org/resource/Steve_Jobs> . FILTER (!regex(str(?p), 'wikiPage', 'i')) } LIMIT 5 

...

Discovered relationship links:

<http://dbpedia.org/resource/IBM> --> http://dbpedia.org/ontology/owner --> <http://dbpedia.org/resource/Applix>
<http://dbpedia.org/resource/IBM> --> http://dbpedia.org/ontology/owningCompany --> <http://dbpedia.org/resource/Applix>
<http://dbpedia.org/resource/Applix> --> http://dbpedia.org/ontology/owner --> <http://dbpedia.org/resource/IBM>
<http://dbpedia.org/resource/Applix> --> http://dbpedia.org/ontology/owningCompany --> <http://dbpedia.org/resource/IBM>
Enter a list of entities: 

```

## Possible problems

I cache SPARQL queries to DBPedia in a local SQlite3 database. I sometimes need to delete the database file.


## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd kgn
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
