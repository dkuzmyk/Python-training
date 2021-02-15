# sets
myset = {1, 2, 3, 4, 5}
print(myset)

myset2 = set("Hello")
print(myset2)

myset3 = set()
myset3.add(1)
myset3.add(2)
myset3.add(3)
print(myset3)

myset3.remove(2)
print(myset3)

print(myset3.pop())
print(myset3)

odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(even)
print(u)

i = odds.intersection(primes)
print(i)

d = odds.difference(primes)
print(d)



