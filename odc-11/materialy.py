name = 'Kasia'
number = 2

# Konkatencja
# Mało czytelny kod
message = name + ' ma ' + str(number) + ' koty'    
print(message)           # Kasia ma 2 koty

# Metoda format()
# Czytelny kod
message = '{} ma {} koty'.format(name, number)      
print(message)           # Kasia ma 2 koty

message = '{0} ma {1} koty i {1} pieski'.format(name, number)   
print(message)           # Kasia ma 2 koty i 2 pieski

# f-string - nowa właściwość w Python 3
# Czytelny kod
message = f'{name} ma {number} koty i {number} pieski'          
print(message)           # Kasia ma 2 koty i 2 pieski