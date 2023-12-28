from flask import Flask, escape, request
import requests

app = Flask(__name__)


#one type 
@app.route('/')
def helloworld():
    course = request.args["course"]
    rating = request.args.get("rating")
    return {"message" : f"{course} with rating {rating}" }

# calling External Apis through Flask
@app.route('/')
def get_author():
    res = requests.get("https://openlibrary.org/search/authors.JSON?q=Michael Crichton") # requesting authors data from open library
    if res.status_code == 200:
        return { "message" : res.JSON()}, 200
    elif res.status_code == 404:
        return { "message" : "something went wrong!"}, 404
    else:
        return {"message" : "Server error!"}, 500


# Dynamic Routing using flask
@app.route('/book/<isbn>')
def got_author(isbn):
    res = requests.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON")

    if res.status_code == 200:
        return { "message" : res.JSON()}, 200
    elif res.status_code == 404:
        return { "message" : "something went wrong!"}, 404
    else:
        return {"message" : "Server error!"}, 500
