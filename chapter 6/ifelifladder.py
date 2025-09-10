marks=int(input("enter your marks"))

# if elif ladder 

if(marks<50):
    print("you have failed")

elif(marks<100 and marks>90):
    print("your grade is A+")

elif(marks<90 and marks > 80):
    print("your grade is A")

elif(marks< 80 and marks >70):
    print("your grade is B")

elif(marks<70 and marks>60 ):
    print("your grade is C")

elif(marks< 60 and marks> 50):
    print("your grade is D")
else:
    print("invalid marks")