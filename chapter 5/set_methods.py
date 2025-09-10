# sets are unordered and unindexed
se={1,3,34,5,"abdullah"}
print(se,type(se))

#add method it insert some element in set 

s={1,2,4,4}
s.add(3)
print(s)

# remove method , it removes an element in set 
set={1,2,3,4,5}
set.remove(5)
print(set)

# discard method, it removes and element and no error if not foumfd
e={1,3,4,5,5,65}
e.discard(77)
print(e)

# the main diff is tat remove give error when element not founf but discard dobt give 

# pop method it removes an element from set 
p={87,45,68}
print(p.pop())
print(p)

# clear method it removes all elements opf a set 

c={1,35,76,4}
c.clear()
print(c)

#union or | it combine two sets 
a={13,65,454}
b={7,6,9,0}
print(a.union(b))
# or 
print(a|b)


# intersection or common or & 

i={1,5,8,90}
k={1,9.4,5}
print(i.intersection(k))
