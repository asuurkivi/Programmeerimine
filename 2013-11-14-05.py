import getpass
pw = getpass.getpass("Testi oma salas6na tugevust. Sisesta salas6na: ")
if not pw.isalpha() \
	and not pw.isupper() \
	and not pw.islower() \
	and len(pw)>=8 :
	print "salas6na on tugev"
else:
	print "salas6na on n6rk"
