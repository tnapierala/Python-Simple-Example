print("\n Witaj w programie, ktory wylosuje liczby")
print(" z zakresu, ktory mu podasz")

print("\n\tTomasz Napierala \n")
import random
while 1:
    try:
        liczba1=int(input("\nPodaj zakres min: "))
        liczba2=int(input("Podaj zakres max: "))

    except ValueError:
        print("Błąd! Wpisałeś wartość inną niż cyfra ")

    else:
        # Losowa wartosc z zakresu podanego od uzytkownika
        print("\nWylosowane liczby to: ")
        print("\n  Liczba1: " + str(random.randint(liczba1, liczba2)))
        print("\n  Liczba2: " + str(random.randint(liczba1, liczba2)))
        print("\n  Liczba3: " + str(random.randint(liczba1, liczba2)))
        print("\n  Liczba4: " + str(random.randint(liczba1, liczba2)))
        print("\n  Liczba5: " + str(random.randint(liczba1, liczba2)) + "\n\n")
    