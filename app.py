from flask import Flask
from flask_restful import Api
from model.Hotel import bd
from resources.Banco import Hoteis, Hotel
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:id>')
@app.before_first_request
def criar_banco():
    bd.init_app(app)
    bd.create_all()
if __name__ == '__main__':
    app.run(debug=True)