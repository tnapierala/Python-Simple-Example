pracownik = {
        ' name ': ' Tomasz ',
        ' surname ' : 'Nowakowski ',
        ' city ' : ' Poznań ',
        ' age ' : ' 23 ' ,
        ' namesChildren ': [' Tomasz ' , ' Krystyna ' ],
        ' namesParent ': [' Paweł ' , ' Katarzyna ' ]
}

print(pracownik)
#print(pracownik['namesChildren'][0])

pracownik[' height '] = 180
pracownik[' weight '] = 180
print(pracownik)

key = 'age'
if key in pracownik:
    del pracownik[key]
    print(f'Klucz {key} został usunięty')
else:
    print(f'Klucz o nazwie {key} nie znaleziono w słowniku praconik]')

print(pracownik)

print(pracownik.values())
print(list(pracownik.values()))
print(pracownik.items())


for value in pracownik.values():
    print(value, end="")

print()

'''
Wyświetl za pomocą pętli for wartości i klucze słownika pracownik w formacie: klucz: wartość
wykorzystaj w pętli for funkję print do wyświetlenia danych

'''
print('\n\n\nKlucze i wartosci:\n')
for key, value in pracownik.items():
    print(key,':', value, ',\n', end="")
    

print('\n')


