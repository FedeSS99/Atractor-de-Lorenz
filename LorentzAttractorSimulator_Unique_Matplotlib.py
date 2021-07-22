from matplotlib.pyplot import figure, show, pause
from matplotlib.animation import FuncAnimation
from numpy import array, amin, amax

#The output files from the Fortran code are read and saved in arrays
with open("Lorenz_Path.dat", 'r') as out_file1:
    lines = out_file1.readlines()

    t_values = array([float(linea.split()[0]) for linea in lines])
    x_values = array([float(linea.split()[1]) for linea in lines])
    y_values = array([float(linea.split()[2]) for linea in lines])
    z_values = array([float(linea.split()[3]) for linea in lines])

with open("Lorenz_Constants.dat", "r") as out_file2:
    line = out_file2.readlines()

    constants = [float(element) for element in line[0].split()]

#The minimum and max values for each coordinate are searched and saved
xmin, xmax = amin(x_values), amax(x_values)
ymin, ymax = amin(y_values), amax(y_values)
zmin, zmax = amin(z_values), amax(z_values)

#The main figure is created with string formats to display relevant data
main_figure = figure(figsize=(6,6))
subfigure_main = main_figure.add_subplot(111, projection='3d')
main_figure.suptitle(r"$x_0$={0:.2f} $y_0$={1:.2f} $z_0$={2:.2f}".format(*constants[:3])+"\n"+
                    r"$\sigma$={0:.2f} $\rho$={1:.2f} $\beta$={2:.2f}".format(*constants[3:]))

subfigure_main.set_xlabel("X(t)")
subfigure_main.set_ylabel("Y(t)")
subfigure_main.set_zlabel("Z(t)")
subfigure_main.grid(False)

title = subfigure_main.text2D(0.5, 0.95, " ", transform=subfigure_main.transAxes, ha="center")

subfigure_main.set_xlim(xmin, xmax)
subfigure_main.set_ylim(ymin, ymax)
subfigure_main.set_zlim(zmin, zmax)

path_plot = subfigure_main.plot(x_values[0], y_values[0], z_values[0], '-b', linewidth=0.75)
path = path_plot[0]

#Block that creates the animation using FuncAnimation from matplotlib.animation
""""
#The input function to update the plot for each step time is the following
def update_path(i):
    path.set_data(x_values[:i],y_values[:i])
    path.set_3d_properties(z_values[:i])

    title.set_text(f't={t_values[i]:.3f}s')

    return [path, title]

#The animation is created and later displayed
path_ani = FuncAnimation(main_figure, update_path, len(x_values), interval=1, blit=True, repeat=False)
"""

show(block=False)
pause(0.01)

background = main_figure.canvas.copy_from_bbox(main_figure.bbox)

subfigure_main.draw_artist(path)
subfigure_main.draw_artist(title)

main_figure.canvas.blit(main_figure.bbox)

for i in range(len(t_values)):
    main_figure.canvas.restore_region(background)

    path.set_data(x_values[:i],y_values[:i])
    path.set_3d_properties(z_values[:i])
    title.set_text(f't={t_values[i]:.3f}s')

    subfigure_main.draw_artist(path)
    subfigure_main.draw_artist(title)

    main_figure.canvas.update()
    main_figure.canvas.flush_events()
