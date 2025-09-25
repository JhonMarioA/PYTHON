# ==========================================
# Librerías
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración opcional para que los gráficos se vean mejor
sns.set(style="whitegrid")  # estilo de seaborn
plt.rcParams["figure.figsize"] = (10, 6)  # tamaño por defecto de las gráficas


# ==========================================
# Entendiendo el dataset
# ==========================================
# 1.1 Cargando y mostrando información general del dataset:


# Cargando datos
ruta = "data/train.csv"
df = pd.read_csv(ruta)


# Información general
print(df.head())
print(df.info(), "\n")
print("Shape", df.shape, "\n") #Existen 891 pasajeros (filas) y existen 12 variables (columnas), float64(2) - int64(5) - object(5)


# 1.2 Estadísticas descriptivas:

# Resumen estadistico de variables númericas
print(df[["Age", "Fare"]].describe())

print(df["Survived"].value_counts())


# Preguntas:

print("\nEdad promedio: ", df["Age"].mean())
print("Tarifa más cara: ", df["Fare"].max())
print("Edad mediana: ", df["Age"].median())

rango_fare = df["Fare"].max() - df["Fare"].min()
print("Rango de tarifas: ", rango_fare)

print("Desveciación estandar de edad: ", df["Age"].std())
print("Desviación estandar de precios de boletos: ", df["Fare"].std())

print("Edad mínima: ", df["Age"].min())
print("Edad máxima: ", df["Age"].max())

print("\n", df["Sex"].value_counts())
print("\n", df["Embarked"].value_counts())


