# swap 2 no withput 3rd variables 

a=90
b=60
a,b = b,a
print("a=",a,"b=",b)


# find ascii value of a character
ch=input("enter a character :")
print("ascii value of a char",ch,"is",ord(ch))


# convert celcius to farhenite 

n=int(input ("enter temp in celcius: "))
far=(n* 9/5) + 32
print(far)


# reversing a string 

s=input("enter a string to be reversed: ")

rev=""
for i in s:
    rev=i +rev

print(rev)