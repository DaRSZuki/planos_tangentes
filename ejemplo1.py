import numpy as np
import matplotlib.pyplot as plt

# Definir la cuadrícula de valores para X e Y
x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x, y)

# Superficie original: z = x^2 + y^2
Z_superficie = X**2 + Y**2

# Plano tangente en (1,2): z = 2x + 4y - 5
Z_plano = 2*X + 4*Y - 5

# Configurar la figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie (paraboloide)
ax.plot_surface(X, Y, Z_superficie, alpha=0.6, cmap='viridis', edgecolor='none')

# Graficar el plano tangente
ax.plot_surface(X, Y, Z_plano, alpha=0.5, color='orange')

# Marcar el punto de tangencia (1, 2, 5)
ax.scatter([1], [2], [5], color='red', s=50, label='Punto de tangencia (1, 2, 5)')

# Configuraciones de la gráfica
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Superficie $f(x,y) = x^2 + y^2$ y su plano tangente')
ax.set_zlim(0, 20)
ax.legend()

plt.show()