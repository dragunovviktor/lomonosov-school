
#1
'''
def f(x, a):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100)

for a in range(1, 10**5):
    if all(f(x,a) == 1 for x in range(1,10000)):
        print(a)
        break
'''


#2
'''
def f(x,a):
        return ((x % 3 == 0) <= (x % 17 != 0)) or (not(a < 190 - x))

for a in range(1, 10 ** 5):
    if all(f(x,a) == 1 for x in range(1,10000)):
        print(a)
        break
'''

#3
'''
B = [int(x) for x in range(70, 81)]

def f(x, a):
    return (x % a == 0) or ((x in B) <= (x % 18 != 0))

c = 0
for a in range(1, 10 ** 5):
    if all(f(x,a) == 1 for x in range(1,10000)):
        c += 1
print(c)
'''

#4


'''
def f(x, a, y):
    return (x < a) or (y < a) or (x + 2 * y > 150)

for a in range(1, 10 ** 5):
    if all(f(x,a,y) == 1 for x in range(1,10000) for y in range(1,1000)):
        print(a)
        break
'''

#5
'''
def f(x, a, y):
    return (11 * x - y != 53) or (x > y) or (a < x)

for a in range(1, 10 ** 5):
    if all(f(x,a,y) == 1 for x in range(1,1000) for y in range(1,1000)):
        print(a)
'''

#6
'''
def f(x, a):
    return (a % 35 == 0) and ((730 % x == 0) <= ((a % x != 0) <= (110 % x != 0)))

c = 0
for a in range(1, 1000):
    if all(f(x,a) == 1 for x in range(1,1000)):
        c += 1
print(c)
'''

#7


'''
def f(x, a):
    return ((x % 15 == 0) and (x % 21 != 0) ) <= ((x % a != 0) or (x % 15 != 0))

for a in range(1, 10**5):
    if all(f(x,a) == 1 for x in range(1,1000)):
        print(a)
        break
'''

#8


'''
def f(x, a):
    return ((x % a == 0) and (x % 21 == 0)) <= (x % 18 == 0)


for a in range(1, 10**5):
    if all(f(x,a) == 1 for x in range(1,1000)):
        print(a)
        break
'''

#9


'''
def f(x, a):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)

for a in range(1, 10**5):
    if all(f(x,a) == 1 for x in range(1,1000)):
        print(a)
        break

'''
