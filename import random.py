import random
import time

def medir(funcion, datos):
    """Devuelve el tiempo en segundos que tarda funcion(datos)."""
    copia = list(datos)

    inicio = time.perf_counter()
    funcion(copia)
    fin = time.perf_counter()

    return fin - inicio


tamanos = [1000, 2000, 4000, 8000]
anterior = None

print(f"{'n':>6} {'tiempo(s)':>12} {'razon':>8}")

for n in tamanos:
    datos = [random.randint(1, 10**6) for _ in range(n)]

    # Reemplazar por el algoritmo que se desea medir
    t = medir(merge_sort, datos)

    razon = f"{t/anterior:.2f}" if anterior else "-"

    print(f"{n:>6} {t:>12.5f} {razon:>8}")

    anterior = t