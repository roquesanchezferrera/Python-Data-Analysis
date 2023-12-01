import numpy as np

# Creamos el array
asignaturas = np.array([[8, 7, 10, 4, 9], [8, 6, 7, 4, 8], [9, 7, 8, 3, 9], [4, 2, 9, 2, 6]])

# Declaramos una variable para contabilizar la cantidad de alumnos suspensos por asignatura
suspensos = 0

# Declaramos una variable para saber en qué asignatura nos encontramos en el bucle anidado
# a la hora de calcular el número total de suspensos por asignatura
asignatura = 0

# Realizamos un bucle anidado para acceder a las filas y columnas
for i in asignaturas:
    for j in i:
        if (j < 5):
            # Si la nota es menor de 5, incrementamos en uno la variable suspensos
            suspensos +=1

    # Dependiendo de la asignatura, lanzamos por pantalla el mensaje correspondiente
    if (asignatura == 0):
        print(f"Latín se ha suspendido por {suspensos} alumnos.")

    if (asignatura == 1):
        print(f"Castellano se ha suspendido por {suspensos} alumnos.")

    if (asignatura == 2):
        print(f"Francés se ha suspendido por {suspensos} alumnos.")

    if (asignatura == 3):
        print(f"Inglés se ha suspendido por {suspensos} alumnos.")

    # Ponemos la variable suspensos a cero e incrementamos la variable asignatura para
    # que la próxima vez que se recorra el bucle se sepa que estamos en otra asignatura
    # y muestre su correspondiente mensaje por pantalla
    suspensos = 0
    asignatura +=1

# Declaramos la variable alumno. Se utiliza solamente para que a la hora de mostrar la media
# por pantalla, se sepa que alumno es.
alumno = 1

# Declaramos una lista para guardar el nombre de los alumnos aprobados
alumnosAprobados = []

# Calculamos la media para cada columna (axis = 0)
mediaAlumnos = np.mean(asignaturas, axis=0)

# Recorremos el array
for i in mediaAlumnos:
    print(f"El alumno{alumno} ha tenido una nota media de {i}")

    if (i >= 5):
        # Si el alumno tiene una nota mayor o igual a 5 ha aprobado el curso y guardamos su
        # nombre en la lista
        alumnosAprobados.append(f"Alumno{alumno}")

    # Siguiente alumno
    alumno +=1

# Mostramos los alumnos aprobados por pantalla
print("Los alumnos que han aprobado el curso son: ", end = "")
print(*alumnosAprobados, sep =", ")

