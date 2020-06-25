
uzytkownika = []

while True:
    try:
        ile=int(input("\n Wprowadź liczbę elementów do posortowania<1..10>: "))
        if ile >= 1 and ile <= 10:
            for i in range(ile):
                licz = int(input('  Wprowadź wartość: [' + str(i+1) + ']: '))
                uzytkownika.append(licz)
            print('\n\n  Wyprowadzanie posortowanych elementów: ')
            uzytkownika.sort()
            for i in range(ile):
                print("Element [" + str(i+1) + '] = ' + str(uzytkownika[i]))
            print('\n Koniec sortowania :D \n')
        else:
            print("Zła liczba, spróbuj ponownie!")
            
    except ValueError:
        print("\nZła liczba, spróbuj ponownie... ")