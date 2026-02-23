# Función ZIP

# La función zip() en Python es una herramienta integrada muy útil que se utiliza para combinar elementos de dos o más iterables (como listas, tuplas o diccionarios) en un solo objeto.
#Imagina que zip() funciona como una cremallera (de hecho, de ahí viene su nombre en inglés): une los elementos que están en la misma posición en diferentes contenedores.

nombres = ["Ana", "Luis", "Marta"]
edades = [25, 30, 22]

# Combinamos con zip
resultado = zip(nombres, edades)

# Para ver el resultado, lo convertimos a una lista
print(list(resultado))
# Salida: [('Ana', 25), ('Luis', 30), ('Marta', 22)]