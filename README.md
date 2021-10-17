# Solucionador del Atractor de Lorenz
Scripts de Python y Fortran que resuelven y muestran el Atracto de Lorenz.

Se cuenta con un script de Python en conjunto con un rutinas escritas para ser compiladas
con el paquete Cython con el fin de acelerar los tiempos de ejecución del método númerico.

Además se tiene también un notebook el cual resuelve bajo la misma estructura del código
anterior; ambos formatos solucionan el siguiente sistema de ecuaciones diferenciales acopladas, llamadas también Atractor de Lorenz, bajo el método de Runge-Kutta de orden 4:

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" title="\large \frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta z" /></a>

El usuario es capaz de asignar los valores deseados de condiciones iniciales así como de los parámetros visibles en las ecuaciones; siendo estos usados para determinar las soluciones númericas.

Los siguientes videos presentan simulaciones de los resultados estáticos a obtenerse con los scripts y notebook: 

* Primera Version
  * Unique -> https://youtu.be/Qipy5A2d384
  * Multiple -> https://youtu.be/v5C7-NbWaVo

* Segunda Version
  * Multiple -> https://youtu.be/tmA8tr8Vq5s
