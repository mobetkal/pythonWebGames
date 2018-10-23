# coding=utf-8

from flask_cors import CORS
from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base

# Creating the application
app = Flask(__name__)
CORS(app)

Base.metadata.create_all(engine)

# Methods of capturing requests...
