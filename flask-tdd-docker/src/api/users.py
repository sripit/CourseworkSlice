from flask import Blueprint, request
#what is fields
from flask_restx import Resource, Api, fields # updated

from src import db
from src.api.models import User

#isort skip comment prevents isort from formatting the associated import
from src.api.crud import ( #isort:skip
    get_all_users,
    get_user_by_email,
    add_user,
    get_user_by_id,
    update_user,
    delete_user,

)

users_namespace = Namespace("users")
#users_blueprint = Blueprint('users', __name__)
#api = Api(users_blueprint)

user = users_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)

class UsersList(Resource):
    @users_namespace.marshal_with(user, as_list=True)
    def get(self):
        """Returns all users."""  # new
        return User.query.all(), 201

    @users_namespace.expect(user, validate=True)
    @users_namespace.response(201, "<user_email> was added!")  # new
    @users_namespace.response(400, "Sorry. That email already exists.")  # new

    def post(self):
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        response_object = {}

        #db.session.add(User(username=username, email=email))
        #db.session.commit()

        #response_object = {
            #'message': f'{email} was added!'
        #}
        user = get_user_by_email(email)
        if user:
            response_object['message'] = 'Sorry. That email already exists'
            return response_object, 400

        #db.session.add(User(username=username, email=email))
        #db.session.commit()
        add_user(username, email)

        response_object['message'] = f'{email} was added!'
        return response_object, 201



#api.add_resource(UsersList, '/users')
#user = api.model('User', {
    #'id': fields.Integer(readOnly=True),
    #'username': fields.String(required=True),
    #'email': fields.String(required=True),
    #'created_date': fields.DateTime,
#})

#api.add_resource(UsersList, '/users')

class Users(Resource):

    @users_namespace.marshal_with(user)
    @users_namespace.response(200, "Success")  # new
    @users_namespace.response(404, "User <user_id> does not exist")  # new
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")
        return user, 200
    @users_namespace.expect(user, validate=True)
    @users_namespace.response(200, "<user_id> was updated!")  # new
    @users_namespace.response(400, "Sorry. That email already exists.")  # new
    @users_namespace.response(404, "User <user_id> does not exist")  # new
    def put(self, user_id):
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        response_object = {}

        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")

        if get_user_by_email(email):
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400

        update_user(user, username, email)


        response_object["message"] = f"{user.id} was updated!"
        return response_object, 200

    @users_namespace.response(200, "<user_id> was removed!")  # new
    @users_namespace.response(404, "User <user_id> does not exist")  # new
    def delete(self, user_id):
        response_object = {}
        user = get_user_by_id(user_id)

        if not user:
            users_namespace.abort(404, f"User {user_id} does not exist")

        delete_user(user)

        response_object["message"] = f"{user.email} was removed!"
        return response_object, 200
users_namespace.add_resource(UsersList, "")
users_namespace.add_resource(Users, "/<int:user_id>")




