
slownik = {'klucz': 'wartosc'}

print(slownik)

pustySlownik = {}

print(type(pustySlownik))

daneOsobowePracownika = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'wiek': 35,
    'imiona rodzicow': ['Andrzej', 'Iwona']
}

print(daneOsobowePracownika)

daneOsobowePracownika['waga'] = '85kg'
daneOsobowePracownika['wzrost'] = '185cm'

print(daneOsobowePracownika)

print(daneOsobowePracownika['nazwisko'])
# print(daneOsobowePracownika['pensja'])      # KeyError

print(daneOsobowePracownika.get('imie'))
print(daneOsobowePracownika.get('pensja', 'Ten klucz nie istnieje'))

daneOsobowePracownika['waga'] = '90kg'
print(daneOsobowePracownika['waga'])

daneOsobowePracownika.update({'wiek': 36, 'waga': '80kg', 'wzrost': '183cm'})
print(daneOsobowePracownika)

del daneOsobowePracownika['waga']
# del daneOsobowePracownika['pensja']     # Key error
print(daneOsobowePracownika)

print(daneOsobowePracownika.pop('imie'))
print(daneOsobowePracownika)
print(daneOsobowePracownika.pop('pensja', 'Nie znaleziono takiego klucza'))     
