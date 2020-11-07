from flask import Flask, request, Response
import json
import random

app = Flask(__name__)
animals_list = ["Zebra", "Polar Bear", "Snake", "Tiger", "Lion", "Grizzly Bear", "Bald Eagle", "Peregrin Falcon", "Cat", "Dog", "Jaguar", "Chimpanzee"]

# GET, POST, PATCH, DELETE
@app.route('/animals', methods = ['GET', 'POST', 'PATCH','DELETE'])
def animals():
    if request.method == 'GET':
        return Response(json.dumps(animals_list, default = str), mimetype = "application/json", status = 200)

    elif request.method == 'POST':
        return Response("You've added a Turtle!", mimetype = "text/html", status = 201)

    elif request.method == 'PATCH':
        return Response("You've changed Turtle to Tortoise!", mimetype = "text/html", status = 201)

    elif request.method == 'DELETE':
        return Response("You've deleted Lion!", mimetype = "text/html", status = 201)
    
    else:
        return Response("There's an error!", mimetype = "text/html", status = 401)
