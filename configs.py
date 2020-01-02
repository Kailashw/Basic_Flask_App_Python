"""This module is to configure app to connect with database."""

from pymongo import MongoClient

DATABASE = MongoClient()['pokedox'] # DB_NAME
DEBUG = True
# in following change placeholders with proper values. 
client = MongoClient("mongodb+srv://{username}:{password}@{mongoUrl}/test?retryWrites=true&w=majority", 27017)
