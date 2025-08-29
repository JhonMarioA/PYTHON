import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Paso 1: Cargar los datos históricos de ventas
# ==============================

# Cada fila representa un año de ventas para los 4 tipos de motocicletas (2013–2022)
ventas = np.array([
    [2013, 172,  89,  18,  28],   # Año, Tipo 1, Tipo 2, Tipo 3, Tipo 4
    [2014, 185, 116,  49,  33],
    [2015, 202, 155,  98,  49],
    [2016, 225, 188,  96,  44],
    [2017, 252, 200, 148,  59],
    [2018, 286, 199, 173,  72],
    [2019, 316, 240, 204,  70],
    [2020, 342, 245, 235,  96],
    [2021, 371, 280, 266, 140],
    [2022, 402, 302, 297, 250],
])

# Separa el vector de años y la matriz de ventas por tipo
años = ventas[:, 0]      # Vector columna con los años (2013 a 2022)
tipos = ventas[:, 1:]    # Matriz de tamaño (10x4) con las ventas por tipo

# ==============================
# Paso 2: Ajuste de mínimos cuadrados para cada tipo
# ==============================

# Construimos la matriz de diseño A para regresión lineal: una columna de unos (intercepto) y otra con los años
A = np.vstack([np.ones_like(años), años]).T  # Shape (10, 2)

coeficientes = []
for i in range(4):
    b = tipos[:, i]  # Vector de ventas del tipo i
    # Resolvemos por mínimos cuadrados: x = (AᵗA)^(-1)Aᵗb
    x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    coeficientes.append(x)

coeficientes = np.array(coeficientes)  # Cada fila contiene [intercepto, pendiente] para cada tipo

# ==============================
# Paso 3: Predicción para 2024 y 2025
# ==============================

años_pred = np.array([2024, 2025])  # Años a predecir
A_pred = np.vstack([np.ones_like(años_pred), años_pred]).T  # Matriz de diseño para predicción (2x2)

predicciones = []
for x in coeficientes:
    pred = A_pred @ x  # Ventas predichas = A_pred * coeficientes
    predicciones.append(pred)

predicciones = np.array(predicciones).T  # Shape (2, 4), cada fila es un año, columnas son tipos

# ==============================
# Paso 4: Matriz de componentes por tipo
# ==============================

# Cada fila representa un componente y cada columna cuántas unidades se necesitan por tipo
componentes = np.array([
    [1, 1, 1, 0],  # Componente 1 requerido por tipos 1, 2, 3
    [2, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [3, 2, 0, 0],
    [1, 4, 0, 0],
    [5, 2, 0, 1],
    [1, 1, 2, 0],
    [1, 1, 0, 0],
])

# ==============================
# Paso 5: Calcular cantidad de componentes a ordenar
# ==============================

# Redondeamos las predicciones al número entero más cercano
pred_2024 = np.round(predicciones[0])
pred_2025 = np.round(predicciones[1])

# Multiplicamos la matriz de componentes por la cantidad de motos de cada tipo
stock_2024 = componentes @ pred_2024  # Componentes necesarios para 2024
stock_2025 = componentes @ pred_2025  # Componentes necesarios para 2025

# Imprimimos los resultados
print("Predicción de ventas para 2024:", pred_2024)
print("Predicción de ventas para 2025:", pred_2025)
print("\nComponentes necesarios en 2024:\n", stock_2024)
print("\nComponentes necesarios en 2025:\n", stock_2025)

# ==============================
# Paso 6: Visualización de ventas y predicción
# ==============================

for i in range(4):
    # Gráfica de datos reales
    plt.plot(años, tipos[:, i], 'o-', label=f"Tipo {i+1} - Real")
    # Gráfica de predicciones
    plt.plot(años_pred, A_pred @ coeficientes[i], 's--', label=f"Tipo {i+1} - Pred")

# Configuración del gráfico
plt.xlabel("Año")
plt.ylabel("Ventas")
plt.title("Ventas históricas y predicción por mínimos cuadrados")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
