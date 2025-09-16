list=[]

while True:
 x=input("enter numbers in list :")
 if (x.lower()=="no"):
   break
 list.append(int(x))
for i in list:
    if (i % 2!=0):
       print("not all numbers are even ")
       break
else:
      print("all no are even")


'''

student={"abdullah":78,
         "zoro":86,
         "zi zu":90,
         "shahzy":100,
         "jedii":67
}

for i in student:
  print(i)

name=input("enter name of student : ")
if name in student:
  print(f"{name}marks are {student[name]}")
else:
  print("not found")

'''