import time

from simpleflake import simpleflake

from .ext import db


def now():
  return int(time.time())


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.String(255), primary_key=True, default=simpleflake)
  name = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.Integer, default=now)

