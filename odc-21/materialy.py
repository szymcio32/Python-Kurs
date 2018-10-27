daneOsobowePracownika = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'wiek': 35,
    'imiona rodzicow': ['Andrzej', 'Iwona']
}

klucz = 'pensja'
if klucz in daneOsobowePracownika:
    del daneOsobowePracownika[klucz]
    print(f'klucz {klucz} został usunięty')
else:
    print(f'klucz {klucz} nie istnieje w słowniku')

print(daneOsobowePracownika.keys())
print(list(daneOsobowePracownika.values()))
print(daneOsobowePracownika.items())

for klucz in daneOsobowePracownika.items():
    print(klucz)

