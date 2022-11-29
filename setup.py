from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="kgn",
    description="Interactive exploration of Knowledge Graphs using natural language",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Mark Watson",
    url="https://github.com/mark-watson/kgn",
    project_urls={
        "Issues": "https://github.com/mark-watson/kgn/issues",
        "CI": "https://github.com/mark-watson/kgn/actions",
        "Changelog": "https://github.com/mark-watson/kgn/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["kgn"],
    entry_points="""
        [console_scripts]
        kgn=kgn.cli:cli
    """,
    install_requires=["click", "requests", "spacy", "tk"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
