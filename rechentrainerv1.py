import random #das hauptmoul
from sys import exit as cya #sys.exit() als cya()
alwayson = False
status = False
def mainmenu():
    print("----Hauptmenü----")
    print("Dies bringt dir mathe bei!") #hab ich original für mich programmiert weil ich kein mathe kann. Was python nicht einen helfen kann
    print("1: Addition")
    print("2: Subtraktion")
    print("3: Multiplikation")
    print("4: Division")
    print("5: Beenden")
    print("6: Always on mode")
    while True:
        wahl = input("Wähle eine Option (1-6): ")
        try:
            wahl = int(wahl)
            break
        except ValueError:
            print("Bitte wähle eine gültige zahl")
    return(wahl) #gebe wahl zurück, diese  funktion müssen von einer hauptfunktion gerufen werden
def mainmencaller():
    while True:
        try:
            mm = mainmenu()
            if mm == 3:
                multiplikation()
            elif mm == 5:
                print("Bis bald!")
                cya()
            elif mm == 6:
                global alwayson
                global status
                if status == False:
                    alwayson = True
                    status = True
                    print("Alwayson ist jetzt an")
                else:
                    status = False
                    alwayson = False
                    print("Alwayson ist jetzt aus")
            elif mm == 1:
                addition()
            elif mm == 2:
                subtrahierung()
            elif mm == 4:
                division()
            else:
                print("Existiert nicht!")
        except KeyboardInterrupt:
            print("")
            print("Bis bald!")
            cya()
def multiplikation():
    print("Bitte wähle") #Hauptmenü, frage für zahl
    print("1: Grosses 1x1 (bis zu 100x100)")
    print("2: Kleines 1x1 (bis zu 10x10) [empfohlen]")
    print("3: Spezifische reihe")
    while True: #für try-except
        wahl = input("Wähle eine Option (1-3): ") #wahl
        try:
            wahl = int(wahl)
            break
        except ValueError: #falls ein troll einen buchstabe eingibt
            print("Bitte wähle eine gültige zahl")
    if wahl == 1: #grosses 1x1
        while True:

            n1 = random.randint(1, 100) #muss noch in einen while true loop, wahl von zufälligen zahlen
            n2 = random.randint(1, 100)
            korrekt = n1 * n2 #richtiges ergebnis
            try:

                ergebnis = input(f"{n1}x{n2}: ") #benutzer gewähltes ergebnis
                ergebnis = int(ergebnis)
                if ergebnis == korrekt:
                    print("Sehr gut!") #falls es richtig is :D
                    if alwayson == False:
                        try:
                            fortfahren = input("Enter um fortzufahren 1 um zurück zum menü zu gehen: ")
                            fortfahren = int(fortfahren)
                        except ValueError:
                            print("Bitte gebe eine zahl ein")
                        if fortfahren == 1:
                            mainmencaller()
                        else:
                            print("")
                    else:
                        print("")
                else:
                    print("Nicht so ganz, versuche es noch einmal") #awh, er kann genauso viel mathe wie ich D:
            except ValueError:
                print("Bitte gebe eine ZAHL ein") #sehr witzig mr troll
    elif wahl == 2: #kleines 1x1
        while True:
            n1 = random.randint(1,10) #muss noch in einen while true loop, wahl von zufälligen zahlen
            n2 = random.randint(1,10)
            korrekt = n1 * n2 #richtiges ergebnis
            try:

                ergebnis = input(f"{n1}x{n2}: ") #benutzer gewähltes ergebnis
                ergebnis = int(ergebnis)
                if ergebnis == korrekt:
                    print("Sehr gut!") #falls es richtig is :D
                    if alwayson == False:
                        try:
                            fortfahren = input("Enter um fortzufahren 1 um zurück zum menü zu gehen: ")
                            fortfahren = int(fortfahren)
                        except ValueError:
                            print("Bitte gebe eine zahl ein")
                        if fortfahren == 1:
                            mainmencaller()
                        else:
                            print("")
                    else:
                        print("")
                else:
                    print("Nicht so ganz, versuche es noch einmal") #awh, er kann genauso viel mathe wie ich D:
            except ValueError:
                print("Bitte gebe eine ZAHL ein") #sehr witzig mr troll
    elif wahl == 3:
         while True:
            try:
                reihe = input("Welche reihe soll gecheckt werden? Alles funktioniert: ")
                reihe = int(reihe)
                zahl2range = input(f"Bei der {reihe}er reihe, von welcher range soll x2 sein? (reihe * 1-X) [wenn unklar, analysiere zeile 117-128 im code manuell bitte untersuchen]: ")
                zahl2range = int(zahl2range)
                break
            except ValueError:
                print("Bitte gebe echte zahlen an")
         while True:
           
            n1 = reihe #muss noch in einen while true loop, wahl von zufälligen zahlen
            n2 = random.randint(1,zahl2range)
            korrekt = n1 * n2 #richtiges ergebnis
            try:

                ergebnis = input(f"{n1}x{n2}: ") #benutzer gewähltes ergebnis
                ergebnis = int(ergebnis)
                if ergebnis == korrekt:
                    print("Sehr gut!") #falls es richtig is :D
                    if alwayson == False:
                        try:
                            fortfahren = input("Enter um fortzufahren 1 um zurück zum menü zu gehen: ")
                            fortfahren = int(fortfahren)
                        except ValueError:
                            print("Bitte gebe eine zahl ein")
                        if fortfahren == 1:
                            mainmencaller()
                        else:
                            print("")
                    else:
                        print("")
                else:
                    print("Nicht so ganz, versuche es noch einmal") #awh, er kann genauso viel mathe wie ich D:
            except ValueError:
                print("Bitte gebe eine ZAHL ein") #sehr witzig mr troll
    else:
        print("Keine valide option")
def addition():
    print("Addition (+)")
    while True:
        try:
            zahl1 = input("von 1-x soll wie viel soll zahl 1 sein?: ")
            zahl1 = int(zahl1)
            zahl2 = input("von 1-x soll wie viel soll zahl 2 sein?: ")
            zahl2 = int(zahl2)
            break
        except ValueError:
            print("Bitte gebe eine valide zahl ein")
    while True:
        n1 = random.randint(1,zahl1)
        n2 = random.randint(1,zahl2)
        korrekt = n1 + n2
        while True:
                try:

                    ergebnis = input(f"{n1}+{n2}: ") #benutzer gewähltes ergebnis
                    ergebnis = int(ergebnis)
                    if ergebnis == korrekt:
                        print("Sehr gut!") #falls es richtig is :D
                        if alwayson == False:
                            try:
                                fortfahren = input("Enter um fortzufahren 1 um zurück zum menü zu gehen: ")
                                fortfahren = int(fortfahren)
                            except ValueError:
                                print("Bitte gebe eine zahl ein")
                            if fortfahren == 1:
                                mainmencaller()
                            else:
                                print("")
                        else:
                            print("")
                    else:
                        print("Nicht so ganz, versuche es noch einmal") #awh, er kann genauso viel mathe wie ich D:
                except ValueError:
                    print("Bitte gebe eine ZAHL ein")
           
def subtrahierung():
    print("Subtraktion (-)")
    while True:
        try:
            zahl1 = input("von 1-x soll wie viel soll zahl 1 sein?: ")
            zahl1 = int(zahl1)
            zahl2 = input("von 1-x soll wie viel soll zahl 2 sein?: ")
            zahl2 = int(zahl2)
            break
        except ValueError:
            print("Bitte gebe eine valide zahl ein")
    while True:
        n1 = random.randint(1,zahl1)
        n2 = random.randint(1,zahl2)
        korrekt = n1 - n2
        while True:
                try:

                    ergebnis = input(f"{n1}-{n2}: ") #benutzer gewähltes ergebnis
                    ergebnis = int(ergebnis)
                    if ergebnis == korrekt:
                        print("Sehr gut!") #falls es richtig is :D
                        if alwayson == False:
                            try:
                                fortfahren = input("Enter um fortzufahren 1 um zurück zum menü zu gehen: ")
                                fortfahren = int(fortfahren)
                            except ValueError:
                                print("Bitte gebe eine zahl ein")
                            if fortfahren == 1:
                                mainmencaller()
                            else:
                                print("")
                        else:
                            print("")
                    else:
                        print("Nicht so ganz, versuche es noch einmal") #awh, er kann genauso viel mathe wie ich D:
                except ValueError:
                    print("Bitte gebe eine ZAHL ein")
                    
def division():
    print("Division (:)")
    while True:
        try:
            zahl1 = input("von 1-x soll wie viel soll zahl 1 sein?: ")
            zahl1 = int(zahl1)
            zahl2 = input("von 1-x soll wie viel soll zahl 2 sein?: ")
            zahl2 = int(zahl2)
            break
        except ValueError:
            print("Bitte gebe eine valide zahl ein")
    while True:
        n1 = random.randint(1,zahl1)
        n2 = random.randint(1,zahl2)
        korrekt = n1 / n2
        while True:
                try:

                    ergebnis = input(f"{n1}/{n2}: ") #benutzer gewähltes ergebnis
                    ergebnis = float(ergebnis)
                    if ergebnis == korrekt:
                        print("Sehr gut!") #falls es richtig is :D
                        if alwayson == False:
                            try:
                                fortfahren = input("Enter um fortzufahren 1 um zurück zum menü zu gehen: ")
                                fortfahren = int(fortfahren)
                            except ValueError:
                                print("Bitte gebe eine zahl ein")
                            if fortfahren == 1:
                                mainmencaller()
                            else:
                                print("")
                        else:
                            print("")
                    else:
                        print("Nicht so ganz, versuche es noch einmal") #awh, er kann genauso viel mathe wie ich D:
                except ValueError:
                    print("Bitte gebe eine ZAHL ein")
        
mainmencaller() 