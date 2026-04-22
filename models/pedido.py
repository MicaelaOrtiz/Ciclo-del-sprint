class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        self.estado = "Pendiente"
        self.total = sum(p["precio"] for p in productos)