#listy
progr=['PHP', 'Python']
print(type(progr))
progr.append('C#')
print(progr)
count=progr.count('PHP')
print(f'PHP występuje {count} razy\n\n')

#tuple
name=('Krystyna', 'Anna')
print(name)
print(type(name))
first=name[0]
print(name)
#name.append('Janusz') - nie można tego używać
print()

#słowniki

person = {
    'name' : 'Anna',
    'surname' : 'Nowak'
}

print(person)
print(type(person))
print(person['name'])
print(person.keys())
print(person.get('height', 'brak danych'))

person['height'] = 178
print(person.get('height', 'brak danych'))

print()


'''
Utwórz słownik i przypisz mu trzy imion podane z klawiatury
Wyświetl te dane na ekranie w formacie
Imię1: ..
Imię2: ..
Imię3: ..
'''

#zad

x = input("\n Podaj 1 imię: ")
y = input("\n Podaj 2 imię: ")
z = input("\n Podaj 3 imię: ")

ludzie = {
    0: x,
    1: y,
    2: z,
}


for key, value in ludzie.items():
    count=key+1
    print(f'Imie{count} : {value}')

print(f'Imię1: {ludzie[0]}')
print(f'Imię2: {ludzie[1]}')
print(f'Imię3: {ludzie[2]}')

#zad pana
n1 = input("\n Podaj 1 imię: ")
n2 = input("\n Podaj 2 imię: ")
n3 = input("\n Podaj 3 imię: ")

name = {
    0:n1,
    1:n2,
    2:n3
}

for key, value in name.items():
    count=key+1
    print(f'Imie{count} : {value}')

print(f'Imię1: {name[0]}')
print(f'Imię2: {name[1]}')
print(f'Imię3: {name[2]}')