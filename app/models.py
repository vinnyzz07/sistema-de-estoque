from app import db
from datetime import datetime

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    descricao = db.Column(db.String(200))

    produtos = db.relationship('Produto', backref='categoria', lazy=True)

    def __repr__(self):
        return f'<Categoria {self.nome}>'

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(300))
    quantidade = db.Column(db.Integer, default=0, nullable=False)
    quantidade_minima = db.Column(db.Integer, default=5, nullable=False)
    preco = db.Column(db.Float, default=0.0)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    movimentacoes = db.relationship('Movimentacao', backref='produto', lazy=True)

    def estoque_baixo(self):
        return self.quantidade <= self.quantidade_minima

    def __repr__(self):
        return f'<Produto {self.nome}>'

class Movimentacao(db.Model):
    __tablename__ = 'movimentacoes'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10), nullable=False)  # 'entrada' ou 'saida'
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    observacao = db.Column(db.String(200))
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)

    def __repr__(self):
        return f'<Movimentacao {self.tipo} - {self.quantidade}>'