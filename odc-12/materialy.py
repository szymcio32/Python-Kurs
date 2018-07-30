colors = ['żółty', 'biały', 'niebieski', 'czarny']

# print(colors)             # ['żółty', 'biały', 'niebieski', 'czarny']
# print(len(colors))        # 4


### INDEKSOWANIE I WYCINANIE ###
# print(colors[0])          # żółty
# print(colors[3])          # czarny
# print(colors[0:2])        # ['żółty', 'biały']
# print(colors[2:])         # ['niebieski', 'czarny']


### Metoda index() - zwraca numer indeksu pod którym znajduje się dana wartość.
# print(colors.index('żółty'))        # 0
# print(colors.index('fioletowy'))    # ValueError


### Metoda append() - dodaje na koniec listy nowy element o określonej wartości.
colors.append('czerwony')           # ['żółty', 'biały', 'niebieski', 'czarny', 'czerwony']
# print(colors)


### Metoda insert() - dodaje element o konkretnej wartości do wskazanej pozycji na liście .
colors.insert(0, 'zielony')         # ['zielony', 'żółty', 'biały', 'niebieski', 'czarny', 'czerwony']
# print(colors)


### Metoda extend() - dodaje na koniec listy elementy z innej listy bądź obiektu iterable.
colors_2 = ['granatowy', 'bordowy'] 
# colors.append(colors_2)            # ['zielony', 'żółty', 'biały', 'niebieski', 'czarny', 'czerwony', ['granatowy', 'bordowy']]
# colors.insert(0, colors_2)         # [['granatowy', 'bordowy'], 'zielony', 'żółty', 'biały', 'niebieski', 'czarny', 'czerwony']    
colors.extend(colors_2)              # ['zielony', 'żółty', 'biały', 'niebieski', 'czarny', 'czerwony', 'granatowy', 'bordowy']
# print(colors)


### Metoda remove() - usuwa element o określonej wartości z listy.
colors.remove('niebieski')          # ['zielony', 'żółty', 'biały', 'czarny', 'czerwony', 'granatowy', 'bordowy']
# print(colors)


### Metoda pop() - usuwa ostatni bądź wskazany element z listy. Zwraca również usuwaną wartość.
colors.pop()                        # ['zielony', 'żółty', 'biały', 'czarny', 'czerwony', 'granatowy']
# print(colors)
colors.pop(0)
# print(colors)                       # ['żółty', 'biały', 'czarny', 'czerwony', 'granatowy']

white_color = colors.pop(1)           # biały
print(colors)                         # # ['żółty', 'czarny', 'czerwony', 'granatowy']
# print(white_color)


### Słowo 'in' sprawdza czy dana wartość występuje w określonej liście. Zwraca True lub False.
# print('czarny' in colors)           # True
# print('zielony' in colors)          # False
