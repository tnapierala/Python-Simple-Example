# try except

'''
Napisać funkcję, która umożliwi użytkownikowi podzielenie dwóch liczb z precyzją do dwóch miejsc po przecinku
'''

## zerknij :P
def div(x, y):
  try:
    return round(x / y, 2)
  except ZeroDivisionError:
    print('Nie wolno dzielić przez 0!')

print(div(3, 7))

'''
Użytkownik podaje z klawiatuyr wartośc do momentu podania liczby całkowitej
'''

while True:
  try:
    num = int(input('Podaj liczbę całkowitą:'))
    print(f'Podałeś liczbę: {num}')
    break
  except ValueError:
    print('Podałeś błędne dane')
  finally:
    print('Koniec iteracji')
