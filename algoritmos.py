
def burbuja(datos):
    """
    Ordena una lista utilizando el algoritmo Bubble Sort.
    Devuelve una nueva lista ordenada de menor a mayor.
    """
    lista = list(datos)
    n = len(lista)

    for i in range(n - 1):
        intercambio = False

        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True

        # Si no hubo intercambios, la lista ya está ordenada.
        if not intercambio:
            break

    return lista


def merge_sort(datos):
    """
    Ordena una lista utilizando el algoritmo Merge Sort.
    Devuelve una nueva lista ordenada de menor a mayor.
    """
    lista = list(datos)

    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2

    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    return combinar(izquierda, derecha)


def combinar(izquierda, derecha):
    """
    Combina dos listas ordenadas en una sola lista ordenada.
    """
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


def busqueda_lineal(datos, objetivo):
    """
    Busca un elemento recorriendo la lista desde el inicio.
    Devuelve su posición o -1 si no existe.
    """
    for i in range(len(datos)):
        if datos[i] == objetivo:
            return i

    return -1


def busqueda_binaria(datos, objetivo):
    """
    Busca un elemento mediante búsqueda binaria.
    La lista debe estar ordenada previamente.
    Devuelve su posición o -1 si no existe.
    """
    izquierda = 0
    derecha = len(datos) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if datos[medio] == objetivo:
            return medio

        elif datos[medio] < objetivo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return -1

