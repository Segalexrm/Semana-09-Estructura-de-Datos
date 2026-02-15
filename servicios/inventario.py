# servicios/inventario.py
from modelos.producto import Producto

class Inventario:
    def __init__(self):
        # Estructura principal de almacenamiento
        self.productos = []

    def añadir_producto(self, producto):
        # Validar que el ID no esté repetido
        if any(p.id == producto.id for p in self.productos):
            print(f"Error: El ID {producto.id} ya existe.")
            return False
        self.productos.append(producto)
        print("Producto añadido con éxito.")
        return True

    def eliminar_producto(self, id_buscar):
        for p in self.productos:
            if p.id == id_buscar:
                self.productos.remove(p)
                print(f"Producto {id_buscar} eliminado.")
                return True
        print("Error: Producto no encontrado.")
        return False

    def actualizar_producto(self, id_buscar, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_buscar:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                print("Producto actualizado.")
                return True
        print("Error: Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre_parcial):
        # Coincidencias parciales (case insensitive)
        resultados = [p for p in self.productos if nombre_parcial.lower() in p.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(p)