"""This is init module."""

from flask import Flask

# Place where app is defined
runapp = Flask(__name__)

from runapp import pokemons