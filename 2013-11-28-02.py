a = raw_input('Sisesta topeltt2hed: ')

if 'n' in  a:
	if 'w' in a:
		print "north-west"
	elif "e" in a:
		print "north-east"
elif "s" in a:
	if 'w' in a:
		print "south-west"
	elif "e" in a:
		print "south-east"
else:
	print "vale kombinatsioon"
