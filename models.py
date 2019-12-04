import json

from tortoise.models import Model
from tortoise import fields


with open('config.json') as config_file:
    db_config = json.load(config_file)["database"]


class Tour(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    data = fields.JSONField(default=dict)

    def __str__(self):
        return self.name


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        return self.name
