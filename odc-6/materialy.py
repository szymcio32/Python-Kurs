# String to łańcuch znaków
# Funckja len() - zwraca liczbę elementów danego obiektu

##INDEKSOWANIE

# tekst = "Maly pies"

# print(tekst[0])   # M
# print(tekst[1])   # a
# print(tekst[4])   # " " spacja
# print(tekst[8])   # s
# print(tekst[-1])  # s

# print(tekst[9])   # Błąd: IndexError


##WYCINANIE

# tekst = "Maly pies"

# print(tekst[0:4])   # Maly
# print(tekst[0:5])   # Maly<spacja>
# print(tekst[:4])     # Maly
# print(tekst[5:9])   # pies
# print(tekst[5:])     # pies


##FUNKCJA LEN 

# tekst = "Kot w pustym mieszkaniu"
# liczba_slow = len(tekst)

# print(liczba_slow)  # 23
# print(len(tekst))     # 23