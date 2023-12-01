import numpy as np

# -------------------------------- APARTADO 1 ----------------------------------------------------------
# Declaramos el array de 4 dimensiones
array = np.array ([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
#print(array)
#print(array.ndim)

# Realizamos la suma en función de los dos últimos ejes
suma = np.sum(array, axis = (-2, -1))
print("La suma del array de 4 dimensiones en función de sus dos últimos ejes es:")
print(suma)

# -------------------------------- APARTADO 2 ----------------------------------------------------------

def crear_vectores():
    ''' Función que se encarga de generar un número aleatorio de vectores. Devuelve una 
        lista con todos los vectores creados'''
    # Declaramos nvectores como el número de vectores aleatorios. Mínimo se debe de 
    # tener 2 vectores para calcular el producto cartesiano y como máximo he establecido 
    # 5 para no tener demasiados vectores
    nvectores = np.random.randint(2, 5)
    
    # Declaramos lista para guardar todos los vectores creados
    lista = []

    # Realizamos un bucle para crear todos los vectores
    for i in range(0, nvectores):
        # Cada vector será de 1x2 donde los elementos será números aleatorios entre 0 y 10
        vector = np.array([np.random.randint(0, 10), np.random.randint(0, 10)])
        # Guardamos el vector
        lista.append(vector)
    
    # Devolvemos la lista con los vectores
    return lista

# Llamamos a la función crear_vectores()
vectores = crear_vectores()

# Calculamos el producto cartesiano mediante la función np.meshgrid() (La traspuesta y el reshape nos ayuda
# visualizar mejor el resultado)
producto_cartesiano = np.array(np.meshgrid(*vectores)).T.reshape(-1, len(vectores))

# Mostramos por pantalla los vectores creados y el resultado
print("El producto cartesiano de los vectores (", end = "")
print(*vectores, sep = ", ", end = ") es: ")
print()

for i in producto_cartesiano:
    print(i)


