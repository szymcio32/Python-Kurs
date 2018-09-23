parzyste = 0
nieparzyste = 0

for i in range(1, 15):
    if i % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'Ilosc parzystych liczb to: {parzyste}')
print(f'Ilosc nieparzystych liczb to: {nieparzyste}')

nowe_wyrazy = []

while True:
    wyraz = input('Podaj wyraz (q aby zakonczyc): ')
    if wyraz == 'q':
        break
    nowe_wyrazy.append(wyraz.upper())

i = 0
for w in nowe_wyrazy:
    i += 1
    print(f'{i}. wyraz to {w}')