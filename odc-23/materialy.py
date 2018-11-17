# jeden wymagany argument
def ulubionyOwoc(owoc):
    print(f'Twoj ulubiony owoc to {owoc} ')

ulubionyOwoc('gruszka')
# ulubionyOwoc()          # TypeError


# jeden wymagany i jeden opcjonalny argument
def ileLat(imie, wiek=26):
    print(f'{imie} ma {wiek} lat')

ileLat('Ala')
ileLat('Kasia', 20)


# trzy wymagane argumenty przekazane w innej kolejnosci
def pokazInformacje(imie, wiek, waga):
    print(f'{imie} ma {wiek} lat i wazy {waga} kg.')

pokazInformacje(imie='Janek', wiek=30, waga=90)
pokazInformacje(wiek=40, waga=75, imie='Mateusz')