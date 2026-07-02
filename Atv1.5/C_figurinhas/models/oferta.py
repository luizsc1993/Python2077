from . import db
from .base import ModeloBase

class OfertaTroca(ModeloBase):
    __tablename__ = "ofertas_troca"

    # Chave Estrangeira vinculando a oferta ao criador (Colecionador)
    colecionador_id = db.Column(db.Integer, db.ForeignKey("colecionadores.id"), nullable=False)
    observacao = db.Column(db.String(255), nullable=True)

    # Relacionamentos da Oferta
    colecionador = db.relationship("Colecionador", back_populates="ofertas")
    itens = db.relationship("ItemOferta", back_populates="oferta")

    @classmethod
    def listar_com_colecionador(cls):
        return cls.query.order_by(cls.data_criacao.desc()).all()


class ItemOferta(ModeloBase):
    __tablename__ = "itens_alta"

    # Chaves Estrangeiras vinculando o item à sua respectiva Oferta e à Figurinha
    oferta_id = db.Column(db.Integer, db.ForeignKey("ofertas_troca.id"), nullable=False)
    figurinha_id = db.Column(db.Integer, db.ForeignKey("figurinhas.id"), nullable=False)
    
    tipo = db.Column(db.String(20), nullable=False) # "oferece" ou "deseja"
    quantidade = db.Column(db.Integer, nullable=False, default=1)

    # Relacionamentos do Item
    oferta = db.relationship("OfertaTroca", back_populates="itens")
    figurinha = db.relationship("Figurinha")