# Metoda strip() usuwa wskazane znaki w tekście (od początku i od końca tekstu)
# Domyślny znak to spacja
zmienna = '  taki piekny dzien  '
print(zmienna)                  # '  taki piekny dzien  '
print(len(zmienna))             # 21

zmienna = zmienna.strip()   
print(zmienna)                  # 'taki piekny dzien'
print(len(zmienna))             # 17

zmienna = 'taki piekny dzien'
print(zmienna.strip('piekny'))  # taki piekny dz


# Metoda split() zwraca listę wyrazów w tekście używając wskazanego znaku jako separatora
# Domyślny znak to spacja
zmienna = 'raz dwa trzy'
zmienna = zmienna.split()       
print(zmienna)                  # ['raz', 'dwa', 'trzy']

zmienna = 'raz??dwa??trzy'
zmienna = zmienna.split('??', maxsplit=1)
print(zmienna)                  # ['raz', 'dwa??trzy']
