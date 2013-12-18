tekst=raw_input("Sisesta midagi: ")
# print "\033[y;xH"  viib kursori koordinaatidele x ja y
print "\033[2J"


import sys

def kursor(x, y, t):
    sys.stdout.write("\033[" + str(y) + ";" + str(x) + "H" + t)

kursor(20, 22, tekst)

def kast (x, y, w, h):
        
         kursor(x, y, "#")
         kursor(x+w, y, "#")
        
         kursor(x, y+h, "#")
         kursor(x+y, y+h, "#")
        
kast(10,20,20,20)  
