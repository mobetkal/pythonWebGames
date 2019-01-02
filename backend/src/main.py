# coding=utf-8

from flask_cors import CORS
from flask import Flask, jsonify, request

from .entities.entity import Session
from .entities.user import User, UserSchema
from .entities.statistics import Statistic, StatisticSchema

from .request.userRequest import UserRequestSchema
from .request.registerRequest import RegisterRequestSchema
from .request.statisticRequest import StatisticRequestSchema

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

@app.route('/score', methods=['POST'])
def update_statistic():
    statistic_request = StatisticRequestSchema(only=('login', 'game_name', 'points')). \
        load(request.get_json())

    session = Session()
    stat_object = session.query(Statistic). \
        filter(Statistic.login == statistic_request.data.login, Statistic.game_name == statistic_request.data.game_name). \
        first()

    stat = StatisticSchema().dump(stat_object)

    if 'login' in stat.data:
        if statistic_request.data.points > stat.data['points']:
            session.query(Statistic). \
                filter(Statistic.login == statistic_request.data.login, Statistic.game_name == statistic_request.data.game_name). \
                update({"points": statistic_request.data.points})
            session.commit()
            session.close()
            return jsonify(''), 400
        else:
            session.close()
            return jsonify(''), 200
    else:
        statistic_schema = StatisticSchema(only=('login', 'game_name', 'points')). \
            load(request.get_json())
        statistic = Statistic(**statistic_schema.data)

        session.add(statistic)
        session.commit()
        session.close()
        return jsonify(''), 200