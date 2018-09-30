# Set (zbiory)- to typ danych w Pythonie, posiadający nieuporządkowane
# oraz unikatowe elementy.

list_of_creatures = ['ork', 'goblin', 'troll', 'ogr']
set_of_creatures = {'ork', 'goblin', 'troll', 'ogr'}

print(list_of_creatures)
print(set_of_creatures)

##1. Set nie posiadają zduplikowanych wartości
##   Każdy element jest unikatowy.

list_of_creatures = ['ork', 'goblin', 'troll', 'ogr', 'ogr']
set_of_creatures = {'ork', 'goblin', 'troll', 'ogr', 'ogr'}

print(list_of_creatures)      # ['ork', 'goblin', 'troll', 'ogr', 'ogr']
print(set_of_creatures)       # {'goblin', 'ogr', 'ork', 'troll'}

##2. Elementy w set są nieuporządkowane

list_of_creatures = ['ork', 'goblin', 'troll', 'ogr']
set_of_creatures = {'ork', 'goblin', 'troll', 'ogr'}

print(list_of_creatures)      # ['ork', 'goblin', 'troll', 'ogr']
print(set_of_creatures)       # np. {'goblin', 'ork', 'ogr', 'troll'}

##3. Nie możemy odwołać się do konkretnego elementu w set
##   za pomocą indeksowania

list_of_creatures = ['ork', 'goblin', 'troll', 'ogr']
set_of_creatures = {'ork', 'goblin', 'troll', 'ogr'}

print(list_of_creatures[0])     # ork
# print(set_of_creatures[0])      # Type Error


########### Set i jego główne zastosowanie:
## - usuwanie zduplikowanych elementów
## - sprawdzanie czy element znajduje się w set


set_of_creatures = {'ork', 'goblin', 'troll', 'ogr'}
set_of_ugly_creatures = {'centaur', 'troll', 'chochlik', 'ogr'}

## intersection() - pokazuje wspólne wartości dla obu sets

print(set_of_creatures.intersection(set_of_ugly_creatures))     # {'troll', 'ogr'}


## difference() - pokazuje tylko elementy, które są w set_of_creatures
## ale nie ma ich w set_of_ugly_creatures

print(set_of_creatures.difference(set_of_ugly_creatures))       # {'ork', 'goblin'}


## union() - pokazuje unikatowe wartości dla obu sets

print(set_of_creatures.union(set_of_ugly_creatures))    # {'goblin', 'ogr', 'troll', 'chochlik', 'ork', 'centaur'}