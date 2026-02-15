from producto import Producto

# Clase Inventario
# Utiliza una lista (estructura de datos compuesta y mutable)
# para almacenar los productos.

class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar objetos Producto

    def añadir_producto(self, producto):
        # Verificar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
