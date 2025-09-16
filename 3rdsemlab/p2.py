# check a no is positive _ve or zero 

a=int(input("enter a number:"))
if (a>0):
    print(a,"is a positive no")
elif(a<0):
    print(a,"is a negative number")
elif(a==0):
    print(a,"a is zero")
else:
    print(a,"invalid number")


x=int(input("enter a number:"))
y=int(input("enter a number:"))
z=int(input("enter a number:"))
if(x>y and x>z):
    print(x,"is largest of all ")
elif(y>x and y>z):
    print(y,"is largest of all ")
elif(z>x and z>y):
    print(z,"is largest of all ")
else:
    print("invalid no ")


a=(input("enter a character to check: "))
if a in "aeiou":
    print("character is vowel")
else:
    print("character is consonant")