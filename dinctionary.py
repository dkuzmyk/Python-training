# dictionary key-value pairs mutable
mydict = {"name": "max", "age": 28, "city": "new york"}  # create
print(mydict)

mydict2 = dict(name="mary", age=20, city="boston")  # get
value = mydict2["name"]
value2 = mydict["name"]
print(value, value2)

mydict["email"] = "max@pog.com"  # set
print(mydict)

del mydict["name"]  # remove specific
print(mydict)

mydict.pop("age")  # remove specific
print(mydict)

mydict.popitem()  # remove last
print(mydict)

if "city" in mydict:            # print if exists
    print(mydict["city"])

try:                            # try catch in python
    print(mydict["name"])
except:
    print("No such item")

# looping
mydict = {"name": "max", "age": 28, "city": "new york"}  # print keys
for key in mydict.keys():
    print(key)

for key in mydict.values():                              # print values
    print(key)

for key, value in mydict.items():                        # get both key and values
    print(key, value)

mydict.update(mydict2)                                   # update to new values
print(mydict)

mytuple = (8, 7)                                         # tuple as key
mydict = {mytuple: 1}
print(mydict[mytuple])

