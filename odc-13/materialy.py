colors = ['żółty', 'biały', 'niebieski', 'czarny']

### Metoda sort() - sortuje elementy w liście w kolejności odwrotnej do alfabetycznej
# colors.sort()                  # ['biały', 'czarny', 'niebieski', 'żółty']
# print(colors)


### Metoda sort(reverse=True) - sortuje elementy alfabetycznie w liście
# colors.sort(reverse=True)      # ['żółty', 'niebieski', 'czarny', 'biały']
# print(colors)


### Metoda reverse() - odwraca kolejność elementów w liście
# colors.reverse()               # ['czarny', 'niebieski', 'biały', 'żółty']
# print(colors)


### Funkcja sorted() - zwraca posortowaną listę
# sorted_colors = sorted(colors)
# print(colors)                   # ['żółty', 'biały', 'niebieski', 'czarny']
# print(sorted_colors)            # ['biały', 'czarny', 'niebieski', 'żółty']


### Metoda join() - zwraca tekst utworzony z elementów listy
# text_colors = ' '.join(colors)          # żółty biały niebieski czarny
# print(text_colors)


### Metoda split() - zwraca listę elementów utworzoną z tekstu na podstawie separatora
# new_colors_list = text_colors.split()   # ['żółty', 'biały', 'niebieski', 'czarny']
# print(new_colors_list)


# print(colors)
# colors[0] = 'pomarańczowy'      # ['pomarańczowy', 'biały', 'niebieski', 'czarny']
# print(colors)

# text_colors[0] = 'r'            # NameError: name 'text_colors' is not defined
