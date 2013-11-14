x1 = 10
y1 = 15
r1 = 5

x2 = 25
y2 = 30
r2 = 10

x = 20
y= 20

dx1 = x1 - x
dy1 = y1 - y
dx2 = x2 - x
dy2 = y2 - y

d1 = (dx1**2 + dy1**2) ** 0.5
d2 = (dx2**2 + dy2**2) ** 0.5

p1 = d1 < r1
p2 = d2 < r2

if (p1 and not p2) or (p2 and not p1):
	print "punkt ({},{}) asub piirkonnas.".format(x,y)
else:
	print "ei ole piirkonnas"
