"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Users, Character, Planet, Starship
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Blueprint('api', __name__)
CORS(api)  # Allow CORS requests to this API


@api.route('/hello', methods=[ 'GET'])
def handle_hello():
    response_body = {}
    response_body['message'] = "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    return response_body


@api.route('/characters', methods=['GET'])
def get_characters():
    response_body = {
        'results': [character.serialize() for character in Character.query.all()],
        'message': "All characters retrieved successfully"
    }
    return response_body, 200

@api.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.get(character_id)
    if not character:
        return {'error': 'Not found', 'message': f'Character {character_id} not found'}, 404
    return {'result': character.serialize(), 'message': f'Character {character_id} retrieved'}, 200


@api.route('/planets', methods=['GET'])
def get_planets():
    response_body = {
        'results': [planet.serialize() for planet in Planet.query.all()],
        'message': "All planets retrieved successfully"
    }
    return response_body, 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return {'error': 'Not found', 'message': f'Planet {planet_id} not found'}, 404
    return {'result': planet.serialize(), 'message': f'Planet {planet_id} retrieved'}, 200


@api.route('/users', methods=['GET'])
def get_users():
    response_body = {
        'results': [user.serialize() for user in Users.query.all()],
        'message': "All users retrieved successfully"
    }
    return response_body, 200

