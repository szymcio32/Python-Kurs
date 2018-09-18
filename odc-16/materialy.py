creatures = ['ork', 'goblin', 'troll', 'ogr']

for enemy in creatures:
    print(enemy)

########################
# OUTPUT:
# ork
# goblin
# troll
# ogr

for num in range(4):
    print(num)

########################
# OUTPUT:
# 0
# 1
# 2
# 3

string = "hello world"

for letter in string:
    print(letter)

########################
# OUTPUT:
# h
# e
# l
# l
# o
#
# w
# o
# r
# l
# d

creatures = ['ork', 'goblin', 'troll', 'ogr']

for enemy in creatures:
    if enemy == 'troll':
        print("Koniec petli. Znalezlismy trolla")
        break
    print(enemy)

########################
# OUTPUT:
# ork
# goblin
# Koniec petli. Znalezlismy trolla


for enemy in creatures:
    if enemy == 'troll':
        continue
    print(enemy)

########################
# OUTPUT:
# ork
# goblin
# ogr


i = 0
while i < 10:
    print(i)
    i += 1      # i = i + 1

########################
# OUTPUT:
# 0
# 1
# ...
# 8
# 9

i = 0
while i < 10:
    print(i)
    if i == 5:
        i = 20
        print(f"Nasza liczba to {i}. Koniec petli while")
    i += 1
print(i)

########################
# OUTPUT:
# 0
# 1
# ...
# 5
# Nasza liczba to 20. Koniec petli while
# 21


# Nieskonczona petla
# while True:
#     print('Nieskonczona petla')