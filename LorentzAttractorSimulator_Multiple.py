from matplotlib.pyplot import figure, show
from matplotlib.animation import FuncAnimation

from numpy import array, amin, amax

with open("Lorenz_Results.txt", 'r') as archivo:
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
tmin, tmax = amin(t_values), amax(t_values)

main_figure = figure(figsize=(12,6.5))
main_figure.suptitle(r"$x_0$={0:.2f} $y_0$={1:.2f} $z_0$={2:.2f}".format(*constantes[:3])+"\n"+
                    r"$\sigma$={0:.2f} $\rho$={1:.2f} $\beta$={2:.2f}".format(*constantes[3:]))

subX, subY, subZ = main_figure.add_subplot(231),main_figure.add_subplot(232), main_figure.add_subplot(233)
subMain = main_figure.add_subplot(235, projection='3d')

pathX_plot = subX.plot([], [], '-b', linewidth=0.75)
pathX = pathX_plot[0]
subX.set_xlabel("t")
subX.set_ylabel("X(t)")
subX.set_xlim(tmin, tmax)
subX.set_ylim(xmin, xmax)

pathY_plot = subY.plot([], [], '-g', linewidth=0.75)
pathY = pathY_plot[0]
subY.set_xlabel("t")
subY.set_ylabel("Y(t)")
subY.set_xlim(tmin, tmax)
subY.set_ylim(ymin, ymax)

pathZ_plot = subZ.plot([], [], '-k', linewidth=0.75)
pathZ = pathZ_plot[0]
subZ.set_xlabel("t")
subZ.set_ylabel("Z(t)")
subZ.set_xlim(tmin, tmax)
subZ.set_ylim(zmin, zmax)

path_plot = subMain.plot([], [], [], '-r', linewidth=0.75)
subMain.view_init(15, -60)
subMain.grid(False)
subMain.set_xlim(xmin, xmax)
subMain.set_ylim(ymin, ymax)
subMain.set_zlim(zmin, zmax)
subMain.set_xlabel("X(t)")
subMain.set_ylabel("Y(t)")
subMain.set_zlabel("Z(t)")
path3D = path_plot[0]

main_figure.tight_layout()

def update_path(i):
    path3D.set_data(x_values[:i],y_values[:i])
    path3D.set_3d_properties(z_values[:i])

    pathX.set_data(t_values[:i], x_values[:i])
    pathY.set_data(t_values[:i], y_values[:i])
    pathZ.set_data(t_values[:i], z_values[:i])

    return [path3D, pathX, pathY, pathZ]

path_ani = FuncAnimation(main_figure, update_path, len(x_values), interval=10, blit=True, repeat=False)

show()