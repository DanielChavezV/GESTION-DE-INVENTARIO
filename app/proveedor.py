# proveedor.py
class Proveedor:
    def __init__(self, nombre, direccion, telefono, productos=None):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = productos or []

    def agregar_producto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

