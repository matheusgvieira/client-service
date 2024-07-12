from datetime import datetime
from .database import db


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(120), nullable=False)
    endereco = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    client_id = db.Column(db.String(60), unique=True, nullable=False)
    client_secret = db.Column(db.String(60), unique=True, nullable=False)
    data_inclusao = db.Column(db.DateTime, default=datetime.utcnow)
