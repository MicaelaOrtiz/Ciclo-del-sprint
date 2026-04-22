from flask import Blueprint, request, jsonify
from models.pedido import Pedido

pedidos_bp = Blueprint("pedidos", __name__)

pedidos = []

@pedidos_bp.route("/pedidos", methods=["POST"])
def crear_pedido():
    data = request.json
    nuevo = Pedido(data["cliente"], data["productos"])
    pedidos.append(nuevo.__dict__)
    return jsonify(nuevo.__dict__), 201


@pedidos_bp.route("/pedidos", methods=["GET"])
def ver_pedidos():
    return jsonify(pedidos)


@pedidos_bp.route("/pedidos/<int:index>/estado", methods=["PUT"])
def cambiar_estado(index):
    pedidos[index]["estado"] = request.json["estado"]
    return jsonify(pedidos[index])