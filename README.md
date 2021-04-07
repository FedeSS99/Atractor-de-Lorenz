# Lorenz-Attractor
Python and Fortran scripts that solve and show the Lorenz Attractor.

The Fortran code solves the following system of differential equations by finite differences

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" title="\large \frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta z" /></a>

where the user can change the values of initial conditions and the already seen parameters in the same file. In this same code the Python file is executed at the end of the calculations (Some minor changes must be done if the OS system is Linux).

The Python code reads the .txt output file that contains the input values of the system along with the time and solutions. An important value is the time interval used
in the finite differences given that if it isn´t small enough it won´t have convergent solutions.

The following is an example of the visual output 
