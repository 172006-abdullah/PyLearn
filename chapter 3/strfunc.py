
str="abdullah"
print(len(str))
print(str.startswith("ab"))
print(str.endswith("lah"))
print(str.capitalize())




print(str.upper())
print(str.lower())
print(str.replace("abd","ABD"))
print(str.title())
print(str.find("ullah"))

#searching
str1="python programming"
print(str1.find("python"))
print(str1.index("mming"))
print(str1.count("programming"))
print(str1.startswith("programming"))
print(str1.endswith("programming"))


# validation boolean

st="python"
stx="123"
sty="fun00"
print(st.isalpha())
print(stx.isdigit())
print(sty.isalnum())
print("hello".islower())
print("HEELOO".isupper())

#cleaning
text="    error comming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


#splitting and joining

tex="g36,cannon,xmb"
print(tex.split(","))
print(tex.rsplit(",",2))

