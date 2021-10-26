import numpy as np
from matplotlib.pyplot import figure, rcParams
from matplotlib.cm import jet
from matplotlib.animation import FuncAnimation, FFMpegWriter

from CalculoAtractorLorenz import RungeKutta4Cy

class TrayectoriaLorenz():
    def __init__(self,conds_inic, params, tf, dt):
        self.conds_inic = conds_inic
        self.x0, self.y0, self.z0 = self.conds_inic

        self.params = params
        self.sigma, self.beta, self.rho = self.params
        
        self.tf, self.dt = tf, dt
        self.n_datos = int(1.0+self.tf/self.dt)

    def CalculoRG4_Sistema(self):
        self.t = np.linspace(0.0, self.tf, self.n_datos).astype(np.float64)
        self.x, self.y, self.z = np.zeros_like(self.t), np.zeros_like(self.t), np.zeros_like(self.t)
        self.x[0], self.y[0], self.z[0] = self.x0, self.y0, self.z0

        RungeKutta4Cy(self.x,self.y,self.z,
        self.dt,self.sigma,self.beta,self.rho)

        self.xmin, self.xmax = min(self.x), max(self.x)
        self.ymin, self.ymax = min(self.y), max(self.y)
        self.zmin, self.zmax = min(self.z), max(self.z)    


#Definimos el numero de condiciones iniciales aleatorias que queramos trabajar
n = 50
#Ademas de los valores sigma->a, beta->b, rho->r así como el tiempo final junto con el delta
#de tiempo a utilizar
a,b,r = 10.0,28.0,8.0/3.0
Tf, Dt = 30.0, 5e-3

trayectorias = []

for i in range(n):
    trayectorias.append(TrayectoriaLorenz(np.random.uniform(-20,20, 3),[a,b,r], Tf, Dt))

print(f"(sigma,beta,rho)=({trayectorias[i].sigma:.3f}, {trayectorias[i].beta:.3f}, {trayectorias[i].rho:.3f})")
for i in range(n):
    print(f"Trayectoria {i+1}: (x0,y0,z0)=({trayectorias[i].x0:.3f}, {trayectorias[i].y0:.3f}, {trayectorias[i].z0:.3f})")
    trayectorias[i].CalculoRG4_Sistema()

minX, maxX = min([trayectoria.xmin for trayectoria in trayectorias]), max([trayectoria.xmax for trayectoria in trayectorias])
minY, maxY = min([trayectoria.ymin for trayectoria in trayectorias]), max([trayectoria.ymax for trayectoria in trayectorias])
minZ, maxZ = min([trayectoria.zmin for trayectoria in trayectorias]), max([trayectoria.zmax for trayectoria in trayectorias])

#Iniciamos un par de figuras: En la primera se mostrara la evolucion
#de X(t), Y(t) y Z(t) en un espacio tridimensional
figura3D = figure(1, figsize=(9,7))
sub3D = figura3D.add_subplot(111, projection="3d")
titulo_texto = r"$\sigma={0:.3f}$, $\beta={1:.3f}$, $\rho={2:.3f}$".format(a,b,r)
titulo = sub3D.set_title("", color="white")
sub3D.set_xlim(minX,maxX)
sub3D.set_ylim(minY,maxY)
sub3D.set_zlim(minZ,maxZ)
sub3D.set_xlabel("X")
sub3D.set_ylabel("Y")
sub3D.set_zlabel("Z")

sub3D.set(facecolor="black")
figura3D.set(facecolor="black")
sub3D.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
sub3D.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
sub3D.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
sub3D.xaxis.label.set_color('white')
sub3D.yaxis.label.set_color('white')
sub3D.zaxis.label.set_color('white')
sub3D.tick_params(axis='x',colors='white')
sub3D.tick_params(axis='y',colors='white')
sub3D.tick_params(axis='z',colors='white')

figura3D.tight_layout()

particulas = []
caminos = []
colors = jet(np.linspace(0,1,n))
for k in range(n):
    caminos.append(sub3D.plot([],[],[], "-", linewidth=0.75)[0])
    particulas.append(sub3D.plot([],[],[], "o", color=caminos[k].get_color(), markersize=3.0)[0])


def plot_inicial():
    for k in range(n):
        particulas[k].set_data_3d(trayectorias[k].x[0], trayectorias[k].y[0], trayectorias[k].z[0])
    titulo.set_text(titulo_texto+f"T={trayectorias[0].t[0]}")
        
    return particulas, titulo,

def avance_particula(i):
    for k in range(n):
        caminos[k].set_data_3d(trayectorias[k].x[:i+1], trayectorias[k].y[:i+1], trayectorias[k].z[:i+1])
        particulas[k].set_data_3d(trayectorias[k].x[i+1], trayectorias[k].y[i+1], trayectorias[k].z[i+1])
    titulo.set_text(titulo_texto+f"T={trayectorias[0].t[i+1]}")
        
    return particulas, caminos, titulo,

animacionGIF = FuncAnimation(figura3D, avance_particula, trayectorias[0].n_datos-1, plot_inicial, repeat=True, blit=False)

print("Iniciando creacion de gif...")
rcParams['animation.convert_path'] = r'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\convert.exe'
animacionGIF.save("AtractorLorenz.gif", writer="imagemagick", fps=360)
print("Gif terminado\n")

animacionMP4 = FuncAnimation(figura3D, avance_particula, trayectorias[0].n_datos-1, plot_inicial, repeat=False, blit=False)

print("Iniciando creacion de video mp4...")
rcParams['animation.ffmpeg_path'] = r'C:\FFmpeg\bin\ffmpeg'
writer = FFMpegWriter(fps=120, extra_args=['-vcodec', 'libx264'], bitrate=-1)
animacionMP4.save("AtractorLorenz.mp4", writer=writer)
print("Video terminado")





