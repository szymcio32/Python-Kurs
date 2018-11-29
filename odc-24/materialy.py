def show(variable):
    print('---FUNKCJA SHOW---')
    print(f'Przed zmiana: {variable}')
    variable[0] = 'Poznan'
    variable[1] = 'Wroclaw'
    print(f'Po zmianie: {variable}')
    print(f'ID obiektu to: {id(variable)}')
    print('---KONIEC FUNKCJI SHOW---')


cities = ['Krakow', 'Warszawa']

print(f'Przed funkcja show: {cities}')
print(f'ID obiektu to: {id(cities)}')
show(list(cities))
print(f'Po funkcji show: {cities}')


# dict_cities = {
#     0: 'Gdynia',
#     1: 'Gdansk'}
#
# print(f'Przed funkcja show: {dict_cities}')
# print(f'ID obiektu to: {id(dict_cities)}')
# show(dict(dict_cities))
# print(f'Po funkcji show: {dict_cities}')