import getpass
pw = getpass.getpass("Testi parooli tugevust. Sisesta parool: ")
if not pw.isalpha() \
	and not pw.isupper() \
	and not pw.islower() \
	and len(pw)>=8 :
	print "salas6na on tugev"
else:
	print "salas6na on n6rk"
