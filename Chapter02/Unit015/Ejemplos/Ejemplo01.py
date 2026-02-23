from collections import defaultdict

# 1. Creamos una lista de llaves (como en tu imagen 1.2)
categorias = ['Frutas', 'Verduras', 'Lácteos']

# 2. Inicializamos un diccionario usando fromkeys (Imagen 1.2 y 1.3)
# Esto crea una estructura base con valor inicial 0
inventario_base = dict.fromkeys(categorias, 0)
print("Inventario Inicial:", inventario_base)

# 3. Estructura Compleja: Directorio de Productos (Inspirado en Imagen 3.1)
# Aquí usamos un diccionario donde cada valor es una TUPLA (datos complejos)
# Formato: 'Producto': (Precio, Stock, Proveedor)
tienda_eco = {
    'Manzana': (1.5, 50, 'BioFarm'),
    'Leche': (2.1, 20, 'EcoLact'),
    'Zanahoria': (0.8, 100, 'HuertoSur')
}

print("\nDetalle de Manzana (Precio, Stock, Proveedor):", tienda_eco['Manzana'])

# 4. Uso de defaultdict para evitar errores (Imagen 1.4)
# Si buscamos un producto que no existe, nos devolverá 0 en lugar de un error
ventas_dia = defaultdict(int)
ventas_dia['Manzana'] += 5  # Registramos una venta

print(f"Ventas de Manzana: {ventas_dia['Manzana']}")
print(f"Ventas de Pera (no existía): {ventas_dia['Pera']}") # Devuelve 0 automáticamente