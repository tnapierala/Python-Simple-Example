x = 5

if x == 5:
    print("x jest równa 5")
else:
    print("x nie jest równy 5")
    print("x nie jest równy: " + str(a))

print("Koniec instrukcji warunkowej")

#####################################

y=False

if y:
    print("Prawda")
else:
    print("Fałsz")

#####################################

z = 5 > 6
if z:
    print("Prawda")
else:
    print("Fałsz")

#####################################

#Użytkownik podaje wartości trzech zmiennych: x,y,z
#Wyświetla, która z tych wartości będzie największa
#wykorzystaj instrukcję warunkową


x=input("podaj")
y=input()
z=input()

if x>y and x>z:
    print("Wartość " + x + " jest największe")
elif x>y and y>z:
    print("Wartość " + y + " jest największe")
else:
    print("Wartość " + z + " jest największe")

