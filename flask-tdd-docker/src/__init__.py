import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy #do i need this?
from werkzeug.middleware.proxy_fix import ProxyFix

app.register_blueprint(users_blueprint)

#instantiate the db
db = SQLAlchemy()
admin = Admin(template_mode='bootstrap3')


#instantiate the app
def create_app(script_info = None, ping_blueprint=None, ping_blueprint=None):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

    #api = Api(app)


#set config
#used to configure flask and its extensions, made it available
    app_settings=os.getenv('APP_SETTINGS')
#above pulls in the environment variables
    app.config.from_object(app_settings)
    #set up extensions
    db.init_app(app)

    if os.getenv("FLASK_ENV") == 'development':
        admin.init_app(app)

    #register blueprints
    from src.api import api
    app.init_app(app)
    from src.api.users import users_blueprint

    #shell_context_processor is used to reguster the app and db to the shell
    @app.shell_context_processor

    def ctx():
        return {'app':app, 'db': db}
    return app


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

class Ping(Resource):
    def get(self):
        return{
            'status': 'success',
            'message': 'pong!'
        }
api.add_resource(Ping, '/ping')
#add_resource: adds a resource to api (obviously)
    #add_resource(resource, *urls, **kwargs)
        #second param is url route to match resource
        #third param allows you to pass keyword arguments to a function
            #keyword arguments: i am actually so stupid this is so basic
    #resource: class name of resource, which in this case is Ping

