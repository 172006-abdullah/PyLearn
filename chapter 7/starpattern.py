'''no= int(input("enter a number: "))

for i in range(no):
    for j in range(no): # rows
        print("*",end=" ") # columns
    print()
    '''
'''
# right angle triangle 
n=int(input("enter number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()
'''
# decreasing right triangle
'''
n=int(input("enter number:"))
for i in range(n):
    for j in range(i,n):
        print("*",end='')
    print()
'''
#right sided triangle 
'''
n=int(input("enter number:"))
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print("*",end="")
    print()


# right sided decreasing triangle

n=int(input("enter number:"))
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print("*",end="")
    print()
    


# hill pattern 

n=int(input("enter number:"))
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print("*",end="")
    for j in range(i):
        print("*",end='')
    print()

    
# reverse hill pattern

n=int(input("enter number:"))
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end='')
    print()

'''
n = int(input("Enter number: "))

# Top half
for i in range(n):
    # spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Bottom half
for i in range(n - 2, -1, -1):
    # spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()
