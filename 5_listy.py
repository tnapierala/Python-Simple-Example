progr=['Python', 'PHP', 'C#', 'JS', 'Java']
print("progr")
print(type(progr))

first=progr[0]
print(first)

threeElements=progr[0:3]
print(threeElements)

last=progr[-1]
print(last)


#Dodanie nowego elementu na koniec listy
progr.append('R')
progr.append('Python')
print(progr)


#załączanie elementu w liście
countElement=progr.count('Python')
print(countElement)


#Ilość elementów w liście
countElementsOfList=len(progr)
print(countElementsOfList)


#Połączenie list
anotherList=['C', 'C++']
progr.extend(anotherList)
print('progr: ' + str(progr))
print('anotherLits: ' + str(anotherList))

#Usuwanie elementów z listy
new=progr
print('New list: ' + str(new))
new.clear()
print('New list: ' + str(new))
print('Rozmiar New list: ' + str(len(new)))
print('progr list: ' + str(progr))
print('Rozmiar progr list: ' + str(len(progr)))

x=8
print(x)
y=x
print(y)

y=5
print(x) #8
print(y) #5

'''

Dodaj listę o nazwie: country
Przypisz do niej 5 elementów
Poproś użytkownika, aby dodał dwa nowe elementy do listy
Użytkownik wyświetli listę do wybor:

1) Wyświetl pierwsze 3 elementy listy 
2) Wyświetl elementy listy, które dodałe (dane pobierz z listy)
3) wyświetl zawartość listy
4) Wyczyść zawartość listy
5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)

Użytkownik raz dokonuje wyboru z listy
Wyświetl zawarość listy po wykoaniu operacji przez użytkownika

'''

country=['Poland', 'USA', 'Denemark', 'France', 'Deutchland']

print("Dodaj proszę dwa nowe country xD")

new_country = []
print("First country:")
new_country.append(input())
print("Second country:")
new_country.append(input())
country.extend(new_country)


print('Do wyboru: ')
print('1) Wyświetl pierwsze 3 elementy listy')
print('2) Wyświetl elementy listy, które dodałe (dane pobierz z listy) ')
print('3) wyświetl zawartość listy ')
print('4) Wyczyść zawartość listy ')
print('5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy) ')

choise=input()

if choise == "1":
    print("3 pierwsze elementy listy: ")
    print(country[0:3])
if choise == "2":
    print('Elementy usera ')
if choise == "3":
    print("Zawartość listy: " + country)

if choise == "4":
    print('Czyścimy listę')
    country.clear()
    print("Zawartość listy: " + str(country))
if choise == "5":
    print('Jaki kraj szukasz?')
