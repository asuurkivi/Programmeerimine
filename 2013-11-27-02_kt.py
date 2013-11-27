import math
import decimal
print "ylesanne 1"
arv1=raw_input("sisesta 1. arv: ")
arv2=raw_input("sisesta 2. arv: ")
if arv1.isdigit() and arv2.isdigit():
	print int(arv1)+int(arv2)
	print int(arv1)-int(arv2)
	print int(arv1)*int(arv2)
	print int(arv1)/int(arv2)
	print int(arv2)/int(arv1)
	aste=raw_input("Sisesta arvude " + arv1 + " ja " + arv2 + " astendaja: ")
	print int(arv1)**int(aste)
	print int(arv2)**int(aste)

	print "ylesanne 2"

	print math.radians(float(arv1))
	print math.degrees(float(arv1))
	print math.sin(float(arv1))
	print math.atan(float(arv2))
	print math.pi

	print "ylesanne 3"
	import math.e
	print ((e**arv1)-(e**(-arv1))/((e**arv1)+(e**(-arv1))
	#en.wikipedia.org/wiki/Normal_distribution
else:
	print "Tekkis viga. Kontrolli, kas sisestasid arvud!"
	
#l6petamata
