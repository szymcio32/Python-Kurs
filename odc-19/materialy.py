## Tuple to typ danych, ktory jest podobny do list

## Jak stworzyc krotke (tuple)?

a = 1, 2
print(type(a))          # <class 'tuple'>
b = (1, 2)
print(type(b))          # <class 'tuple'>
c = 1,
print(type(c))          # <class 'tuple'>
d = (1,)
print(type(d))          # <class 'tuple'>

e = (1)
print(type(e))          # <class 'int'>


## Krotki sa obiektami niemodyfikowalnymi

animals = ('lew', 'tygrys')
# animals[0] = 'wilk'         # TypeError

lion = animals[0]
tiger = animals[1]
print(lion)         # lew
print(tiger)        # tygrys

## Rozpakowywanie krotek

lion, tiger = animals
print(lion)         # lew
print(tiger)        # tygrys

## Funkcja tuple()

list_of_animals = ['pingwin', 'strus', 'jelen']
tuple_of_animals = tuple(list_of_animals)
print(tuple_of_animals)                         # ('pingwin', 'strus', 'jelen')