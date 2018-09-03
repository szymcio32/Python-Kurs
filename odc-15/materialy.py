### Operator logiczny 'and'
# Aby operator miał wartość True to oba warunki muszą być prawdziwe
#

nieznajomy = 'ork'
bron = True

if nieznajomy == 'ork' and bron:        # oba warunki są True, więc wyrażenie 'if' jest True
    print('Atakuj!')                    # Atakuj!
else:
    print('To nie jest nasz wróg')

print(1 == 1 and 5 > 2)                 # True

#
### Operator logiczny 'or'
# Aby operator miał wartość True to przynajmniej jeden warunek musi być True
#

nieznajomy = 'ork'
bron = False
                                        # pierwszy warunek jest True, drugi False
if nieznajomy == 'ork' or bron:         # więc całe wyrażenie 'if' jest True
    print('Atakuj!')                    # Atakuj!
else:
    print('To nie jest nasz wróg')

#
### Operator logiczny 'not'
# Neguje (zaprzecza) wyrażenie logiczne
#

nieznajomy = 'czlowiek'
                                        # warunek jest True, ale następuje jego negacja,
if not nieznajomy == 'czlowiek':        # więc całe wyrażenie 'if' jest False
    print('Atakuj!')
else:
    print('To nie jest nasz wróg')      # To nie jest nasz wróg
