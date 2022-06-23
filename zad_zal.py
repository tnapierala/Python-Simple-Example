'''
tworzymy menu

2 możliwości 

- kalk prosty dod, ode, możenie, dzielenie, modulo
- kalkulator liczb hex (dec na hex) lub odwrotnie

'''

uzytkownika = []
k=1
while k > 0:
    ile=0
    a=0
    b=0
    wynik=0
    podmenu=0
    wybor=0
    podmenu = 0
    podmenu2 = 0
    try:
        print("\nMenu:")
        print("\n 1. Kaltulator prosty ")
        print("\n 2. Kalkulator HEX to DEC or DEC to HEX") 
        
        wybor=int(input("\n Twój wybór: "))
        if wybor == 1:
        #kalk pros
            i=0
            while i < 1:
                try:
                    a=float(input("\n Wprowadź liczbę 1: "))                 
                    if  a >= 0:
                        print("\n Liczba a: " + str(a) )
                        i = 2                        
                    else:
                        print("\n\tZa mała liczba! Spróbuj ponownie..\n")
                        continue
                except ValueError:
                    print("\n\tTo nie jest liczba! Spróbuj ponownie... \n")
                    continue
            o=0
            while o < 1:
                try:
                    b=float(input("\n Wprowadź liczbę 2: "))                    
                    print("\n Liczba a: " + str(b)) 
                    o = 2                       
                except ValueError:
                    print("\n\tTo nie jest liczba! Spróbuj ponownie... \n")
                    continue

            print("\n\t Podmenu:")
            print("\n\t 1. Dodawanie")
            print("\n\t 2. Odejmowanie")
            print("\n\t 3. Dzielenie")
            print("\n\t 4. Mnożenie")
            print("\n\t 5. Modulo")
            p=0
            while p < 1:
                try:
                    podmenu=int(input("\n Wprowadź które podmenu wybierasz: "))                    
                    if podmenu == 1:
                        wynik = a+b
                        print( "Wynik to:" + str(a) + " + "+str(b) + " = " + str(wynik)) 
                        p=2                      
                    elif podmenu == 2:
                        wynik = a-b
                        print( "Wynik to:" + str(a) + " + "+str(b) + " = " + str(wynik))
                        p=2
                    elif podmenu == 3:
                        wynik = a*b
                        print( "Wynik to:" + str(a) + " + "+str(b) + " = " + str(wynik))
                        p=2
                    elif podmenu == 4:
                        wynik = a/b
                        print( "Wynik to:" + str(a) + " + "+str(b) + " = " + str(wynik))
                        p=2
                    elif podmenu == 5:
                        wynik = a%b
                        print( "Wynik to:" + str(a) + " + "+str(b) + " = " + str(wynik))               
                    else:
                        print("\n\t Zła liczba, nie wybrałeś podmenu! Spróbuj ponownie..\n")
                        continue
                except ValueError:
                    print("\n\tTo nie jest liczba! Spróbuj ponownie... \n")
                    continue
        #kalk hex dex
        elif wybor == 2:
            print("\n\t Podmenu:")
            print("\n\t 1. HEX to DEC")
            print("\n\t 2. DEC to HEX")
            l=0
            while l < 0: 
                try:
                    podmenu2=int(input("\n Wprowadź które podmenu wybierasz: ")) 
                    if podmenu2 == 1:
                        y=0
                        while y < 1:
                            try:
                                h = str(input("\n Wprowadź liczbę Hex: "))                 
                                print("\n Liczba a: " + str(h))
                                wynik1 = int(h, 16)                     
                            except ValueError:
                                print("\n\tTo nie jest liczba! Spróbuj ponownie... \n")
                                continue

                    elif podmenu2 == 2:
                        v=0
                        while v < 1:
                            try:
                                d = str(input("\n Wprowadź liczbę Hex: "))                 
                                print("\n Liczba a: " + str(d))
                                wynik1 = int(h, 16)          

                                def ChangeHex(d):
                                    if (d < 0):
                                        print(0)
                                    elif (d<=1):
                                        print(d)
                                    else:
                                        ChangeHex(d/16)
                                        x =(d%16)
                                        if (x < 10):
                                            print(x), 
                                        if (x == 10):
                                            print("A"),
                                        if (x == 11):
                                            print("B"),
                                        if (x == 12):
                                            print("C"),
                                        if (x == 13):
                                            print("D"),
                                        if (x == 14):
                                            print("E"),
                                        if (x == 15):
                                            print ("F"),
                            except ValueError:
                                print("\n\tTo nie jest liczba! Spróbuj ponownie... ")
                                continue 
                    else:
                        print("\n\t Zła liczba, nie wybrałeś podmenu! Spróbuj ponownie..\n")
                        continue
                except ValueError:
                    print("\n\tTo nie jest liczba! Spróbuj ponownie... ")
                    continue
        else:
            print("\n\tZła liczba! Spróbuj ponownie!")
            continue
    except ValueError:
        print("\n\tTo nie jest liczba! Spróbuj ponownie... ")
        continue
    
    print("\n Jeśli chcesz kontynuować to kliknij 1, jeśli nie to 0: ")

    x = 0
    while x < 1:
        try:
            k = int(input("\nTwój wybór: "))
            if k == 1 :
                k=1
                x = 2
            elif k == 0:
                k=0
                x=2
                print("\n Zakończyłeś program! Do zobaczenia :) \n")  
                break
            else:
                print("\n\t Podaj liczbę 1 jeśli 'TAK', lub 0 jeśli 'NIE'")
        except ValueError:
            print("\n\tTo nie jest liczba! Spróbuj ponownie... ")
            continue