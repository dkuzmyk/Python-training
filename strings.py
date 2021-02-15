# strings
mystring = "poggers"
print(mystring)

mystring2 = 'I\'m a programmer'
print(mystring2)

letter = mystring[4]   # can access but can't change
print(letter)

substrng = mystring[1:5]
print(substrng)

mystring2.strip()       # remove white spaces

mystring2.upper()
mystring2.lower()

if mystring2.startswith('something'):
    print("yes")
elif mystring2.endswith('else'):
    print("no")
else:
    print("pog")

mystring2.find('aa')
mystring2.count('a')
newstring = mystring.replace('gg', 'Universe')
print(newstring)

mynewstring = "hello there my friend i love you"
newlist = mynewstring.split(" ")
print(newlist)

newerstring = ' '.join(newlist)
print(newerstring)


var = "Tom"
var2 = "Beepo"
mystring = "the variable is %s" % var  # c style
print(mystring)

mystring = "my friend is {} which is {}'s brother".format(var, var2)
print(mystring)

mystring = f"my friend is {var+var2.lower()} which is {var2}'s brother"
print(mystring)
