# coding=utf-8

from marshmallow import Schema, fields, post_load

class StatisticRequest(object):
    def __init__(self, **data):
        self.login = data['login']
        self.game_name = data['game_name']
        self.points = data['points']

class StatisticRequestSchema(Schema):
    login = fields.String()
    game_name = fields.String()
    points = fields.Integer()

    @post_load
    def makeStatisticRequest(self, data):
        return StatisticRequest(**data)
