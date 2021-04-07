program LorentzAttractorData
    implicit none
    real(kind=8)::x0,y0,z0,a,b,c,dt,final_time,t
    integer:: steps, i, j

    real(kind=8), allocatable, dimension(:,:):: positions

    !Initial conditions
    x0 = 0.01
    y0 = 0.0
    z0 = 0.0

    !Parameters
    !a->sigma, b->rho, c->Beta
    a = 10.0
    b = 28.0
    c = 8.0/3.0

    !Time variables
    !t: t variable that goes from 0 to a final time
    !dt: time interval
    !final_time: 
    t = 0
    dt = 1e-2
    final_time = 40.0

    steps  = int(final_time/dt)+1

    allocate(positions(steps, 3))

    positions(1, 1)=x0
    positions(1, 2)=y0
    positions(1, 3)=z0

    do i=2,steps
        positions(i, 1)=a*(positions(i-1,2)-positions(i-1,1))*dt+positions(i-1,1)
        positions(i, 2)=((b-positions(i-1,3))*positions(i-1,1)-positions(i-1,2))*dt+positions(i-1,2)
        positions(i, 3)=(positions(i-1,1)*positions(i-1,2)-c*positions(i-1,3))*dt+positions(i-1,3)
    end do

    call system("del Lorenz_Results.txt")

    open(unit=01, file="Lorenz_Results.txt", status='New')
    write(01,*) x0,y0,z0,a,b,c
    do i=1,steps
        write(01,*) t, (positions(i,j), j=1,3)
        t = t+dt
    end do
    close(01)

    call system("python LorentzAttractorSimulator.py")
    
end program LorentzAttractorData

