from flask import Flask

from .ext import db


def create_app(**config):
  app = Flask(__name__)
  app.config.update(**config)
  db.init_app(app)
  return app
