# coding=utf-8

from flask_cors import CORS
from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema

from .request.userRequest import UserRequest, UserRequestSchema

from .response.messageResponse import MessageResponse, MessageResponseSchema
from .response.loginResponse import LoginResponse, LoginResponseSchema

import sys

# Creating the application
app = Flask(__name__)
CORS(app)


# Methods of capturing requests...
@app.route('/login', methods=['POST'])
def login():
    userRequest = UserRequestSchema(only=('login', 'password')).\
        load(request.get_json())

    session = Session()
    userObject = session.query(User).\
        filter(User.login == userRequest.data.login, User.password == userRequest.data.password).\
        first()

    session.close()

    users = UserSchema().dump(userObject)

    if 'login' in users.data:
        loginSuccessResponse = LoginResponseSchema().\
            dump(LoginResponse(**users.data)).data
        return jsonify(loginSuccessResponse)
    else:
        messageResponse = MessageResponseSchema().\
            dump(MessageResponse(message="The login or password you entered is incorrect. Please try again.")).data
        return jsonify(messageResponse), 403
