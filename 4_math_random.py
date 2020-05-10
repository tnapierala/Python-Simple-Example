#pi
import math
pi=math.pi
print(pi)

#pierw
x=math.sqrt(9)
print(x)

#losowanie
import random
rand=random.random()
print(rand)

list=random.choice([1,2,3,4,5,6])
print(list)

'''
Użytkowanik podaje z klawiatury liczbę całkowitą z zakresu <1; 10>
Sprawdź czy liczb jest prawidłowa:
tak) wylosuj liczbę z podanego zakresu
    porównaj liczbę wylosowaną z liczbą podną przez użytkownika i sprawdź czy zgadł wylosowaną
    wartość ("Gratulacje" lub "spróbuj innym razem")
nie) poinforumuj użytkowanika o błędzie
'''

    

lista=random.choice([1,2,3,4,5,6,7,8,9,10])
print(lista)

print("Wylosowano liczbę 1-10, próbuj zgadnąć xD")
x=int(input("Podaj Twoją liczbę:  "))


if x==lista:
    print("Wartość podana jest prawidłowa")
else:
    print("Niestety nie tym razem Ci się nie udało, liczba to: " + str(lista))
