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
            # Prepare response if the users are found
            return dumps(data)
        else:
            # Return empty array if no users are found
            return jsonify([])
    except:
        # Error while trying to fetch the resource
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