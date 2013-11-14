import math
a = float (raw_input('a = '))
b = float (raw_input('b = '))
c = float (raw_input('c = '))
d = float (raw_input('d = '))

p = -b/(3*a)
q = p**3 + (b*c - 3*a*d) / (6 * a**2)
r = c / (3*a)

print "p = {}".format(p)
print "q = {}".format(q)
print "r = {}".format(r)

x= (q+(q**2+(r-p**2)**3)**(1.0/2))**1.0/3+(q-(q**2+(r-p**2)**3)**(1.0/2))**(1.0/3)+p

print "x = {}".format(x)
