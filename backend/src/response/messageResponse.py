# coding=utf-8

from marshmallow import Schema, fields, post_load

class MessageResponse(object):
    def __init__(self, **data):
        self.message = data['message']

class MessageResponseSchema(Schema):
    message = fields.String()

    @post_load
    def makeMessageResponse(self, data):
        return MessageResponse(**data)
