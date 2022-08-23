from flask_restful import Resource, reqparse
from model.Hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        hoteis_list = [c.to_dict() for c in HotelModel.query.all()]
        return {"Hoteis": hoteis_list}, 200

class Hotel(Resource):
    def get(self, id):
        hotel = HotelModel.encontre_Hotel(id)
        if hotel:
            return {"Hotel": hotel.to_dict()} , 200
        return {"ERRO": "Hotel não encontrado"} , 404

    def post(self, id):
        hotel = HotelModel.encontre_Hotel(id)
        if hotel:
            return {"Mensagem": f"hotel com conta {id} já existe"} , 409
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("nome",location="form", required=True, type=str)
        parser.add_argument("cidade",location="form", required=True, type=str)
        parser.add_argument("qtdEstrelas", location="form", required=True, type=int)
        parser.add_argument("diaria", location="form", required=True, type=float)
        parser.add_argument("qtdQuartos", location="form", required=True, type=int)
        parser.add_argument("cafeManha", location="form", required=True, type=bool)
        dados = parser.parse_args()
        novo_hotel = HotelModel(id = id, **dados)
        novo_hotel.save_hoteis()
        return {"Mensagem": "Hotel cadastrado com sucesso!"},201

    def delete(self, id):
        hotel = HotelModel.encontre_Hotel(id)
        if hotel:
            hotel.delete_hotel()
            return {"Mensagem": f"hotel com conta {id} foi EXCLUIDO!"} , 202
        return {"Mensagem": f"hotel com conta {id} não foi encontrado!"}, 409


    def put(self, id):

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("nome", location="form", required=True, type=str)
        parser.add_argument("cidade", location="form", required=True, type=str)
        parser.add_argument("qtdEstrelas", location="form", required=True, type=int)
        parser.add_argument("diaria", location="form", required=True, type=float)
        parser.add_argument("qtdQuartos", location="form", required=True, type=int)
        parser.add_argument("cafeManha", location="form", required=True, type=bool)
        args = parser.parse_args()
        dados = parser.parse_args()
        hotel = HotelModel.encontre_Hotel(id)
        if hotel:
            hotel.update_hotel(**dados)
            hotel.save_hoteis()
            return {"Mensagem": f"Cadastro atualizado com sucesso!"}, 200
        return {"Mensagem": f"hotel com conta {id} não foi encontrado!"}, 409



