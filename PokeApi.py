# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:06:31 2019

@author: Yutyrannus
"""

from flask import *
from flask_pymongo import PyMongo



app = Flask(__name__)
api = Api(app)
app.config['MONGO_DBNAME'] = "Pokemon"
app.config["MONGO_URI"] = "mongodb+srv://jojo:weak@cluster0-ua5e8.mongodb.net/Pokemon"
mongo = PyMongo(app)


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/api/poke", methods=['GET'])
def GetPoke():
    items = list(mongo.db["pokemons"].find({}))

    return dumps(items)


@app.route("/api/shiny", methods=['GET'])
def GetShiny():
    items = list(mongo.db["shiny-pokemons"].find({}))
    

    return dumps(items)

@app.route("/api/items", methods=['GET'])
def GetItem():
    items = list(mongo.db["items"].find({}))

    return dumps(items)

if __name__ == '__main__':
     app.run(port=5002)
     

     
     
     
     
     
     
     