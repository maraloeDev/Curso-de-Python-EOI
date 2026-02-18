# ¿Qué es un archivo?
# Es una unidad lógica utilizada para almacenar datos en un dispositivo de almacenamiento (como un disco duro). Permite guardar información de forma permanente y recuperarla cuando sea necesario.

# 2. Pasos básicos para usar archivos en Python
# El proceso sigue siempre tres pasos esenciales:

# Abrir (Open): Se especifica el nombre y la ubicación (ruta).

# Usar (Read/Write): Leer el contenido, escribir nuevos datos o editar los existentes.

# Cerrar (Close): Es fundamental para liberar la memoria temporal (buffer) y asegurar que los datos se guarden correctamente en el disco.

# 3. Modos de apertura (Función open)
# El modo determina qué puedes hacer con el archivo:

# r (Read): Modo lectura (por defecto). Da error si el archivo no existe.

# w (Write): Modo escritura. Crea el archivo si no existe; si existe, sobrescribe todo el contenido.

# a (Append): Modo añadir. Agrega contenido al final del archivo sin borrar lo anterior.

# x (Exclusive creation): Crea un archivo nuevo; da error si ya existe.

# +: Permite actualización (lectura y escritura combinadas).

# 4. Tipos de archivos
# t (Text): Para archivos de texto (modo por defecto).

# b (Binary): Para archivos binarios (imágenes, ejecutables, etc.).

# Ejemplo: 'wb' abre un archivo para escritura en formato binario.

# 5. Funciones principales de código
# f = open('archivo.txt', 'modo'): Abre el archivo y devuelve un objeto de archivo.

# f.write('texto'): Escribe una cadena de texto en el archivo.

# f.read(): Lee todo el contenido del archivo y lo devuelve como una sola cadena.

# f.close(): Cierra el archivo. Es vital para la eficiencia de la memoria, ya que mueve los datos del "buffer" (memoria temporal) al disco físico.


# Escritura
f = open('hello.txt', 'w')
f.write('Hello World!')
f.close()

# Lectura
f = open('hello.txt', 'r')
contenido = f.read()
print(contenido)
f.close()