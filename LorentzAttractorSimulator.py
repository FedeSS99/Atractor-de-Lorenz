from matplotlib.pyplot import figure, show, get_cmap
from matplotlib.animation import FuncAnimation

from numpy import array, amin, amax

with open("Resultados_Lorentz.txt", 'r') as archivo:
    lineas = archivo.readlines()

    constantes_string = lineas[0].split()
    constantes = [float(elemento) for elemento in constantes_string]

    num_values = lineas[1:]

    t_values = array([float(linea.split()[0]) for linea in num_values])
    x_values = array([float(linea.split()[1]) for linea in num_values])
    y_values = array([float(linea.split()[2]) for linea in num_values])
    z_values = array([float(linea.split()[3]) for linea in num_values])

xmin, xmax = amin(x_values), amax(x_values)
ymin, ymax = amin(y_values), amax(y_values)
zmin, zmax = amin(z_values), amax(z_values)

main_figure = figure(figsize=(6,6))
subfigure_main = main_figure.add_subplot(111, projection='3d')
main_figure.suptitle(r"$x_0$={0:.2f} $y_0$={1:.2f} $z_0$={2:.2f}".format(*constantes[:3])+"\n"+
                    r"$\sigma$={0:.2f} $\rho$={1:.2f} $\beta$={2:.2f}".format(*constantes[3:]))

subfigure_main.set_xlabel("X(t)")
subfigure_main.set_ylabel("Y(t)")
subfigure_main.set_zlabel("Z(t)")
subfigure_main.grid(False)

subfigure_main.plot(x_values, y_values, z_values, '-b', linewidth=0.75)

"""
title = subfigure_main.text2D(0.5, 0.95, " ", transform=subfigure_main.transAxes, ha="center")

subfigure_main.set_xlim(xmin, xmax)
subfigure_main.set_ylim(ymin, ymax)
subfigure_main.set_zlim(zmin, zmax)

path_plot = subfigure_main.plot(x_values[0], y_values[0], z_values[0], '-b', linewidth=0.75)
path = path_plot[0]

def update_path(i):
    path.set_data(x_values[:i],y_values[:i])
    path.set_3d_properties(z_values[:i])

    title.set_text(f't={t_values[i]:.3f}s')

    return [path, title]

path_ani = FuncAnimation(main_figure, update_path, len(x_values), interval=10, blit=True, repeat=False)
"""

show()