# strings are immutable 

name="abdullah"
nameshort=len(name)

name1=name[0:3]
# staRT FROM INDEX TILL 3
print(name1)
print(nameshort)
character1=name[5]
print(character1)

#negative slicing 
str1= "commentment"
print(str1[-4:-1])
print(str1[1:6])
print(str1[1:])
print(str1[:6])
# skipping values 



str2="0123456789"
print(str2[1:7:3])

str3="abcdefghijklmnopk" 
print(str3[1:9:4])
