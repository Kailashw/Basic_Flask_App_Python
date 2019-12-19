"""This module is to configure app to connect with database."""

from pymongo import MongoClient

DATABASE = MongoClient()['pokedox'] # DB_NAME
DEBUG = True
client = MongoClient("mongodb+srv://temp:temp1234@cluster0-dlosx.azure.mongodb.net/test?retryWrites=true&w=majority", 27017)