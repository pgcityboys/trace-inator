import os
import requests

from http import HTTPStatus
from flask import Blueprint, request
from src.api.model.place import Place
from src.api.model.places import PlacesModel
from src.api.schema.places_schema import PlacesSchema

place_api = Blueprint('place', __name__)
API_URL = "https://places.googleapis.com/v1/places:searchText"


@place_api.route('/places')
def trace():
    params = request.args
    query = params.get("q")
    body = {
        "textQuery": query,
        "languageCode": "pl",
        "maxResultCount": 10
    }
    headers = {
        "X-Goog-FieldMask": "*",
        "X-Goog-Api-Key": os.getenv("API_KEY")
    }
    response = requests.post(API_URL, body, headers=headers)

    mapped_places = get_mapped_places(response.json()["places"])
    result = PlacesModel(mapped_places)
    return PlacesSchema().dump(result), HTTPStatus.OK


def get_mapped_places(places: dict) -> list:
    mapped_places = []
    for place in places:
        name = place["displayName"]["text"]
        address = place["shortFormattedAddress"]
        coordinates = {"lat": place["location"]["latitude"], "lon": place["location"]["longitude"]}
        mapped_places.append(Place(coordinates, name, address).serialize())

    return mapped_places
