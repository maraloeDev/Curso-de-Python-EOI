# --- RESUMEN: UNIDAD 26 - TABLAS HASH ---

"""
DEFINICIÓN:
Una Tabla Hash (o Hash Map) es un tipo de dato abstracto que almacena y extrae
datos mediante el mapeo de 'llaves' (keys) a 'valores' (values) a través de
un proceso llamado 'hashing'.

COMPONENTES CLAVE:
1. Llave (Key): El identificador único (ej: el título de un libro).
2. Función Hash: El algoritmo que transforma la llave en un índice numérico.
3. Tabla Hash: La estructura (como un estante) donde se guarda la información.
"""

# 1. EJEMPLO DE FUNCIÓN HASH
# En tus diapositivas, se usa la suma de códigos ASCII para crear una llave.
def generar_hash_simple(texto):
    # La función ord() devuelve el código ASCII de cada carácter.
    # Ejemplo: "The Last Leaf" -> 1133.
    return sum(map(ord, texto))

# 2. ESTRUCTURA DE LA TABLA
# Una tabla hash debe proporcionar tres interfaces significativas:
class TablaHashResumen:
    def __init__(self, tamaño=8):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño # Estante con 8 ranuras

    def hash_function(self, key):
        """Convierte la llave en un índice dentro del rango de la tabla."""
        return generar_hash_simple(key) % self.tamaño

    def put(self, key, value):
        """Almacena el valor en la cubeta designada por el hash."""
        indice = self.hash_function(key)
        self.tabla[indice] = (key, value)
        print(f"Guardado '{key}' en el índice {indice}")

    def get(self, key):
        """Extrae el valor almacenado mediante la llave."""
        indice = self.hash_function(key)
        return self.tabla[indice]

# --- CASO DE ESTUDIO: BIBLIOTECA ---
libros = [
    "The Little Prince",      # Hash ASCII: 1584
    "The Old Man and the Sea",# Hash ASCII: 1929
    "The Little Mermaid",     # Hash ASCII: 1678
    "Beauty and the Beast",   # Hash ASCII: 1837
    "The Last Leaf"           # Hash ASCII: 1133
]

# Ejemplo de uso:
mi_biblioteca = TablaHashResumen()

# Al guardar los libros, la función hash decide en qué 'slot' del 1 al 8 van.
for libro in libros:
    mi_biblioteca.put(libro, "Disponible")

print("\nEstructura final de la tabla:", mi_biblioteca.tabla)