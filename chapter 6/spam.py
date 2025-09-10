s1="make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"

message=input("enter your message: ")

if((s1 in message)or (s2 in message) or (s3 in message)or (s4 in message)):
    print("it is spam")
else:
    print("this message is not spam")