# Lorenz Attractor Solver
There's available a Python script with the numerical routines to be executed with Cython to obtain greate computation velocity and a Jupyter notebook that has the same code structure as the previous Python script. Both formats solve the following coupled differential equations, which are called Lorenz Attractor, through the Runge-Kutta of 4th order:

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" title="\large \frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta z" /></a>

The user is capable to give as input exact initial conditons and the values of the parameters shown in the equations; both of these numerical sets are used to solve the system.
