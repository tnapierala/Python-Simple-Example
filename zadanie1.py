print("\n Witaj w programie, ktory wylosuje liczby")
print(" z zakresu, ktory mu podasz")

print("\n\tTomasz Napierala \n")

liczba1=int(input("\nPodaj zakres min: "))
liczba2=int(input("Podaj zakres max: "))

import random
# Losowa wartosc z zakresu podanego od uzytkownika
print("\nWylosowane liczby to: ")
print("\n  Liczba1: " + str(random.randint(liczba1, liczba2)))
print("\n  Liczba2: " + str(random.randint(liczba1, liczba2)))
print("\n  Liczba3: " + str(random.randint(liczba1, liczba2)))
print("\n  Liczba4: " + str(random.randint(liczba1, liczba2)))
print("\n  Liczba5: " + str(random.randint(liczba1, liczba2)) + "\n\n")