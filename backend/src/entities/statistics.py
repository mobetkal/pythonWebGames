# coding=utf-8

from sqlalchemy import Column, String, Integer
from marshmallow import Schema, fields

from .entity import Entity, Base


class Statistic(Entity, Base):
    __tablename__ = 'statistics'

    login = Column(String)
    game_name = Column(String)
    points = Column(Integer)

    def __init__(self, login, game_name, points):
        Entity.__init__(self)
        self.login = login
        self.game_name = game_name
        self.points = points

class StatisticSchema(Schema):
    id = fields.Number()
    login = fields.Str()
    game_name = fields.Str()
    points = fields.Number()
    created_at = fields.DateTime()
