wiadomosc = 'Wina wina wina dajcie'

# Metoda count() zwraca liczbę wystpień danego wyrazu / znaku w tekście
print(wiadomosc.count('wina'))      # 2
print(wiadomosc.count('i'))         # 4

# Metoda find() zwraca numer indeksu pod którym znajduje się wskazany znak
print(wiadomosc.find('dajcie'))     # 15
print(wiadomosc.find('piwa'))       # -1

# Metoda index() działa tak samo jak metoda find() 
# W przypadku nie wystąpienia podanego znaku w tekście metoda zwraca "ValueError"
print(wiadomosc.index('dajcie'))    # 15
# print(wiadomosc.index('piwa'))    # ValueError: substring not found

# Metoda replace() zamienia wskazany wyraz na nowy
wiadomosc.replace('wina', 'piwa')
nowa_wiadomosc = wiadomosc.replace('wina', 'piwa')

print(wiadomosc)        # Wina wina wina dajcie
print(nowa_wiadomosc)   # Wina piwa piwa dajcie

# Funkcja dir() zwraca listę metod dla danego obiektu
print(dir(str))
