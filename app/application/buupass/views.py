from flask import render_template, redirect, url_for, request, flash, session, jsonify

from . import buupass
from .model import homes, hotels, flights, experiences, cars


@buupass.route("/home")
def index():
    return render_template("index.html")


@buupass.route("/api/v1/resources/homes", methods=["GET"])
def search_homes():
    query_params = request.args
    location = query_params.get("location")
    capacity = query_params.get("capacity")
    no_of_rooms = query_params.get("no_of_rooms")
    if not location or not capacity or not no_of_rooms:
        return "Kindly fill in all the fields"
    results = []

    for home in homes:
        if (
            home["location"] == location
            and home["capacity"] == capacity
            and home["no_of_rooms"] == no_of_rooms
        ):
            results.append(home)

    return jsonify(results)


@buupass.route("/api/v1/resources/hotels", methods=["GET"])
def search_hotels():
    query_params = request.args
    location = query_params.get("location")
    capacity = query_params.get("capacity")
    no_of_rooms = query_params.get("no_of_rooms")
    if not location or not capacity or not no_of_rooms:
        return "Kindly fill in all the fields"
    results = []

    for hotel in hotels:
        if (
            hotel["location"] == location
            and hotel["capacity"] == capacity
            and hotel["no_of_rooms"] == no_of_rooms
        ):
            results.append(hotel)

    return jsonify(results)


@buupass.route("/api/v1/resources/cars", methods=["GET"])
def search_cars():
    query_params = request.args
    type_ = query_params.get("type")
    capacity = query_params.get("capacity")
    price = query_params.get("price")
    if not type_ or not capacity or not price:
        return "Kindly fill in all the fields"

    results = []

    for car in cars:
        if (
            car["type"] == type_
            and car["capacity"] == capacity
            and car["price"] == price
        ):
            results.append(car)
    return jsonify(results)


@buupass.route("/api/v1/resources/experiences", methods=["GET"])
def search_experiences():
    query_params = request.args
    experience_ = query_params.get("experience")
    if not experience_:
        return "Kindly fill in all the fields"

    results = []

    for experience in experiences:
        if experience["experience"] == experience_:
            results.append(experience)

    return jsonify(results)


@buupass.route("/api/v1/resources/flights", methods=["GET"])
def search_flights():
    query_params = request.args
    destination = query_params.get("destination")
    arrival = query_params.get("arrival")
    departure = query_params.get("departure")
    route = query_params.get("route")
    if not destination or not arrival or not departure or not route:
        return "Kindly fill in all the fields"

    results = []

    for flight in flights:
        if (
            flight["destination"] == destination
            and flight["arrival"] == arrival
            and flight["route"] == route
            and flight["departure"] == departure
        ):
            results.append(flight)

    return jsonify(results)


@buupass.route("/api/v1/resources/homes/all", methods=["GET"])
def get_homes():
    return jsonify(homes)


@buupass.route("/api/v1/resources/hotels/all", methods=["GET"])
def get_hotels():
    return jsonify(hotels)


@buupass.route("/api/v1/resources/cars/all", methods=["GET"])
def get_cars():
    return jsonify(cars)


@buupass.route("/api/v1/resources/experiences/all", methods=["GET"])
def get_experiences():
    return jsonify(experiences)


@buupass.route("/api/v1/resources/flights/all", methods=["GET"])
def get_flights():
    return jsonify(flights)
