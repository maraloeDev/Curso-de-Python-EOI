"""
RETO: ANALIZADOR DE TEXTO ESTADÍSTICO

-------------------------------------

OBJETIVO:
Desarrollar un programa que procese un archivo de texto externo para realizar
un conteo de frecuencias tanto a nivel de palabras como de caracteres. Opcionalmente,
el programa también puede ordenar los resultados de mayor a menor frecuencia.


CONCEPTOS CLAVE A PRACTICAR:

1. GESTIÓN DE FICHEROS: Uso de 'with open' y manejo de errores (FileNotFoundError).

2. LIMPIEZA DE DATOS: Normalización de texto (lower) y eliminación de ruido
   usando la librería 'string'.

3. ESTRUCTURAS DE DATOS PRO: Uso de 'defaultdict' de la librería 'collections'
   para evitar errores de claves inexistentes.

4. LÓGICA DE CONTEO: Bucles anidados para procesar estructuras (Palabra -> Letra).

5. [OPCIONAL]ALGORITMOS DE ORDENACIÓN: Uso de 'sorted' con funciones 'lambda' para
   ordenar diccionarios por sus valores de mayor a menor.
"""
import string
from collections import defaultdict

ruta_archivo = "/home/eduardo/IdeaProjects/Curso-de-Python-EOI/Chapter02/Unit015/Ejercicios/Cuento_demo.txt"

# 2. ESTRUCTURAS DE DATOS PRO: Inicialización con defaultdict
frec_palabras = defaultdict(int)
frec_letras = defaultdict(int)

try:

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    tabla_limpieza = str.maketrans("", "", string.punctuation + "¡!¿?«»")
    texto_limpio = contenido.lower().translate(tabla_limpieza)


    palabras = texto_limpio.split()
    for palabra in palabras:
        frec_palabras[palabra] += 1  # Conteo de palabras
        for letra in palabra:
            frec_letras[letra] += 1  # Conteo de letras individual

    # --- RESULTADOS GENERALES ---
    print("================================")
    print("   ESTADÍSTICAS DEL CUENTO")
    print("================================")
    print(f"Total de palabras únicas: {len(frec_palabras)}")
    print(f"Total de letras procesadas: {sum(frec_letras.values())}")

    # 6. ORDENACIÓN (TOP 10 PALABRAS): Uso de lambda y sorted
    top_10_palabras = sorted(frec_palabras.items(), key=lambda x: x[1], reverse=True)[:10]

    print(f"\n{'RANGO':<5} {'PALABRA':<15} {'FRECUENCIA'}")
    print("-" * 35)
    for i, (pal, freq) in enumerate(top_10_palabras, 1):
        print(f"{i:<5} {pal:<15} {freq}")

    # 7. LA LETRA REINA Y TOP 5 LETRAS
    top_letras = sorted(frec_letras.items(), key=lambda item: item[1], reverse=True)
    letra_ganadora, conteo_max = top_letras[0]

    print("\n--- ANÁLISIS DE CARACTERES ---")
    print(f"La letra reina es la '{letra_ganadora.upper()}' con {conteo_max} apariciones.")

    print("\nTop 5 Letras más usadas:")
    for letra, freq in top_letras[:5]:
        print(f" - {letra}: {freq} veces")

except FileNotFoundError:
    print(f"Error: El archivo no existe en la ruta: {ruta_archivo}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")