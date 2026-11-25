
from algoritmos import (
    burbuja,
    merge_sort,
    busqueda_lineal,
    busqueda_binaria
)


def mostrar_menu():
    print("\n================================")
    print("   ALGORITMOS DE ORDENAMIENTO")
    print("        Y DE BÚSQUEDA")
    print("================================")
    print("1. Ordenamiento Bubble Sort")
    print("2. Ordenamiento Merge Sort")
    print("3. Búsqueda lineal")
    print("4. Búsqueda binaria")
    print("5. Salir")


def main():
    datos = [45, 12, 78, 23, 9, 56, 34]

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            resultado = burbuja(datos)
            print("Datos originales:", datos)
            print("Resultado Bubble Sort:", resultado)

        elif opcion == "2":
            resultado = merge_sort(datos)
            print("Datos originales:", datos)
            print("Resultado Merge Sort:", resultado)

        elif opcion == "3":
            try:
                valor = int(input("Ingrese el número que desea buscar: "))
                posicion = busqueda_lineal(datos, valor)

                if posicion != -1:
                    print(f"Elemento encontrado en la posición {posicion}.")
                else:
                    print("El elemento no se encuentra en la lista.")

            except ValueError:
                print("Error: debe ingresar un número entero.")

        elif opcion == "4":
            try:
                valor = int(input("Ingrese el número que desea buscar: "))
                datos_ordenados = merge_sort(datos)
                posicion = busqueda_binaria(datos_ordenados, valor)

                if posicion != -1:
                    print(
                        f"Elemento encontrado en la posición {posicion} "
                        "de la lista ordenada."
                    )
                else:
                    print("El elemento no se encuentra en la lista.")

            except ValueError:
                print("Error: debe ingresar un número entero.")

        elif opcion == "5":
            print("Gracias por utilizar el programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
