import click
from app.app import create_app
from app.ext import db


@click.group()
@click.pass_context
def cli(ctx):
  ctx.obj = create_app()


@cli.command()
@click.pass_obj
def runserver(app):
  app.run(host="0.0.0.0")


@cli.command()
@click.option('--drop-tables', '-d', is_flag=True)
def initdb(drop_tables):
  if drop_tables:
    db.drop_all(app=app)
  db.create_all(app=app)


if __name__ == '__main__':
  cli()
