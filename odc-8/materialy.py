zdanie = 'pies LUBI SZczekac'

print(zdanie.lower())       # pies lubi szczekac
print(zdanie.upper())       # PIES LUBI SZCZEKAC
print(zdanie.capitalize())  # Pies lubi szczekac
print(zdanie.title())       # Pies Lubi Szczekac

print(zdanie)               # pies LUBI SZczekac

nowe_zdanie = zdanie.lower()
print(nowe_zdanie)          # pies lubi szczekac

print('tygrys'.islower())   # True
print('Tygrys'.islower())   # False

print('PUMA'.isupper())     # True
print('Puma'.isupper())     # False

#Znaki alfanumeryczne:  a-z A-Z 0-9
print('alaMA20lat'.isalnum())   # True
print('alaMA20 lat'.isalnum())  # False

#Znaki alfabetyczne:    a-z A-Z
print('to'.isalpha())      # True
print('to 1'.isalpha())    # False

#Cyfry:    0-9
print('6.5'.isdigit())     # False
print('65'.isdigit())      # True