import math
print "TAHELEPANU! programm tootab SIIS ja AINULT SIIS, kui sisestad numbrid!"
a=float(raw_input("Sisesta arv a: "))
b=float(raw_input("Sisesta arv b: "))
print a+b
print a-b
print b-a
print a*b
print a/b
print b/a
print a**b
print b**a
print ""
print math.radians(a)
print math.degrees(a)
print math.sin(a)
print math.atan(b)
print math.pi

p = 2 
x = 3 
u = 4 

f = 1/(p//2*math.pi)**math.e**(-((x-u)**2)/(2*p**2))
print ""
print f
print ""
import datetime
d = datetime.datetime(2013, 03, 02) 
print '{:%d-%m-%Y}'.format(d)

e=1
f=1.3
g=0.05
h=9.99
#ylesanne 4 lahendamine ei onnestunud

print math.ceil(a)
print math.trunc(b)
