def sayHello():
    print('Czesc Michal! co slychac?')

def sayHello2(name):
    print(f'Czesc {name}! co slychac?')

def dodaj(x, y):
    suma = x + y
    return suma


sayHello()
sayHello2('Ania')

wynikDzialania = dodaj(5, 10)
print(wynikDzialania)