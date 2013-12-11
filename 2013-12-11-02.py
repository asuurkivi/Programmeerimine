import math
a=float(raw_input('a = '))
b=float(raw_input('b = '))
c=float(raw_input('c = '))

d = b**2-4*a*c 

def ruutv(a, b, c):
	if d < 0:
		print "Sellisel ruutv6rrandil lahendid puuduvad"
	elif d == 0:
		x = (-b+math.sqrt(b**2-4*a*c))/2*a
		print "Sellisel ruutv6rrandil on yks lahend: ", x
	else:
		x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
		x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
		print "Sellisel ruutv6rrandil on 2 lahendit: ", x1, " ja", x2

ruutv(a, b, c)
