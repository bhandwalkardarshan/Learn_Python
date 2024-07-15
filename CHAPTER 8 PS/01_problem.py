# find greatest from 3 numbers

def greatest(a,b,c):
    if(a>b and a>b):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
c = int(input("enter value of c: "))

print("greatest number is: ",greatest(a,b,c))