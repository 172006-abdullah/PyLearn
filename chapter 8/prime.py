def prime(start,end):
    p=[]
    for no in range(start,end+1):
        if no <=1:
            print(f"{no} is not prime")
        else:
            for i in range (2,no):
                if no% i==0:
                    break
                else:
                    