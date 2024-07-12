from flask import Flask, request, jsonify
from .config import Config
from .database import db
from .models import Cliente
import uuid


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    @app.route("/clientes", methods=["POST"])
    def cadastrar_cliente():
        data = request.json
        client_id = str(uuid.uuid4())
        client_secret = str(uuid.uuid4())
        cliente = Cliente(
            nome_completo=data["nome_completo"],
            endereco=data["endereco"],
            email=data["email"],
            client_id=client_id,
            client_secret=client_secret,
        )
        db.session.add(cliente)
        db.session.commit()
        return (
            jsonify(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "data_inclusao": cliente.data_inclusao,
                }
            ),
            201,
        )

    @app.route("/clientes", methods=["GET"])
    def listar_clientes():
        clientes = Cliente.query.all()
        return (
            jsonify(
                [
                    {
                        "id": cliente.id,
                        "nome_completo": cliente.nome_completo,
                        "endereco": cliente.endereco,
                        "email": cliente.email,
                        "client_id": cliente.client_id,
                        "client_secret": cliente.client_secret,
                        "data_inclusao": cliente.data_inclusao,
                    }
                    for cliente in clientes
                ]
            ),
            200,
        )

    return app
