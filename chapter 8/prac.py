
#problem 1


def greatest(a,b,c):
    if(a>b and a >c ):
        return a
    elif(b>a and b> c):
        return b
    elif(c>a and c>b):
        return c
    
x=98
y=94
z=56

print(greatest(x,y,z))
