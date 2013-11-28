while True:
    t2ht = raw_input('Sisesta t2ht:')
    if len(t2ht) == 1:
        break
    print 'Palun sisesta ainult 1 t2ht'
guessInLower = t2ht.lower()
if "j" in t2ht:
	print "vasak"
elif "k" in t2ht:
	print "all"
elif "l" in t2ht:
	print "parem"
elif "i" in t2ht:
	print "yleval"
else:
	print "Tundmatu t2ht"
