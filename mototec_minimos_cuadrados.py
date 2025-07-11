import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Paso 1: Datos
# ==============================

ventas = np.array([
    [2013, 172,  89,  18,  28],
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

años = ventas[:, 0]
tipos = ventas[:, 1:]

# ==============================
# Paso 2: Ajuste de mínimos cuadrados
# ==============================

A = np.vstack([np.ones_like(años), años]).T

coeficientes = []
for i in range(4):
    b = tipos[:, i]
    x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    coeficientes.append(x)

coeficientes = np.array(coeficientes)

# ==============================
# Paso 3: Predicción 2024 y 2025
# ==============================

años_pred = np.array([2024, 2025])
A_pred = np.vstack([np.ones_like(años_pred), años_pred]).T

predicciones = []
for x in coeficientes:
    pred = A_pred @ x
    predicciones.append(pred)

predicciones = np.array(predicciones).T

# ==============================
# Paso 4: Matriz de componentes
# ==============================

componentes = np.array([
    [1, 1, 1, 0],
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
# Paso 5: Componentes necesarios
# ==============================

pred_2024 = np.round(predicciones[0])
pred_2025 = np.round(predicciones[1])

stock_2024 = componentes @ pred_2024
stock_2025 = componentes @ pred_2025

print("Predicción de ventas para 2024:", pred_2024)
print("Predicción de ventas para 2025:", pred_2025)
print("\nComponentes necesarios en 2024:\n", stock_2024)
print("\nComponentes necesarios en 2025:\n", stock_2025)

# ==============================
# Paso 6: Gráfica 
# ==============================

for i in range(4):
    plt.plot(años, tipos[:, i], 'o-', label=f"Tipo {i+1} - Real")
    plt.plot(años_pred, A_pred @ coeficientes[i], 's--', label=f"Tipo {i+1} - Pred")

plt.xlabel("Año")
plt.ylabel("Ventas")
plt.title("Ventas históricas y predicción por mínimos cuadrados")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
