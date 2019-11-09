from flask_restful import Resource, reqparse
from api.models.wine_model import WineModel

#https://flask-restful.readthedocs.io/en/latest/reqparse.html
parser = reqparse.RequestParser()
parser.add_argument('name', help = 'This field cannot be blank', required = True)
parser.add_argument('price', help = 'This field cannot be blank', required = True)

class WineCreate(Resource):
    def get(self):
        data = parser.parse_args()

        wine = WineModel(
            name = data['name'],
            price = data['price']
        )
        
        wine.save_to_db()

        return 'ok'

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        req_username = data['username']

        # if UserModel.find_by_username(req_username):
            # return {
                # 'message': 'User {} already exists'.format(req_username)
            # }

        # user_new = UserModel(
            # username = req_username,
            # password = data['password']
        # )
        try:
            # user_new.save_to_db()
            return {
                'message': 'User {} was created'.format(req_username)
            }
        except:
            return {'message': 'Algo deu errado'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return data