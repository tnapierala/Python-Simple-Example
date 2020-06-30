# jedna gwiazdka --> jeśli nie wiesz ile argumentów będziesz podawał
def sum(*args):
  result=0
  for x in args:
    result += x
  return result

print(sum())
print(sum(2, 4))
print(sum(2, 4, 1, 22, -2, 33))

# =========================================
# dwie gwiazdki --> jeśli nie wiesz ile słów kluczowych zostanie przekazanych
def dict(**kwargs):
  for name, value in kwargs.items():
    print(f'{name} - {value}')

dict(name1 = 'Jan', name2 = 'Anna')

# =========================================
'''
Użytkownik podaje z klawiatury minimum trzy imiona
Wyświetl na ekranie dane w nastepujący sposób:

name1: ...
name2: ...
name3: ...
Pozostałe imiona: [...]
'''

def data(first, second, third, *others):
    print(f'Pierwszy {first}')
    print(f'Drugi {second}')
    print(f'Trzeci {third}')
    print(f'Pozostałe {list(others)}')

data('Jan', 'Anna', 'Karol', 'Tomasz', 'Krystyna')

# ==========================================

def show(first, second, third, **options):
  if options.get('action') == 'add':
    sum = first + second + third
    print(f'Suma wynosi: {sum}')

  if options.get('element') == 'first':
    return first

x = show(2, 3, 4, action='add', element='first')
print(f'Wynik: {x}')
    
