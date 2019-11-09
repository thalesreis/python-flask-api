from flask import Flask
from flask_restful import Api


app = Flask(__name__)

wineApi = Api(app)

import api.data.db_setup
import api.views
import api.controllers.wine_controller as wine_controller

# rotas do vinho
wineApi.add_resource(wine_controller.WineCreate, '/wine')


# Registra as rotas/resources para cada controller
# wineApi.add_resource(user_controller.UserRegistration, '/registration')
# wineApi.add_resource(user_controller.UserLogin, '/login')
# wineApi.add_resource(user_controller.UserLogoutAccess, '/logout/access')
# wineApi.add_resource(user_controller.UserLogoutRefresh, '/logout/refresh')
# wineApi.add_resource(user_controller.TokenRefresh, '/token/refresh')
# wineApi.add_resource(user_controller.AllUsers, '/users')
# wineApi.add_resource(user_controller.SecretResource, '/secret')