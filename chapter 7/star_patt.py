no =int(input("enter a no:"))


#     *
#    ***
#   *****

for i in range(1,no+1):
 print(" "* (no-1),end="")
 print("*"* (2*i-1),end="")
 print("")