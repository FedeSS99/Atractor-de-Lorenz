import numpy as np
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.pyplot import figure, Normalize, show

from CalculoAtractorLorenz import RungeKutta4Cy

#Definimos las constantes del sistema
sigma, beta, rho = 10.0, 8.0/3.0, 28.0

#Seguido de proporcionar las condiciones iniciales 
#de cada cantidad
x0, y0, z0 = 10.0, 0.1, 6.0

#Asignamos el tiempo final para realizar los cálculos así como
#el delta de tiempo a utilizar
tf, dt = 60.0, 1e-4

#Calculamos el número de valores que se irán a calcular para dar
#con el arreglo de tiempo a utilizar
n_datos = int(1.0 + tf/dt)
t = np.linspace(0.0, tf, n_datos).astype(np.float64)

#Creamos y fijamos la memoria requerida para almacenar tanto la
#posicion inicial como los cálculos posteriores
x,y,z = np.zeros_like(t),  np.zeros_like(t),  np.zeros_like(t)
x[0], y[0], z[0] = x0,y0,z0

RungeKutta4Cy(x,y,z,dt,sigma,rho,beta)

#Iniciamos un par de figuras: En la priemra se mostrara la evolucion
#de X(t), Y(t) y Z(t) en un espacio tridimensional
figura3D = figure(1, figsize=(7,6))
sub3D = figura3D.add_subplot(111, projection="3d")
sub3D.set_xlim(x.min(), x.max())
sub3D.set_ylim(y.min(), y.max())
sub3D.set_zlim(z.min(), z.max())
sub3D.set_xlabel("X")
sub3D.set_ylabel("Y")
sub3D.set_zlabel("Z")

normalizacion = Normalize(0, n_datos-1)
ColeccionLineas = Line3DCollection([], cmap="jet", norm=normalizacion)
ColeccionLineas.set_array(np.arange(n_datos))

puntos = np.array([x[:], y[:], z[:]]).T.reshape(-1,1,3)
segmentos = np.hstack([puntos[:-1], puntos[1:]])
ColeccionLineas.set_segments(segmentos)
sub3D.add_collection(ColeccionLineas)
sub3D.grid(False)

#En la segunda se mostrara la evolucion de X,Y,Z a lo largo del tiempo
#por separado
figuras2D = figure(2, figsize=(6,6))
subX, subY, subZ = figuras2D.add_subplot(311),  figuras2D.add_subplot(312),  figuras2D.add_subplot(313)

subX.set_ylabel("X")
subY.set_ylabel("Y")
subZ.set_xlabel("Tiempo")
subZ.set_ylabel("Z")

subX.plot(t,x,"-r")
subY.plot(t,y,"-g")
subZ.plot(t,z,"-b")

figura3D.tight_layout()
figuras2D.tight_layout()

show()