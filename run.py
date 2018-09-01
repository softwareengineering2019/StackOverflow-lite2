"""
   Module for starting/ running the app
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from api.routes.routes import GetRoutes

app = Flask(__name__)
app.config.from_object('api.config.DevelopmentConfig')
GetRoutes.fetch_routes(app)

app.config['JWT_SECRET_KEY'] = 'kjdkhfdfi'
jwt = JWTManager(app)

if __name__ == '__main__':    
    app.run()
    