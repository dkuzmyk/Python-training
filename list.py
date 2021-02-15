# list
mylist = [1,1.4,"poggers"]
print(mylist)

item = mylist[0]    # first item
item2 = mylist[-1]  # last item
print(item2)

mylist2 = mylist   # copy
print(mylist2)

for a in mylist:   # iterate thro
    print(a)

if 1.5 in mylist:  # if
    print("it's here")
else:              # else
    print("no " + str(1.5) + " item")  # cast to string

print("len: "+str(len(mylist)))       # length

mylist.insert(1, "beepo")             # insertion
print(mylist)

mylist.append("appended")             # add end
print(mylist)

mylist.pop()                          # remove end
print(mylist)

mylist.remove("poggers")
print(mylist)

mylist.reverse()
print(mylist)

mylist3 = [1, 2, 5, 3, 5, 67, 7, 3, 4, 6, 2, 10, 145, 15, 15, 6, 7]
mylist3.sort()
print(mylist3)

mylist4 = [5]*5
mylist5 = mylist3 + mylist4
print(mylist5)

mylist5 = mylist5[1:9]  # slicing 1 to 9
print(mylist5)

mylist5 = mylist5[:8]  # slicing start to 9 [s:e], [:e], [s:]
print(mylist5)

mylist5 = mylist5[::2]  # slicing start to end with step 2
print(mylist5)

mylist6 = mylist5.copy()  # make actual copy
mylist5.append(123)
mylist6.append("pog")
print(mylist5)
print(mylist6)

mylist7 = [0, 1, 2, 3, 4, 5]
mylist8 = [i*i for i in mylist7]
print(mylist8)


