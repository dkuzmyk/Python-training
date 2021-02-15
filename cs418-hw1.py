import random


def function(r):
    sum = 0
    for a in range(r + 1):
        sum += a * a
    return sum


print(function(5))

l = lambda x: x * x + l(x - 1) if x > 0 else False
print(l(5))


def double_letters(s):
    # complete this function
    str = ""
    for a in s:
        str += a
        str += a
    return str


s = 'Hello'
print(double_letters(s))

s = 'aardvark'
print(len(s))
print(s * 5)
print(s[0])
print(s[0:3])
print(s[len(s) - 3::])
print(s[::-1])
print(s[1:len(s) - 1])
print((s.upper()))
print(s.replace('a', 'e'))
print('The ' + s)

days = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri']
print(days[0:3])
print(days[-1])
print(days[len(days) - 3::])

count = 0
l = []
for a in days:
    if count % 2 != 0:
        l.append(a)
    count += 1
print(l)

print(days[::-1])

li = []
for a in reversed(days):
    li.append(a)
print(li)

L = [(random.randint(0, 100)) for i in range(15)]
print(L)

L = list(map(lambda x: x * x, L))
print(L)

print(len(list(filter(lambda a: a > 60, L))))
print(len(list(filter(lambda a: a < 30, L))))

rac_alum = {
    'Albert': '1996',
    'Ada': '1998',
    'Barry': '1996',
    'Carlos': '1999',
    'Chris': '1996',
    'Claire': '1998',
    'Jill': '1999',
    'Rebecca': '2002',
    'Luis': '2004',
    'Leon': '1998',
}

rac_alum['Ashley'] = '2004'
print(rac_alum)

rac_alum.pop('Barry')
print(rac_alum)

rac_alum['Leon'] = '2004'
print(rac_alum)


def reverse_dict(map):
    map2 = dict()

    for tmp in map:
        print(tmp, map[tmp])
        map2.setdefault(map[tmp], []).append(tmp)
    return map2


print(reverse_dict({"Alice": "Chicago", "Bob": "Detroit", "Jenna": "Chicago", "Adam": "Chicago"}))
# => {"Chicago": ["Alice", "Jenna", "Adam"], "Detroit": ["Bob"]}


points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
          'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
          'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
          'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

# z e b r a = 10 + 1 + 3 + 1 + 1 = 16

words = ['airplane', 'zebra', 'statistics', 'algorithm']


def fun(w):
    for k in w:
        k = k.upper()
        sum = 0
        for j in k:
            sum += points[j]
        print("word: ", k, " points: ", sum)


fun(words)


dat = open('Yellow_Wallpaper_PROJECT_GUTENBERG.txt', encoding="UTF8").read()

dat = dat.lower()


dat = "".join(u for u in dat if u not in ('.', ',', '!', '?', ':', '“', '’', '”', '—'))

data = dat.split()

print(data)


d = dict()

for w in data:
    d[w] = data.count(w)

print(d)

for k, v in sorted(d.items()):
    print(k,':',v)
