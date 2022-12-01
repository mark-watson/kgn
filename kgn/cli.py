import click

from .textui import *
from .kgn import *

@click.command()
@click.version_option()
def cli():
    "Knowledge Graph Navigator - an interactive command line app"
    kgn()
