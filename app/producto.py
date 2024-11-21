# producto.py
class Producto:
    def __init__(self, nombre, descripcion, precio, stock, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.proveedor = None

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

    def calcular_valor_total(self):
        return self.precio * self.stock
