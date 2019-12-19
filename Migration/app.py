from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://temp:temp1234@cluster0-dlosx.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('pokedox')
categories = db.pokemons
print(categories.count_documents({}))
with open('data.json', 'r') as importFile:
    categories_dict = json.load(importFile)

categories.insert_many(categories_dict)
print(categories.count_documents({}))
