program LorentzAttractorData
    implicit none
    common/ constants/ a,b,c
    real(kind=8)::x0,y0,z0,a,b,c,dt,final_time,t
    integer:: steps, i, j, method
    real(kind=4) elapsed_time, dtime, et(2) 

    real(kind=8), allocatable, dimension(:,:):: positions

    !Initial conditions
    write(*,*) "Enter the initial conditions for X,Y,Z:"
    read(*,*) x0,y0,z0

    !Parameters
    !a->sigma, b->rho, c->Beta
    write(*,*) "Enter the parameter values of a,b,c:"
    read(*,*) a,b,c

    !Time variables
    !t: t variable that goes from 0 to a final time
    !dt: time interval
    !final_time: The last time value that will be evaluated
    t = 0
    write(*,*) "Enter the time interval to use and the final time:"
    read(*,*) dt, final_time

    steps  = int(final_time/dt)+1

    !Allocating the array positions and saving the initial conditions
    allocate(positions(steps, 3))

    positions(1, 1)=x0
    positions(1, 2)=y0
    positions(1, 3)=z0

    !User decides which numerical method will be used
    write(*,*) "Choose which method will be used to solve the Lorenz Equations"
    write(*,*) "1) Euler Method"
    write(*,*) "2) Runge-Kutta 4"
    read(*,*) method

    select case(method)
        case(1) 
            elapsed_time = dtime(et)
            call EulerMethod(dt, steps, positions)
            elapsed_time = dtime(et)
            write(*,*) "Euler Method execution time of ",final_time,"with dt=",dt,"is"
            write(*,*) elapsed_time

        case(2)
            elapsed_time = dtime(et)
            call RG4(dt, steps, positions)
            write(*,*) "Runge-Kutta 4 execution time of ",final_time,"with dt=",dt,"is"
            write(*,*) elapsed_time

        case default
            write(*,*) "Entrada invalida"
    end select

    !The results from the used method and the input constants are saved in two
    !different .dat files
    open(unit=01, file="Lorenz_Path.dat")
    do i=1,steps
        write(01,*) t, (positions(i,j), j=1,3)
        t = t+dt
    end do
    close(01)

    open(unit=02, file="Lorenz_Constants.dat")
    write(02,*) x0, y0, z0, a, b, c

    write(*,*) "The results and constant values have been saved!"
    
end program LorentzAttractorData


!----- System of Differential Equations of the Lorenz Attractor
function dXdt(x,y)
    implicit none
    common/ constants/ a,b,c
    real(kind=8)::x, y, a, b, c, dXdt
    
    dXdt = a*(y-x)

    return
end function dXdt

function dYdt(x,y,z)
    implicit none
    common/ constants/ a,b,c
    real(kind=8)::x, y, z, a, b, c, dYdt
    
    dYdt = (b-z)*x-y
    
    return
end function dYdt

function dZdt(x,y,z)
    implicit none
    common/ constants/ a,b,c
    real(kind=8)::x, y, z, a, b, c, dZdt
    
    dZdt = x*y-c*z
    
    return
end function dZdt

!------ Subroutines for Euler Method and Runge-Kutta 4 Method
subroutine EulerMethod(dt, steps, array)
    implicit none
    real(kind=8), dimension(steps,3)::array
    integer::i, steps
    real(kind=8):: dt, dXdt, dYdt, dZdt

    do i=2,steps
        array(i, 1)= dXdt(array(i-1,1),array(i-1,2))*dt+array(i-1,1)
        array(i, 2)= dYdt(array(i-1,1),array(i-1,2), array(i-1,3))*dt+array(i-1,2)
        array(i, 3)= dZdt(array(i-1,1),array(i-1,2), array(i-1,3))*dt+array(i-1,3)
    end do
end subroutine EulerMethod

subroutine RG4(dt, steps, array)
    implicit none
    real(kind=8), dimension(steps,3)::array
    integer::i, steps
    real(kind=8):: dt, dXdt, dYdt, dZdt
    real(kind=8)::k1,k2,k3,k4, m1,m2,m3,m4, l1,l2,l3,l4

    do i=2,steps
        k1 = dt*dXdt( array(i-1,1), array(i-1,2) )
        m1 = dt*dYdt( array(i-1,1), array(i-1,2), array(i-1,3) )
        l1 = dt*dZdt( array(i-1,1), array(i-1,2), array(i-1,3) )

        k2 = dt*dXdt( array(i-1,1)+ k1/2.0, array(i-1,2)+ m1/2.0 )
        m2 = dt*dYdt( array(i-1,1)+ k1/2.0, array(i-1,2)+ m1/2.0, array(i-1,3)+ l1/2.0 )
        l2 = dt*dZdt( array(i-1,1)+ k1/2.0, array(i-1,2)+ m1/2.0, array(i-1,3)+ l1/2.0 )

        k3 = dt*dXdt( array(i-1,1)+ k2/2.0, array(i-1,2)+ m2/2.0 )
        m3 = dt*dYdt( array(i-1,1)+ k2/2.0, array(i-1,2)+ m2/2.0, array(i-1,3)+ l2/2.0 )
        l3 = dt*dZdt( array(i-1,1)+ k2/2.0, array(i-1,2)+ m2/2.0, array(i-1,3)+ l2/2.0 )

        k4 = dt*dXdt( array(i-1,1)+ k3, array(i-1,2)+ m3 )
        m4 = dt*dYdt( array(i-1,1)+ k3, array(i-1,2)+ m3, array(i-1,3)+ l3 )
        l4 = dt*dZdt( array(i-1,1)+ k3, array(i-1,2)+ m3, array(i-1,3)+ l3 )

        array(i,1) = array(i-1,1) + (k1+k2+k3+k4)/6.0
        array(i,2) = array(i-1,2) + (m1+m2+m3+m4)/6.0
        array(i,3) = array(i-1,3) + (l1+l2+l3+l4)/6.0

    end do
end subroutine RG4
