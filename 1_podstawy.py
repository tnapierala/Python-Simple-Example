print("Anna")
print(8)

#potegowanie
pow=2**10
print(pow)

text="CDV"
print(text*2)

#pobieranie danych z klaw
#+ konkatenacja
name=input("Podaj imie: ")
print("Twoje imie: " + name ) 

surname=input("Podaj swoje nazwisko: ")
print("Imie: " + name + ", nazwisko: " + surname )

lenghtName=str(len(name))
print("Długość imienia: " + lenghtName )


lenSurname=len(surname)
print(lenSurname)
print(type(lenSurname))
print(type(lenghtName))
print(type(surname))

#zad1
age=int(input("Podaj wiek: "))

print("Imię i nazwisko: " + name + " " + surname + ", wiek: " + age + " lat " )

#/

print("\nPodaj narodowość: ", end="")
nationality=input()

surname="Kowalski"
#pierwsza litera
firstLetter=surname[0]
print(firstLetter)
#ostatnia litera
lastLetter=surname[len(surname)-1]
print(lastLetter)

#konwersja typów danych
a="10"
print(type(a)) #string
a=int(a)
print(type(a)) #int

b=5
print(type(b))  #int
b/=2   #b=b/2
print(type(b)) #float
print(b) #3.0


print()
surname="Nowakowski"
print(surname[0])     # N
print(surname[0:2])   # No
print(surname[-2])    # k
print(surname[-2:])   # ki
print(surname[:-2])   # Nowakows
print(surname[:-2:2]) # NWkw
