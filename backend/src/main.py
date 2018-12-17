# coding=utf-8

from flask_cors import CORS
from flask import Flask, jsonify, request

from .entities.entity import Session
from .entities.user import User, UserSchema

from .request.userRequest import UserRequestSchema
from .request.registerRequest import RegisterRequestSchema

from .response.messageResponse import MessageResponse, MessageResponseSchema
from .response.loginResponse import LoginResponse, LoginResponseSchema

# Creating the application
app = Flask(__name__)
CORS(app)


# Methods of capturing requests...
@app.route('/login', methods=['POST'])
def login():
    user_request = UserRequestSchema(only=('login', 'password')).\
        load(request.get_json())

    session = Session()
    user_object = session.query(User).\
        filter(User.login == user_request.data.login, User.password == user_request.data.password).\
        first()

    session.close()

    users = UserSchema().dump(user_object)

    if 'login' in users.data:
        login_success_response = LoginResponseSchema().\
            dump(LoginResponse(**users.data)).data
        return jsonify(login_success_response)
    else:
        message_response = MessageResponseSchema().\
            dump(MessageResponse(message="The login or password you entered is incorrect. Please try again.")).data
        return jsonify(message_response), 403

@app.route('/register', methods=['POST'])
def register():
    register_request = RegisterRequestSchema(only=('login', 'password', 'first_name', 'last_name')). \
        load(request.get_json())

    session = Session()
    user_object = session.query(User).\
        filter(User.login == register_request.data.login).\
        first()

    users = UserSchema().dump(user_object)

    if 'login' in users.data:
        session.close()
        message_response = MessageResponseSchema().\
            dump(MessageResponse(message="The account with the login already exists. Please try pick another.")).data
        return jsonify(message_response), 403
    else:
        registered_user_map = UserSchema(only=('login', 'password', 'first_name', 'last_name')).\
            load(request.get_json())

        registered_user = User(**registered_user_map.data)

        session.add(registered_user)
        session.commit()

        user_object = session.query(User). \
            filter(User.login == register_request.data.login). \
            first()

        users = UserSchema().dump(user_object)
        session.close()

        login_success_response = LoginResponseSchema(). \
            dump(LoginResponse(**users.data)).data

        return jsonify(login_success_response)