# main.py
from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():
    sistema = Inventario()

    while True:
        print("\n- SISTEMA DE GESTIÓN DE INVENTARIOS -")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID unico: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                nuevo = Producto(id_p, nom, cant, pre)
                sistema.añadir_producto(nuevo)
            except ValueError:
                print("Error: Cantidad y Precio deben ser numeros.")

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            sistema.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            try:
                cant = int(input("Nueva cantidad (dejar vacío para no cambiar): ") or -1)
                pre = float(input("Nuevo precio (dejar vacío para no cambiar): ") or -1)
                sistema.actualizar_producto(id_p,
                                            nueva_cantidad=cant if cant != -1 else None,
                                            nuevo_precio=pre if pre != -1 else None)
            except ValueError:
                print("Error en el formato de los datos.")

        elif opcion == "4":
            nom = input("Ingrese el nombre (o parte del nombre) a buscar: ")
            encontrados = sistema.buscar_por_nombre(nom)
            for e in encontrados: print(e)

        elif opcion == "5":
            sistema.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()