# Quadratic Formula Time
# So fun
import math
def quad():
    print("Lets do the Quadratic formula")
    print("Please put the values for A, B, and C")

    a=int(input("A-Value: "))
    b=int(input("B-Value: "))
    c=int(input("C-Value: "))

    d = b*b-4*a*c

    if d > 0:
        plus=float(((-b)+math.sqrt(b**2-a*c*4))/(a*2))
        minus=float(((-b)-math.sqrt(b**2-a*c*4))/(a*2))

        print("Your answers are",plus,"and",minus,)
    elif d == 0:
        root = -b / (2*a)
        print("Double root at",root)
    else:
        print("no roots here")
                
quad()
          
