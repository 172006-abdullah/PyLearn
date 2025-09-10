no = int(input("enter an number:"))

for i in range(2,no):
    if(no % i ==0):
        print("no is not prime")
        break
    else:
        print(" no is prime")
        break