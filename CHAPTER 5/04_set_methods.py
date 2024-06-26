# set 

s = set()

s.add(100)
s.add(201)
s.add(31)
s.add(71)
s.add(61)

print(s, type(s))

# length of set
print(len(s))

s.remove(61) # if element is present then removes it

s.discard(2) # if element is not present then does nothing
print(s)

element = s.pop()
print(element)  # Output: 71 (or any other element, as sets are unordered)
print(s)   # Output:  (or whatever elements remain)

s.clear() # deletes all elements
print(s)