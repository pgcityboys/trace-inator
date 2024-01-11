import os
import re
from http import HTTPStatus

import requests as requests
from flask import Blueprint, request

from api.model.path import Path
from api.model.step import Step
from api.model.trace import TraceModel
from api.schema.trace_schema import TraceSchema

trace_api = Blueprint('trace', __name__)


@trace_api.route('/trace')
def trace():
    params = request.args
    origin = params.get("origin")
    destination = params.get("destination")
    travel_mode = params.get("mode")
    waypoints = params.get("waypoints")

    data = send_request(origin, destination, travel_mode, waypoints)
    return data["routes"][0], HTTPStatus.OK


@trace_api.route('/trace/path')
def path():
    params = request.args
    origin = params.get("origin")
    destination = params.get("destination")
    travel_mode = params.get("mode")
    waypoints = params.get("waypoints")

    data = send_request(origin, destination, travel_mode, waypoints)
    points = []
    for trace in data["routes"][0]["legs"]:
        for step in trace["steps"]:
            points.append({"lat": step["end_location"]["lat"], "lng": step["end_location"]["lng"]})

    return points


def send_request(origin: str, destination: str, travel_mode: str, waypoints: str):
    if origin is None or destination is None:
        raise Exception("origins and destination params are required")
    url = "https://maps.googleapis.com/maps/api/directions/json?" \
          "destination=" + destination + \
          "&origin=" + origin + \
          "&key=" + "AIzaSyA2zGfw0xiuN49bqES2-0_lrlq-106ewjU"

    if travel_mode is not None:
        url += "&mode=" + travel_mode

    if waypoints is not None:
        url += "&waypoints=" + waypoints

    return requests.get(url).json()


def create_paths_for_trace(trace: dict):
    paths = []
    for path in trace["legs"]:
        distance = convert_to_meters(path["distance"]["text"])
        duration = convert_to_seconds(path["duration"]["text"])
        start_address = path["start_address"]
        end_address = path["end_address"]
        start_coordinates = {"lat": path["start_location"]["lat"], "lon": path["start_location"]["lng"]}
        end_coordinates = {"lat": path["end_location"]["lat"], "lon": path["end_location"]["lng"]}
        steps = create_steps_for_path(path)
        paths.append(Path(start_coordinates, start_address, end_coordinates, end_address, duration, distance, steps).serialize())

    return paths


def create_steps_for_path(path: dict) -> list:
    pattern = re.compile('<.*?>')
    steps = []
    for step in path["steps"]:
        distance = convert_to_meters(step["distance"]["text"])
        duration = convert_to_seconds(step["duration"]["text"])
        start_coordinates = {"lat": step["start_location"]["lat"], "lon": step["start_location"]["lng"]}
        end_coordinates = {"lat": step["end_location"]["lat"], "lon": step["end_location"]["lng"]}
        instruction = re.sub(pattern, '', step["html_instructions"])
        steps.append(Step(start_coordinates, end_coordinates, distance, duration, instruction).serialize())

    return steps


def convert_to_meters(value: str) -> int:
    numeric_value = float(value.split(" ")[0])
    if "km" in value:
        return int(numeric_value * 1000)
    return int(numeric_value)


def convert_to_seconds(value: str) -> int:
    numeric_value = int(value.split(" ")[0])
    if "h" in value:
        return numeric_value * 60 * 60
    return numeric_value * 60
