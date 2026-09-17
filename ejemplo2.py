import numpy as np
import matplotlib.pyplot as plt

# Definir la cuadrícula de valores para X e Y
# Restringimos un poco el área alrededor del punto (1,3) para apreciar el plano
x = np.linspace(-1, 3, 40)
y = np.linspace(1, 5, 40)
X, Y = np.meshgrid(x, y)

# Inicializar matriz para la superficie
Z_superficie = np.zeros_like(X)

# Máscara para evitar valores negativos en la raíz cuadrada (x + y >= 0)
mask = (X + Y) >= 0

# Evaluar la función solo donde x+y es positivo o cero
Z_superficie[mask] = (X[mask]**2) * Y[mask] + np.sqrt(X[mask] + Y[mask])
Z_superficie[~mask] = np.nan # Los valores inválidos no se graficarán

# Plano tangente en (1,3,5): z = (25/4)x + (5/4)y - 5
Z_plano = (25.0/4.0)*X + (5.0/4.0)*Y - 5

# Configurar la figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z_superficie, alpha=0.6, cmap='viridis', edgecolor='none')

# Graficar el plano tangente
ax.plot_surface(X, Y, Z_plano, alpha=0.5, color='orange')

# Marcar el punto de tangencia (1, 3, 5)
ax.scatter([1], [3], [5], color='red', s=60, label='Punto de tangencia (1, 3, 5)')

# Configuraciones de la gráfica
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Superficie $f(x,y) = x^2y + \sqrt{x+y}$ y su plano tangente')
ax.legend()

plt.show()