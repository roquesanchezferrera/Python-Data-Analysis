import pandas as pd
import matplotlib.pyplot as plt

covid1 = pd.read_csv("Python_AnalisisDeDatos_TF2\COVID_01-01-2021.csv")
covid2 = pd.read_csv("Python_AnalisisDeDatos_TF2\COVID_01-02-2021.csv")
covid3 = pd.read_csv("Python_AnalisisDeDatos_TF2\COVID_01-03-2021.csv")

# --------------------------------------- APARTADO 1 --------------------------------------------------------------- TERMINADO
print("------------------------------------------ APARTADO 1 -----------------------------------------------------")

# Mostramos las 5 primeras filas del dataframe
print("Primeras 5 líneas del dataframe:")
print(covid1.head())
print()

# Para cada columna mostramos la cantidad de valores nulos que hay
print("Información sobre la cantidad de valores nulos por cada columna:")
print(covid1.isnull().sum())
print()

# Para eliminar las columnas innecesarias utilizamos la función drop()
covid1 = covid1.drop(["FIPS", "Admin2", "Lat", "Long_", "Incident_Rate", "Combined_Key", "Case_Fatality_Ratio"], axis = "columns")
covid2 = covid2.drop(["FIPS", "Admin2", "Lat", "Long_", "Incident_Rate", "Combined_Key", "Case_Fatality_Ratio"], axis = "columns")
covid3 = covid3.drop(["FIPS", "Admin2", "Lat", "Long_", "Incident_Rate", "Combined_Key", "Case_Fatality_Ratio"], axis = "columns")

# Para rellenar los datos que faltan se utiliza la función fillna()
covid1["Active"] = covid1["Active"].fillna("No existen datos")
covid2["Active"] = covid2["Active"].fillna("No existen datos")
covid3["Active"] = covid3["Active"].fillna("No existen datos")


# --------------------------------------- APARTADO 2 ---------------------------------------------------------------
print("------------------------------------------ APARTADO 2 -----------------------------------------------------")

# Pasamos la columna Las_Update a datetime64 para asegurarnos de que sea un tiempo
covid1["Last_Update"] = covid1["Last_Update"].astype("datetime64[ns]")

# Ordenamos por pais y por cada pais ordenamos por tiempo. El último tiempo será el más grande y por tanto la última actualización
datos_ordenados = covid1.sort_values(by = ["Country_Region", "Last_Update"])

# Agrupamos por pais y cogemos la última actualización mediante last()
ultimos_casos = datos_ordenados.groupby("Country_Region").last().reset_index()

# Mostramos los datos deseados
print("Último número de casos confirmados, fallecidos, recuperados y activos según el país:")
print(ultimos_casos[["Country_Region", "Confirmed", "Deaths", "Recovered", "Active"]])
print()


# --------------------------------------- APARTADO 3 --------------------------------------------------------------- TERMINADO
print("------------------------------------------ APARTADO 3 -----------------------------------------------------")

# Eliminamos las filas que no poseen datos. En este caso las de Province_State que es la única columna
# donde tenemos valores nulos
covid1_mod = covid1.dropna()

# Agrupamos por provincia y sumamos los pacientes recuperados
provincias_agrupadas = covid1_mod.groupby("Province_State")["Recovered"].sum()

# Filtramos para aquellos conseguir aquellas provincias que no tenga pacientes recuperados
no_recuperados = provincias_agrupadas[provincias_agrupadas == 0]

# Pasamos a una lista para poder mostrarlo por pantalla. Se podría haber representado directamente con la línea siguiente:
# print(no_recuperados)
lista_no_recuperados = list(no_recuperados.index)

print("Las provincias que no tienen ningún caso de paciente recuperado son:", end = " ")
print(*lista_no_recuperados, sep = ", ")
print()



# --------------------------------------- APARTADO 4 --------------------------------------------------------------- TERMINADO
print("------------------------------------------ APARTADO 4 -----------------------------------------------------")

# Agrupamos por país y para cada uno sumamos los casoa confirmados, fallecidos y recuperados
max_confirmados = covid1.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum()

# Ordenamos por casos confirmados en orden descendente, es decir, el primer valor será el más alto
max_confirmados = max_confirmados.sort_values(by = "Confirmed", ascending=False)

# Puesto que los 10 primeros valores son los más grandes, basta con mostrarlos
print("Los 10 países con más casos confirmados, sus números de fallecidos y recuperados son:")
print(max_confirmados.head(10))
print()



# --------------------------------------- APARTADO 5 --------------------------------------------------------------- 

# Agrupamos por país y para cada uno sumamos el total de confirmados, fallecidos y recuperados mediante sum()
total_paises = covid1.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum()

# Filtramos para aquellos paises con más de 150 fallecidos
paises_comparar = total_paises[total_paises["Deaths"] > 150]

# Realizamos el gráfico de líneas
plt.plot(paises_comparar.index, paises_comparar["Confirmed"], label = "Confirmados", marker = "o")
plt.plot(paises_comparar.index, paises_comparar["Deaths"], label = "Fallecidos", marker = "o")
plt.plot(paises_comparar.index, paises_comparar["Recovered"],label = "Recuperados", marker = "o")

plt.title('Comparación de Casos Confirmados, Fallecidos y Recuperados')
plt.xlabel('País')
plt.xticks(rotation = 90, ha = "right", fontsize = 5)
plt.ylabel('Número de Casos')
plt.legend()

# Mostramos el gráfico
plt.show()



# --------------------------------------- APARTADO 6 --------------------------------------------------------------- 

# Creamos un dataframe con los casos confirmados totales en cada mes y le asignamos un índice
total_trim = pd.DataFrame({"Casos Confirmados": [covid1["Confirmed"].sum(), covid2["Confirmed"].sum(), covid3["Confirmed"].sum()]},
                           index = ["Enero", "Febrero", "Marzo"])

# Realizamos un gráficos de barras para realziar la comparación
total_trim.plot.bar(color="red")
plt.xticks(rotation = 0, ha = "right", fontsize = 7)

# Asignamos un título
plt.title("Casos Confirmados en el Mundo durante el Primer Trimestre")

# Mostramos el resultado
plt.show()



# --------------------------------------- APARTADO 7 --------------------------------------------------------------- 

# Filtramos por país
provincias_ene = covid1[covid1["Country_Region"] == "Spain"]
provincias_feb = covid2[covid2["Country_Region"] == "Spain"]
provincias_mar = covid3[covid3["Country_Region"] == "Spain"]

# Creamos un dataframe con los datos necesarios
total_trim2 = pd.DataFrame({"Casos Confirmados": [provincias_ene["Confirmed"].sum(), provincias_feb["Confirmed"].sum(), provincias_mar["Confirmed"].sum()],
                            "Casos Recuperados": [provincias_ene["Recovered"].sum(), provincias_feb["Recovered"].sum(), provincias_mar["Recovered"].sum()]},
                            index = ["Enero", "Febrero", "Marzo"])

# Creamos un gráfico de líneas
total_trim2.plot(kind="line")

plt.xlabel("Mes")
plt.ylabel("Número de Casos")
plt.legend()

# Asignamos un título
plt.title("Evolución de Confirmados y Recuperados en España en el Primer Trimestre")

# Mostramos el gráfico
plt.show()

# Para realizarlo por provincias, previamente estableceremos como índice la provincia
provincias_ene.set_index("Province_State", inplace=True)
provincias_mar.set_index("Province_State", inplace=True)
provincias_feb.set_index("Province_State", inplace=True)

# Realizamos un bbuce accediendo a los datos de cada provincia
for i in provincias_ene.index:

    # Cremos un dataframe donde por cada provincia sacaremos los datos de confirmados y recuperados por mes
    provincia_trim = pd.DataFrame({"Casos Confirmados": [provincias_ene.loc[i, "Confirmed"], provincias_feb.loc[i, "Confirmed"], provincias_mar.loc[i, "Confirmed"]],
                                   "Casos Recuperados": [provincias_ene.loc[i, "Recovered"], provincias_feb.loc[i, "Recovered"], provincias_mar.loc[i, "Recovered"]]},
                                   index = ["Enero", "Febrero", "Marzo"])
    
    # Creamos un gráfico de líneas
    provincia_trim.plot(kind="line")

    plt.xlabel("Mes")
    plt.ylabel("Número de Casos")
    plt.legend()

    # Asignamos un título
    plt.title(f"Evolución de Confirmados y Recuperados en {i} en el Primer Trimestre")

    # Mostramos el gráfico
    plt.show()

