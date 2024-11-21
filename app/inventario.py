# inventario.py
class Inventario:
    def __init__(self):
        self.productos = []
        self.categorias = []
        self.proveedores = []
        self.bodegas = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)

    def agregar_bodega(self, bodega):
        self.bodegas.append(bodega)

    def listar_productos(self):
        return self.productos

    def listar_categorias(self):
        return self.categorias

    def listar_proveedores(self):
        return self.proveedores

    def listar_bodegas(self):
        return self.bodegas

    def agregar_stock(self, nombre_producto, cantidad):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            producto.agregar_stock(cantidad)
            return True
        return False

    def retirar_stock(self, nombre_producto, cantidad):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            return producto.retirar_stock(cantidad)
        return False

    def calcular_valor_total_stock(self):
        return sum(p.calcular_valor_total() for p in self.productos)

    def agregar_producto_a_proveedor(self, nombre_proveedor, producto):
        proveedor = next((p for p in self.proveedores if p.nombre == nombre_proveedor), None)
        if proveedor:
            proveedor.agregar_producto(producto)
        else:
            raise ValueError(f"No se encontró el proveedor '{nombre_proveedor}'")

    def eliminar_producto_de_proveedor(self, nombre_proveedor, nombre_producto):
        proveedor = next((p for p in self.proveedores if p.nombre == nombre_proveedor), None)
        if proveedor:
            producto = next((p for p in proveedor.productos if p.nombre == nombre_producto), None)
            if producto:
                proveedor.eliminar_producto(producto)
                return True
        return False

    def agregar_producto_a_bodega(self, nombre_bodega, producto, cantidad):
        bodega = next((b for b in self.bodegas if b.nombre == nombre_bodega), None)
        if bodega:
            return bodega.agregar_producto(producto, cantidad)
        raise ValueError(f"No se encontró la bodega '{nombre_bodega}'")

    def retirar_producto_de_bodega(self, nombre_bodega, producto, cantidad):
        bodega = next((b for b in self.bodegas if b.nombre == nombre_bodega), None)
        if bodega:
            return bodega.retirar_producto(producto, cantidad)
        raise ValueError(f"No se encontró la bodega '{nombre_bodega}'")

    def eliminar_producto_de_categoria(self, nombre_producto, nombre_categoria):
        categoria = next((c for c in self.categorias if c.nombre == nombre_categoria), None)
        if categoria:
            producto = next((p for p in categoria.productos if p.nombre == nombre_producto), None)
            if producto:
                categoria.eliminar_producto(producto)
                return True
        return False
