from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()


class HotelModel(bd.Model):
    __tablename__ = "hoteis"
    id = bd.Column(bd.String, primary_key=True)
    nome = bd.Column(bd.String(100), nullable=False)
    cidade = bd.Column(bd.String(100), nullable=False)
    qtdEstrelas = bd.Column(bd.Integer, nullable=False)
    diaria = bd.Column(bd.Float(precision=2), nullable=False)
    qtdQuartos = bd.Column(bd.Integer, nullable=False)
    cafeManha = bd.Column(bd.Boolean, nullable=None)

    @classmethod
    def encontre_Hotel(cls, id):
        hotel = cls.query.get(id)
        return None if not hotel else hotel

    def update_hotel(self, **dados):
        self.nome = dados["nome"] or self.nome
        self.cidade = dados["cidade"] or self.cidade
        self.qtdEstrelas = dados["qtdEstrelas"] or self.qtdEstrelas
        self.diaria = dados["diaria"] or self.diaria
        self.qtdQuartos = dados["qtdQuartos"] or self.qtdQuartos
        self.cafeManha = dados["cafeManha"] or self.cafeManha

    def delete_hotel(self):
        bd.session.delete(self)
        bd.session.commit()

    def save_hoteis(self):
        bd.session.add(self)
        bd.session.commit()

    def to_dict(self):
        return {'id': self.id,
                'nome': self.nome,
                'cidade': self.cidade,
                'qtdEstrelas': self.qtdEstrelas,
                'diaria': self.diaria,
                'qtdQuartos': self.qtdQuartos,
                'cafeManha': self.cafeManha}