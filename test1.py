'''class itsclass ():
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def art (self):
        print(self.name)
        print(self.age)
class own (itsclass):
    v = "its global of own"
    def func (self):
        print("itsclass in herited")
        print(own.v)


v = own("eswar","24")
v.art()
v.func()'''
'''k = 1
l = 5
c = 5
for  i in range (0,5):
    for j in  range (0,k):
        print(" ",end='')
    k = k  + 1

    for v  in range(0,l):
        print("*",end='')
    l = l - 1

    for m in range(0,l+1):
        print('*',end='')
    

    print("")
'''
'''txt = "this is format string {price:.2f}"
print(txt.format(price = 250))

l  = [k for k in a(123456)  ]
print(l)'''
'''
a,b = input().split()
i = input().split()
l = [int(j) for j in i]
c = int(input())
bill = l[int(b)]

g = 0
for i  in  range(len(l)):
    if l[i] == bill:
        continue
    g = g+l[i]
ac = g/2
if int(c - ac) == 0:
    print('Bon Appetit')
else:
    print(int(c - ac))
'''
'''from math import *
y = max([2,2,3])
print(y)
x = abs(-7.25)
print(x)
print('TTHE FORGIT {THE:.2F}'.format(THE = 100))
x = pow(4,2)
print(x)
print = sqrt(2)
print(4**4)'''

'''d = {"a":12 , 'b':23 ,'c' :78}

f = dict(d)

for i,j  in d.items():
    v = f[i]
    f[i] = v + j

print(f)

del d['d']'''


def func (n):
    for i in range (0,n):
        yield i 

h = func(10)
for i in h:
    print(i)


