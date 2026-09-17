import numpy as np
import matplotlib.pyplot as plt

# Definir la cuadrícula de valores para X e Y alrededor del punto (1,1)
x = np.linspace(-2, 4, 40)
y = np.linspace(-2, 4, 40)
X, Y = np.meshgrid(x, y)

# Función original: z = x^2 + xy + y^2
Z_superficie = X**2 + X*Y + Y**2

# Ecuación del plano tangente evaluado: z = 3x + 3y - 3
Z_plano = 3*X + 3*Y - 3

# Configurar la figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z_superficie, alpha=0.7, cmap='plasma', edgecolor='none')

# Graficar el plano tangente
ax.plot_surface(X, Y, Z_plano, alpha=0.5, color='cyan')

# Marcar el punto de tangencia (1, 1, 3)
ax.scatter([1], [1], [3], color='red', s=60, label='Punto de tangencia (1, 1, 3)')

# Configuraciones de la gráfica
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Superficie $f(x,y) = x^2 + xy + y^2$ y su plano tangente')
ax.legend()

plt.show()