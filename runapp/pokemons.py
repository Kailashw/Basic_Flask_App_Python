"""This module will serve the api request."""

from configs import client
from runapp import runapp
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp


# Select the database
db = client.pokedox
# Select the collection
collection = db.pokemons
categories_collection = db.categories

@runapp.route("/")
def welcome():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp

@runapp.route("/api/v1/pokemons", methods=['GET'])
def fetch_pokemons():
    """
       Function to fetch the pokemons.
       """
    try:
        data = list(collection.find())
        # Return all the records as query string parameters are not available
        if len(data) > 0:
            # Prepare response if the pokemons are found
            return dumps(data)
        else:
            # Return empty array if no pokemons are found
            return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500

@runapp.route("/api/v1/categories", methods=['GET'])
def fetch_categories():
    """
       Function to fetch the categories.
       """
    try:
        data = list(categories_collection.find())
        # Return all the records as query string parameters are not available
        if len(data) > 0:
            # Prepare response if the categories are found
            return dumps(data)
        else:
            # Return empty array if no categories are found
            return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500

@runapp.route("/api/v1/categories", methods=['POST'])
def create_category():
    """
       Function to create new category.
       """
    try:
        # Create new categories
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as request body is not available
            # Add message for debugging purpose
            return "", 400

        record_created =  categories_collection.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of Id of the newly created item
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500

@runapp.route("/api/v1/categories/<id>", methods=['DELETE'])
def remove_category(id):
    """
       Function to remove the category.
       """
    try:
        # Delete the category
        delete_category = categories_collection.delete_one({"categoryId": int(id)})

        if delete_category.deleted_count > 0 :
            # Prepare the response
            return "", 204
        else:
            # Resource Not found
            return "", 404
    except:
        # Error while trying to delete the resource
        # Add message for debugging purpose
        return "", 500


@runapp.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp