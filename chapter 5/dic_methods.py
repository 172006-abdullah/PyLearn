dic={"reacher":111,
"neagley":110,
"jack":1011,
1109:"seargent"
}

print(dic.items())# it make output like tupple
print(dic.keys())# it gives us left side values
print(dic.values())# it gives us right side values 
dic.update({"reacher":11})# by this we can update any valkue of dict
print(dic)

print(dic.get("reacher2"))
#print(dic["reacher2"]) it will give error
print(dic["reacher"])

# we can find length of sets and dic by len function