# kgn

[![PyPI](https://img.shields.io/pypi/v/kgn.svg)](https://pypi.org/project/kgn/)
[![Changelog](https://img.shields.io/github/v/release/mark-watson/kgn?include_prereleases&label=changelog)](https://github.com/mark-watson/kgn/releases)
[![Tests](https://github.com/mark-watson/kgn/workflows/Test/badge.svg)](https://github.com/mark-watson/kgn/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/mark-watson/kgn/blob/master/LICENSE)

Interactive exploration of Knowledge Graphs using natural language

## Installation

Install this tool using `pip`:

    pip install kgn

## Usage

For help, run:

    kgn --help

You can also use:

    python -m kgn --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd kgn
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
