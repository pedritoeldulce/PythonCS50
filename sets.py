# set: Colección de datos únicos y ordenados. 
# create am empty set

s = set()

# Add elements to set

s.add(12)
s.add(13)
s.add(14)
s.add(15)
s.add(11)

# Added a item to set; won´t add to list as it is a repeating value
s.add(15)
print(s)
# remove; remove a value of the list
s.remove(14)
print(s)

# len(): a function that return a quantity of elements

print(f"cantidad de elementos {len(s)}")