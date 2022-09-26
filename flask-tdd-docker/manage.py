#manage app from command line
from flask.cli import FlaskGroup

from src import create_app, db
src.api.users.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
if __name__=='__main__':
    cli()
#to extend normal CLI with commands related to Flask app

@cli.command('seed.db'):
def seed_db():
    db.session.add(User(username='michael', email="hermanmu@gmail.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.commit()