# Lorenz-Attractor
Python and Fortran scripts that solve and show the Lorenz Attractor.

The Fortran code solves the following system of differential equations by Euler's Method and Runge-Kutta 4:

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;\large&space;\frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta&space;z" title="\large \frac{dx}{dt}=\sigma(y-x)\quad\frac{dy}{dt}=x(\rho-z)-y\quad\frac{dz}{dt}=xy-\beta z" /></a>

where the user can type the values of initial conditions and the already seen parameters by compiling and executing the same file.

The Python code reads the .txt output file that contains the input values of the system along with the time and solutions. An important value is the time interval used in the finite differences given that if it isn´t small enough it won´t have convergent solutions. There are two different programs:

1. LorentzAttractorSimulator_Unique.py: This one only shows a 3D plotting of the solutions obtained and saved in the .txt file.

2. LorentzAttractorSimulator_Multiple.py: This one does the same but also shows the temporal evolution of the coordinates in 2D plots separately.

The following links shows a simulation of the system propose by Lorenz with both programs: 

Unique -> https://youtu.be/Qipy5A2d384  
Multiple -> https://youtu.be/v5C7-NbWaVo
