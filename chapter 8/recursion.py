'''
factorial(5)=n 5x4x3x2x1
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n= int(input("enter a number:"))

print(f"the factorial fo no is:{factorial(n)}" )