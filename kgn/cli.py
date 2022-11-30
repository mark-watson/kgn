import click

from kgn import *

@click.command()
@click.version_option()
@click.option("--query", help='Example: "Bill Gates, Apple, Steve Jobs, Microsoft', default='')
@click.option("--use_gui", help="Use GUI", default=1)
def cli(inputdir, outputfile):
    "Knowledge Graph Creator: converts text to RDF triples.\n\ne.g., kgcreator --inputdir=test_data --outputfile=out.rdf"
    kgn_console(query, None)
