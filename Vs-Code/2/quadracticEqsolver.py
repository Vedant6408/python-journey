#WAP to solve quadractic equation
#user will get the real root solution 
print("-----------------------------------")
print("   Quadractic Equation Solver      ")
print("-----------------------------------")
try:
    xsq = float(input("Type x² Coefficient::  "))
    x = float(input("Type x Coefficient::  "))
    c = float(input("Type Constant Coefficient:: "))
    if xsq != 0:
        d = x**2-4*xsq*c
        if d > 0:
            root1 = round((- x + (d)**0.5)/(2*xsq),2)
            root2 = round((- x - (d)**0.5)/(2*xsq),2)
            print(f"There are two real roots:: {root1,root2}")
        elif d < 0:
            imgroot1 = (- x + complex(d)**0.5)/(2*xsq)
            imgroot2 = (- x - complex(d)**0.5)/(2*xsq)
            im1 = round(imgroot1.imag,2) 
            im2 = round(imgroot2.imag,2)
            print(complex(im1,im2))
        elif d == 0:    
            sameroots = round((- x + (d)**0.5)/(2*xsq),2)
            print(f"The repeated roots are:: \n {sameroots,sameroots}")
        else:
            print("invalid !!")
    else:
        print("Coefficent of x² can't be zero")
except ValueError:
    print("Please enter valid numeric coefficient")
