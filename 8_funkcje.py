
def show():
  print('Funkcja show')

show()


def iloraz(a, b):
  return a/b

print(iloraz(4, 2))
print(type(iloraz(4, 2)))


def iloraz1(a, b):
  return a//b

print(iloraz(3,7))
print(iloraz1(3, 7))
print(iloraz1(8, 3))

###### spojrzeć!
def iloraz2(a, b):
  x = a/b
  return "{:.2f}".format(x)

print(iloraz2(4, 7))



def iloraz3(a, b):
  x = a/b
  return "{:.5f}".format(x)

print(iloraz3(4, 7))

# inny sposób
a=4
b=7
x = a/b
print("Liczba z dwoma miejscami po przecinku: {:.2f}".format(x))

######
def sum(*a):
  result=0
  for x in a:
    result += x
  return result

print(sum(1, 2, 3, 10))


'''
Użytkownik podaje z klawiatury:
marka, model, pojemnosc, predkoscMax
utwórz funkcję, która pobierze dane od użytkownika i przypisze do słownika

utwórz drugą funkcję wyświetlającą dane w formacie:
Marka: ...
Model: ...
Pojemnosc: ...
Predkosc maksymalna: ...
'''
