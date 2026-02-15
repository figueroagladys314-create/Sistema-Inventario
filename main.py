from inventario import Inventario
from producto import Producto

def menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("Ingrese ID: ")
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Cantidad debe ser entero y precio decimal.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            try:
                cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
                precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error en los datos ingresados.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

