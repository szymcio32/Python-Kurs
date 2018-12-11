def printNumbers(number, *args):
    print(f'First number {number}')
    for num in args:
        print(f'Next number {num}')

nums = [3, 4, 5]
printNumbers(*nums)
printNumbers(8, 40, 20, 77, 7)



def printScores(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

printScores(imie='Jan', wiek=26, waga='77 kg', dlugie_wlosy=True)