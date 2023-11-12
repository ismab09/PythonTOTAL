set = set([1,2,3,4,5])
print(type(set))
print(set)

print("--------------------------------------------")

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

print("--------------------------------------------")

set3 = {1,2,(1,2,3),3,4,5}
print(type(set3))
print(set3)
print(len(set3))
print(2 in (set3))

print("--------------------------------------------")

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
print(len(s3))

print("--------------------------------------------")

m1 = {1,2,3}

m1.add(4)
print(m1)
m1.remove(3)
print(m1)

print("--------------------------------------------")

a1 = {1,2,3}
a1.discard(6)
print(a1)
sorteo = a1.pop()
print(sorteo)

print("--------------------------------------------")

b1 = {1,2,3}
b1.clear()
print(b1)