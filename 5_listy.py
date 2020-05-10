progr=['Python', 'PHP', 'C#', 'JS', 'Java']
print("progr")
print(type(progr))

first=progr[0]
print(first)

threeElements=progr[0:3]
print(threeElements)

last=progr[-1]
print(last)


#Dodanie nowego elementu na koniec listy
progr.append('R')
progr.append('Python')
print(progr)


#zaliczanie elementu w liście
countElement=progr.count('Python')
print(countElement)


#Ilość elementów w liście
countElementsOfList=len(progr)
print(countElementsOfList)


#Połączenie list
anotherList=['C', 'C++']
progr.extend(anotherList)
print('progr: ' + str(progr))
print('anotherLits: ' + str(anotherList))

#Usuwanie elementów z listy
new=progr
print('New list: ' + str(new))
new.clear()
print('New list: ' + str(new))
print('Rozmiar New list: ' + str(len(new)))
print('progr list: ' + str(progr))
print('Rozmiar progr list: ' +str(len(progr)))

x=8
print(x)
y=x
print(y)

y=5
print(x) #8
print(y) #5



