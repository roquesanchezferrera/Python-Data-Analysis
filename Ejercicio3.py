import numpy as np
import pandas as pd

# --------------------- APARTADO 1 ---------------------------------------------------
# Creamos serieA como una lista de números
serieA = pd.Series([5, 30, 15, 42, 3], index = ["A", "B", "C", "D", "E"])

# Cremoa serieB como un array de números
serieB = pd.Series(np.array([60, 72, 36, 3, 72]), index = ["A", "B", "C", "D", "E"])

# --------------------- APARTADO 2 ---------------------------------------------------
# Realizamos un filtrado para ver cuales son múltiplos de 3
print("Los números múltiples de 3 en la serieA y su correspondiente posición son:") 
print(serieA[serieA % 3 == 0])
print("-------------------------------------------------------------")

# --------------------- APARTADO 3 ---------------------------------------------------
# Creamos un dataframe con ambas series y se le asigna un índice
df3 = pd.DataFrame({"SerieA": serieA,
                   "SerieB": serieB},
                   index = ["A", "B", "C", "D", "E"])

print(df3)
print("-------------------------------------------------------------")

# --------------------- APARTADO 4 y 5------------------------------------------------
# Creamos dos listas vacías para guardar los número que sean comunes o no
lista1 = []
lista2 = []
lista_serieB = list(serieB)

# Realizamos un bucle recorriendo todos los elementos de la serieA
for i in serieA:
    # Si el elemento no está en la serieB y no se ha añadido todavía en la lista2
    if (i not in lista_serieB) and (i not in lista2):
        # Añadimos el elemento
        lista2.append(i)
    # Si el elemento está en la serieB y no se ha añadido todavía en la lista1
    elif (i in lista_serieB) and (i not in lista1):
        # Añadimos el elemento
        lista1.append(i)

# Mostramos los resultados
print("Los elementos comunes en ambas series son: ", end = "")
print(*lista1, sep = ", ")

print("Los elementos de la serieA que no están presentes en la serieB son: ", end = "")
print(*lista2, sep = ", ")
print("-------------------------------------------------------------")

# --------------------- APARTADO 6 ---------------------------------------------------
serieC = pd.Series(np.random.randint(1, 10, 35))

# Realizamos una rebanada para cada columna y además resteamos el índice para empezar por cero
columna1 = serieC[0:7]
columna2 = serieC[7:14].reset_index(drop=True)
columna3 = serieC[14:21].reset_index(drop=True)
columna4 = serieC[21:28].reset_index(drop=True)
columna5 = serieC[28:35].reset_index(drop=True)

# Concatenamos por columnas y mostramos el resultado
df6 = pd.concat([columna1, columna2, columna3, columna4, columna5], axis = 1)

print(df6)
