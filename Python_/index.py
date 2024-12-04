import numpy as np
import matplotlib.pyplot as plt  # Asegúrate de importar esta biblioteca

# Parámetros del experimento
r_values = [2.5, 3.0, 3.5, 3.8, 4.0]
initial_conditions = [0.1, 0.10001]
iterations = 100

# Función para calcular el mapa logístico
def logistic_map(r, x):
    return r * x * (1 - x)

# Simulación y visualización
for r in r_values:
    x_values = []
    x_values_prime = []
    
    # Condiciones iniciales
    x = initial_conditions[0]
    x_prime = initial_conditions[1]
    
    for _ in range(iterations):
        x = logistic_map(r, x)
        x_prime = logistic_map(r, x_prime)
        x_values.append(x)
        x_values_prime.append(x_prime)
    
    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, label='Condición Inicial: 0.1', color='blue')
    plt.plot(x_values_prime, label='Condición Inicial: 0.10001', color='red', linestyle='dashed')
    plt.title(f'Mapa Logístico con r={r}')
    plt.xlabel('Iteraciones')
    plt.ylabel('Valor de Población')
    plt.legend()
    plt.grid()
    plt.show()