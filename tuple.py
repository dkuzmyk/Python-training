# tuples // immutable
mytuple = ("Max", 28, "Boston")
print(mytuple)

item = mytuple[0]
print(item)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("Yes")
else:
    print("No")

mytuple2 = ('a', 'b', 'c', 'd', 'e',)  # some functions
print(mytuple2.count('a'))
print(mytuple2.index('c'))

mylist = list(mytuple)        # converting
print(mylist)

mytuple = tuple(mylist)
print(mytuple)

mytuple3 = "max", 24, "boston"  # unpacking
name, age, city = mytuple3
print(name, age, city)

mytuple4 = 0, 1, 2, 3, 4, 5  # functional unpacking
i1, *i2, i3 = mytuple4
print(i1)
print(i2)
print(i3)
