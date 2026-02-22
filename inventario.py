from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # -----------------------------
    # CARGAR DESDE ARCHIVO
    # -----------------------------
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_p, nombre, cantidad, precio = datos
                        producto = Producto(id_p, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            with open(self.archivo, "w") as f:
                pass
            print("Archivo inventario.txt creado porque no existía.")

        except PermissionError:
            print("Error: No se tienen permisos para acceder al archivo.")

    # -----------------------------
    # GUARDAR EN ARCHIVO
    # -----------------------------
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    f.write(linea)
            print("Cambios guardados correctamente en el archivo.")

        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")

    # -----------------------------
    # AÑADIR PRODUCTO
    # -----------------------------
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")

    # -----------------------------
    # ELIMINAR PRODUCTO
    # -----------------------------
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    # -----------------------------
    # ACTUALIZAR PRODUCTO
    # -----------------------------
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    # -----------------------------
    # BUSCAR POR NOMBRE
    # -----------------------------
    def buscar_por_nombre(self, nombre):
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)
        return encontrados

    # -----------------------------
    # MOSTRAR TODOS
    # -----------------------------
    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
