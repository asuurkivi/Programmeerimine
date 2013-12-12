print 'ylesanne1'
tekst=raw_input('Sisesta oma tekst: ')
midagi=raw_input('Sisesta veel midagi: ')
print tekst.upper()
print tekst.lower()
print tekst.center(80)
print tekst.replace(' ','_')
print ' '

print 'ylesanne2'
#ei_suuda_lahendada
print ' '

print 'ylesanne3'
if len(tekst)>10:
	print 'tekst on pikem kui 10 m2rki'
else:
	print 'tekst ei ole pikem kui 10 m2rki'
if ' ' in tekst:
	print 'tekst sisaldab tyhikut'
else:
	print 'tekst ei sisalda tyhikut'
if 'x' not in tekst:
	print 'tekst ei sisalda x'
else: 
	print 'tekstis sisaldab x'
if midagi in tekst:
	print tekst + ' sisaldab ' + midagi
else:
	print tekst + ' ei sisalda ' + midagi
if tekst.isupper():
	print 'tekst sisaldab ainult suurt2hti'
elif tekst.isalnum():
	print 'tekst sisaldab mitte-t2hti'
else:
	print 'tekstis on ka v2iket2hed'
print ' '

print 'ylesanne4'
#ei_suuda_lahendada
print ' '
print 'ylesanne5'
print 'x arv tekstis on: ' + tekst.count('x')
