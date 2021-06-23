import random2
import os
from cfonts import render, say
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#* Wichtige Information zu den Kommentaren, da die Codes sehr identisch zu einander sind, kommt es zu Wiederholung der Kommentaren.*


# In diesem Abschnitt wird das Programm (Schiffe-Versenken) unsere große Überschrifft mit unseren Namen anzeigen.
# Hierbei wurden Schrifft und Schrifftfarbe angepasst.

output = render('Battleships',font='block',colors=['red','red'], align='center')
second = render('a game by zak,merve,sam', font='block',colors=['blue','white'], align='center')
print(output)
print(second)

time.sleep(5)
clear = lambda: os.system('cls') # Ein Timer, der die Überschrifft verschwinden lässt.
clear()

# Dieser Abschnitt des Codes ist das Menu. Auch hier wurde die Farbe des Textes verändert
# und die vier Optionen hinzugefügt mit den jeweiligen Optionen das Spiel entweder zu verlassen oder doch zu starten.
def mainMenu() :
    ok = 1
    while ok == 1:
       try:
        pvp = (f"{Fore.CYAN}Spieler vs. Spieler")
        pve = (f"{Fore.YELLOW}Spieler vs. Computer")
        info = (f"{Fore.GREEN}Anleitung")
        ext = (f"{Fore.MAGENTA}Exit")

        print("Ein Spiel von Zakaria, Merve & Sam ^^")
        print("\n1. " + pvp)
        print("2. " + pve)
        print("3. " + info)
        print("4. " + ext +"\n")

        eingabe = input("Zum Auswählen der Optionen bitte 1, 2 , 3 oder 4 drücken und mit Enter bestätigen.")
        int(eingabe)
        liste = [1,2,3, 4]
        if "1" in eingabe:
            print("Eingabe erfolgreich - es wurde " + pvp + " ausgewählt.")
            ok == 2
            break
        elif "2" in eingabe:
            print("Eingabe erfolgreich - es wurde " + pve + " ausgewählt.")
            ok == 2
            break
        elif "3" in eingabe:
            print("\nEingabe erfolgreich - es wurde " + info + " ausgewählt.")
            ok == 2
            break

        elif "4" in eingabe:
            print("\nEingabe erfolgreich - es wurde " + ext + " ausgewählt.")
            ok == 2
            break

        else:
            print("\nFehler - Bitte 1, 2, 3 oder 4 auswählen.")

       except:
            print("\nFehler - Bitte 1, 2, 3 oder 4 auswählen.")

    return eingabe

# Die Funktion def finale(check) fragt den Spieler, ob er tatsächlich das Programm ausführen möchte,
# in diesem Fall Player vs Player
def finale(check):
    try:
        if "1" == check:
            #pvp
            bestaetigung = input("Player vs. Player ausführen? [j/n]:")
            if bestaetigung == "j":
                clear = lambda: os.system('cls')
                clear()
                time.sleep(2)

                # Spieler1 Programmhälfte    Spieler1 Programmhälfte     Spieler1 Programmhälfte:

                def pruefung_auf_fehler_Spieler1(auswahl_position_Spieler1, bereits_ausgewaehlt_Spieler1):
                    auswahl_position_Spieler1.sort()
                    for i in range(len(auswahl_position_Spieler1)):
                        num = auswahl_position_Spieler1[i]
                        if num in bereits_ausgewaehlt_Spieler1:
                            auswahl_position_Spieler1 = [-1]
                            break
                        elif num < 0 or num > 99:
                            auswahl_position_Spieler1 = [-1]
                            break
                        elif num % 10 == 9 and i < len(auswahl_position_Spieler1) - 1:
                            if auswahl_position_Spieler1[i + 1] % 10 == 0:
                                auswahl_position_Spieler1 = [-1]
                                break
                        if i != 0:
                            if auswahl_position_Spieler1[i] != auswahl_position_Spieler1[i - 1] + 1 and \
                                    auswahl_position_Spieler1[i] != auswahl_position_Spieler1[i - 1] + 10:
                                auswahl_position_Spieler1 = [-1]
                                break
                    return auswahl_position_Spieler1

                # Diese Funktion kreiert für den Spieler 1 seine Spielfeld - ein Feld für die eigenen Schiffe.
                # Hierbei wurde mit Hilfe von If-Anweisungen darauf geachtet, dass es zu keiner doppelplatzierung
                # der Schiffe kommt oder gar zu einer falschen und nicht befindbaren Koordinate (z.B N8 oder Z2).

                def schiff_Spieler1_hinzufuegen(long, bereits_ausgewaehlt_Spieler1):

                    ok = True
                    while ok:
                        try:
                            print("          Schiffe Versenken    ")
                            print("              Spieler 1     ")
                            print("     Bitte plaziere deine Schiffe")
                            print("     A  B  C  D  E  F  G  H  I  J")

                            place1 = 0
                            for x in range(10):
                                row1 = ""
                                for y in range(10):
                                    cz = " _ "
                                    row1 = row1 + cz
                                    place1 = place1 + 1

                                print(x, " ", row1)
                            schiff_Spieler1 = []
                            # Fordert den Spieler auf eine Koordinate einzugeben.
                            print("Standpunkt von Schiff mit Länge ", long)
                            for i in range(long):
                                boat_num = input("Bitte Koordinate eingeben, wo sich dein Schiff befinden soll:")
                                if len(boat_num) != 2:
                                    print("\nFehler - Koordinate befindet sich nicht auf dem Feld.")
                                    print("...versuche stattdessen Bsp: A1, C8, G3\n")
                                else:
                                    eins = boat_num[0:1]
                                    # print(eins)
                                    zwei = boat_num[-1:]
                                    # print(zwei)

                                    if eins == "a" or eins == "A":
                                        abc = 0
                                    elif eins == "b" or eins == "B":
                                        abc = 1
                                    elif eins == "c" or eins == "C":
                                        abc = 2
                                    elif eins == "d" or eins == "D":
                                        abc = 3
                                    elif eins == "e" or eins == "E":
                                        abc = 4
                                    elif eins == "f" or eins == "F":
                                        abc = 5
                                    elif eins == "g" or eins == "G":
                                        abc = 6
                                    elif eins == "h" or eins == "H":
                                        abc = 7
                                    elif eins == "i" or eins == "I":
                                        abc = 8
                                    elif eins == "j" or eins == "J":
                                        abc = 9
                                    else:
                                        print("Falsche Koordinate! Bitte Koordinate innerhalb des Feldes wählen")

                                    xyz = int(zwei)
                                    xyz = (xyz * 10)
                                    boat_num = abc + xyz

                                schiff_Spieler1.append(int(boat_num))
                                # Prüft auf das Schiff
                            schiff_Spieler1 = pruefung_auf_fehler_Spieler1(schiff_Spieler1,
                                                                           bereits_ausgewaehlt_Spieler1)
                            if schiff_Spieler1[0] != -1:
                                bereits_ausgewaehlt_Spieler1 = bereits_ausgewaehlt_Spieler1 + schiff_Spieler1
                                print("...Schiff wurde plaziert")
                                print()
                                print()
                                break
                            else:
                                print("Fehler - Platziertes Schiff überschneidet sich möglicherweise")
                        except:
                            print("        Bitte erneut eingeben")
                            print()
                    return schiff_Spieler1, bereits_ausgewaehlt_Spieler1

                def schiffe_bauen_Spieler1(bereits_ausgewaehlt_Spieler1, anzahl_schiffe_Spieler1):
                    schiffe_Spieler1 = []
                    # auswahl_schiffe_spieler1 = [5,4,3,3,2,2]

                    for auswahl_schiff_Spieler1 in anzahl_schiffe_Spieler1:
                        schiff_Spieler1, bereits_ausgewaehlt_Spieler1 = schiff_Spieler1_hinzufuegen(
                            auswahl_schiff_Spieler1, bereits_ausgewaehlt_Spieler1)
                        schiffe_Spieler1.append(schiff_Spieler1)

                    return schiffe_Spieler1, bereits_ausgewaehlt_Spieler1

                # Die folgende Funktion zeigt dem Spieler 1 sein Spielfeld mit den platzierten Schiffen.

                def show_board_c_Spieler1(bereits_ausgewaehlt_Spieler1):
                    print("               Spieler 1")
                    print("Hier sind deine Schiffe in einer Übersicht")
                    print("     A  B  C  D  E  F  G  H  I  J")

                    place = 0
                    for x in range(10):
                        row = ""
                        for y in range(10):
                            ch = " _ "
                            if place in bereits_ausgewaehlt_Spieler1:
                                ch = " o "
                            row = row + ch
                            place = place + 1

                        print(x, " ", row)

                def show_board_Spieler1(hit_AufSpieler2, miss_AufSpieler2, complete_AufSpieler2):
                    schiffe_uebrig = 6
                    print("          Schiffe Versenken    ")
                    print("               Spieler 1")
                    print("     A  B  C  D  E  F  G  H  I  J")

                    place = 0
                    for x in range(10):
                        row = ""
                        for y in range(10):
                            ch = " _ "
                            if place in miss_AufSpieler2:
                                ch = " x "
                            elif place in hit_AufSpieler2:
                                ch = " o "
                            elif place in complete_AufSpieler2:
                                ch = " O "
                                schiffe_uebrig -= 1
                            row = row + ch
                            place = place + 1
                        print(x, " ", row)
                    print("Spieler 2 hat noch " + str(schiffe_uebrig) + " Schiffe übrig.\n")

                # Mit dieser Funktion (Methode) wird der Spieler 1 aufgefordet auf die Koordinaten,
                # auf die als erstes geschossen werden sollen.
                def schuss_VonSpieler1_AufSpieler2(zuvorGeschosseneSchuesse_Spieler1):


                    ok = "n"
                    while ok == "n":
                        try:
                            print("Spieler 1 ist am Zug")
                            anfrage = input("Bitte gebe dein Ziel ein: ")
                            print("Befehl zum Angriff auf folgendes Ziel: " + ">" + anfrage + "<")

                            if len(anfrage) != 2:
                                print("\nFehler! Koordinate befindet sich nicht auf dem Feld.")
                                print("...versuchen Sie stattdessen Bsp: A1, C8, G3\n")
                            else:
                                print("Ziel anvisiert!")
                                eins = anfrage[0:1]
                                # print(eins)
                                zwei = anfrage[-1:]
                                # print(zwei)

                                if eins == "a" or eins == "A":
                                    abc = 0
                                elif eins == "b" or eins == "B":
                                    abc = 1
                                elif eins == "c" or eins == "C":
                                    abc = 2
                                elif eins == "d" or eins == "D":
                                    abc = 3
                                elif eins == "e" or eins == "E":
                                    abc = 4
                                elif eins == "f" or eins == "F":
                                    abc = 5
                                elif eins == "g" or eins == "G":
                                    abc = 6
                                elif eins == "h" or eins == "H":
                                    abc = 7
                                elif eins == "i" or eins == "I":
                                    abc = 8
                                elif eins == "j" or eins == "J":
                                    abc = 9
                                else:
                                    print("Falsche Koordinate! Bitte Koordinate innerhalb des Feldes wählen")

                                xyz = int(zwei)
                                xyz = (xyz * 10)
                                schuss_VonSpieler1 = abc + xyz

                                if schuss_VonSpieler1 not in zuvorGeschosseneSchuesse_Spieler1:
                                    # print(shot)
                                    print("FEUERFREI!!!\n")
                                    ok = "y"
                                    break

                                else:
                                    print("Ziel wurde bereits beschossen, bitte wähle ein anderes.")

                        except:
                            print("Falsche Koordinaten eingegeben, bitte erneut versuchen")

                    return schuss_VonSpieler1
                # Um das Spiel korrekt spielen zu können, wird mit dieser Funktion (Methode) darauf geprüft,
                # ob es zu einem Miss oder Hit kam.
                def pruefung_schuss_VonSpieler1(schuss_VonSpieler1, schiffe_spieler2, hit_AufSpieler2, miss_AufSpieler2,
                                                complete_AufSpieler2):
                    missed_AufSpieler2 = 0
                    for i in range(len(schiffe_spieler2)):
                        if schuss_VonSpieler1 in schiffe_spieler2[i]:
                            schiffe_spieler2[i].remove(schuss_VonSpieler1)
                            if len(schiffe_spieler2[i]) > 0:
                                hit_AufSpieler2.append(schuss_VonSpieler1)
                                missed_AufSpieler2 = 1
                            else:
                                complete_AufSpieler2.append(schuss_VonSpieler1)
                                missed_AufSpieler2 = 2
                    if missed_AufSpieler2 == 0:
                        miss_AufSpieler2.append(schuss_VonSpieler1)

                    return schiffe_Spieler2, hit_AufSpieler2, miss_AufSpieler2, complete_AufSpieler2

                # Spieler2 Programmhälfte    Spieler2 Programmhälfte     Spieler2 Programmhälfte:

                def pruefung_auf_fehler_Spieler2(auswahl_position_Spieler2, bereits_ausgewaehlt_Spieler2):
                    auswahl_position_Spieler2.sort()
                    for i in range(len(auswahl_position_Spieler2)):
                        num = auswahl_position_Spieler2[i]
                        if num in bereits_ausgewaehlt_Spieler2:
                            auswahl_position_Spieler2 = [-1]
                            break
                        elif num < 0 or num > 99:
                            auswahl_position_Spieler2 = [-1]
                            break
                        elif num % 10 == 9 and i < len(auswahl_position_Spieler2) - 1:
                            if auswahl_position_Spieler2[i + 1] % 10 == 0:
                                auswahl_position_Spieler2 = [-1]
                                break
                        if i != 0:
                            if auswahl_position_Spieler2[i] != auswahl_position_Spieler2[i - 1] + 1 and \
                                    auswahl_position_Spieler2[i] != auswahl_position_Spieler2[i - 1] + 10:
                                auswahl_position_Spieler2 = [-1]
                                break
                    return auswahl_position_Spieler2

                # In dieser Methode(Funktion) soll der Spieler 2 seine Schiffe bauen.
                def schiff_Spieler2_hinzufuegen(long, bereits_ausgewaehlt_Spieler2):

                    ok = True
                    while ok:
                        try:
                            print("          Schiffe Versenken    ")
                            print("              Spieler 2     ")
                            print("     Bitte plaziere deine Schiffe")
                            print("     A  B  C  D  E  F  G  H  I  J")

                            place1 = 0
                            for x in range(10):
                                row1 = ""
                                for y in range(10):
                                    cz = " _ "
                                    row1 = row1 + cz
                                    place1 = place1 + 1

                                print(x, " ", row1)
                            schiff_Spieler2 = []
                            # ask the user to enter numbers
                            print("Standpunkt von Schiff mit Länge ", long)
                            for i in range(long):
                                boat_num = input("Bitte Koordinate eingeben, wo sich dein Schiff befinden soll:")
                                if len(boat_num) != 2:
                                    print("\nFehler - Koordinate befindet sich nicht auf dem Feld.")
                                    print("...versuche stattdessen bspw: A1, C8, G3\n")
                                else:
                                    eins = boat_num[0:1]
                                    # print(eins)
                                    zwei = boat_num[-1:]
                                    # print(zwei)

                                    if eins == "a" or eins == "A":
                                        abc = 0
                                    elif eins == "b" or eins == "B":
                                        abc = 1
                                    elif eins == "c" or eins == "C":
                                        abc = 2
                                    elif eins == "d" or eins == "D":
                                        abc = 3
                                    elif eins == "e" or eins == "E":
                                        abc = 4
                                    elif eins == "f" or eins == "F":
                                        abc = 5
                                    elif eins == "g" or eins == "G":
                                        abc = 6
                                    elif eins == "h" or eins == "H":
                                        abc = 7
                                    elif eins == "i" or eins == "I":
                                        abc = 8
                                    elif eins == "j" or eins == "J":
                                        abc = 9
                                    else:
                                        print("Falsche Koordinate! Bitte Koordinate innerhalb des Feldes wählen")

                                    xyz = int(zwei)
                                    xyz = (xyz * 10)
                                    boat_num = abc + xyz

                                schiff_Spieler2.append(int(boat_num))

                            schiff_Spieler2 = pruefung_auf_fehler_Spieler2(schiff_Spieler2,
                                                                           bereits_ausgewaehlt_Spieler2)
                            if schiff_Spieler2[0] != -1:
                                bereits_ausgewaehlt_Spieler2 = bereits_ausgewaehlt_Spieler2 + schiff_Spieler2
                                print("...Schiff wurde plaziert")
                                print()
                                print()
                                break
                            else:
                                print("Fehler - Platziertes Schiff überschneidet sich möglicherweise")
                        except:
                            print("        Bitte erneut eingeben")
                            print()
                    return schiff_Spieler2, bereits_ausgewaehlt_Spieler2


                def schiffe_bauen_Spieler2(bereits_ausgewaehlt_Spieler2, anzahl_schiffe_Spieler2):
                    schiffe_Spieler2 = []
                    # auswahl_schiffe_spieler1 = [5,4,3,3,2,2]

                    for auswahl_schiff_Spieler2 in anzahl_schiffe_Spieler2:
                        schiff_Spieler2, bereits_ausgewaehlt_Spieler2 = schiff_Spieler2_hinzufuegen(
                            auswahl_schiff_Spieler2, bereits_ausgewaehlt_Spieler2)
                        schiffe_Spieler2.append(schiff_Spieler2)

                    return schiffe_Spieler2, bereits_ausgewaehlt_Spieler2

                # Diese Funktion zeigt nun das Spielfeld für Spieler 2.

                def show_board_c_Spieler2(bereits_ausgewaehlt_Spieler2):
                    print("               Spieler 2")
                    print("Hier sind deine Schiffe in einer Übersicht")
                    print("     A  B  C  D  E  F  G  H  I  J")

                    place = 0
                    for x in range(10):
                        row = ""
                        for y in range(10):
                            ch = " _ "
                            if place in bereits_ausgewaehlt_Spieler2:
                                ch = " o "
                            row = row + ch
                            place = place + 1

                        print(x, " ", row)

                    # Funktion show_board_Spieler2 gibt am Schlüss hit oder miss an. Tifft der Spieler, erscheint ein "o".
                    # Versenkt der Spieler ein Schiff, erscheint ein „0“.
                    # Trifft der Spieler nichts, erscheint ein „x“.
                def show_board_Spieler2(hit_AufSpieler1, miss_AufSpieler1, complete_AufSpieler1):
                    schiffe_uebrig_S1 = 6
                    print("          Schiffe Versenken    ")
                    print("              Spieler 2    ")
                    print("     A  B  C  D  E  F  G  H  I  J")

                    place = 0
                    for x in range(10):
                        row = ""
                        for y in range(10):
                            ch = " _ "
                            if place in miss_AufSpieler1:
                                ch = " x "
                            elif place in hit_AufSpieler1:
                                ch = " o "
                            elif place in complete_AufSpieler1:
                                ch = " O "
                                schiffe_uebrig_S1 -= 1
                            row = row + ch
                            place = place + 1
                        print(x, " ", row)
                    print("Spieler 1 hat noch " + str(schiffe_uebrig_S1) + " Schiffe übrig.\n")

                    # Nun wird Spieler 2 aufgefordet koordinaten zu wählen, um Schiffe von Spieler 1 zu treffen.
                def schuss_VonSpieler2_AufSpieler1(zuvorGeschosseneSchuesse_Spieler2):

                    ok = "n"
                    while ok == "n":
                        try:
                            print("Spieler 2 ist am Zug")
                            anfrage = input("Bitte gebe dein Ziel ein: ")
                            print("Befehl zum Angriff auf folgendes Ziel: " + ">" + anfrage + "<")

                            if len(anfrage) != 2:
                                print("\nFehler - Koordinate befindet sich nicht auf dem Feld.")
                                print("...versuche stattdessen bspw: A1, C8, G3\n")
                            else:
                                print("Ziel anvisiert!")
                                eins = anfrage[0:1]
                                # print(eins)
                                zwei = anfrage[-1:]
                                # print(zwei)

                                if eins == "a" or eins == "A":
                                    abc = 0
                                elif eins == "b" or eins == "B":
                                    abc = 1
                                elif eins == "c" or eins == "C":
                                    abc = 2
                                elif eins == "d" or eins == "D":
                                    abc = 3
                                elif eins == "e" or eins == "E":
                                    abc = 4
                                elif eins == "f" or eins == "F":
                                    abc = 5
                                elif eins == "g" or eins == "G":
                                    abc = 6
                                elif eins == "h" or eins == "H":
                                    abc = 7
                                elif eins == "i" or eins == "I":
                                    abc = 8
                                elif eins == "j" or eins == "J":
                                    abc = 9
                                else:
                                    print("Falsche Koordinate! Bitte Koordinate innerhalb des Feldes wählen")

                                xyz = int(zwei)
                                xyz = (xyz * 10)
                                schuss_VonSpieler2 = abc + xyz

                                if schuss_VonSpieler2 not in zuvorGeschosseneSchuesse_Spieler2:
                                    # print(shot)
                                    print("FEUERFREI!!!\n")
                                    ok = "y"
                                    break

                                else:
                                    print("Ziel wurde bereits beschossen, bitte wähle ein anderes.")

                        except:
                            print("Falsche Koordinaten eingegeben, bitte erneut versuchen")

                    return schuss_VonSpieler2

                # Prüft die Schüsse von Spieler 2 auf mit If- Anweisungen.

                def pruefung_schuss_VonSpieler2(schuss_VonSpieler2, schiffe_Spieler1, hit_AufSpieler1, miss_AufSpieler1,
                                                complete_AufSpieler1):
                    missed_AufSpieler1 = 0
                    for i in range(len(schiffe_Spieler1)):
                        if schuss_VonSpieler2 in schiffe_Spieler1[i]:
                            schiffe_Spieler1[i].remove(schuss_VonSpieler2)
                            if len(schiffe_Spieler1[i]) > 0:
                                hit_AufSpieler1.append(schuss_VonSpieler2)
                                missed_AufSpieler1 = 1
                            else:
                                complete_AufSpieler1.append(schuss_VonSpieler2)
                                missed_AufSpieler1 = 2
                    if missed_AufSpieler1 == 0:
                        miss_AufSpieler1.append(schuss_VonSpieler2)

                    return schiffe_Spieler1, hit_AufSpieler1, miss_AufSpieler1, complete_AufSpieler1

                # Abteilung für die Auführung der Methoden - Reihenfolge beachten!
                # Im Anschluss des Codes erscheint ein Text, der den Spieler erwähnt der gewinnt.

                def check_if_empty_Spieler(list_of_lists):
                    return all([not elem for elem in list_of_lists])

                hit_AufSpieler2 = []
                miss_AufSpieler2 = []
                complete_AufSpieler2 = []
                zuvorGeschosseneSchuesse_Spieler1 = []
                missed_AufSpieler2 = 0
                bereits_ausgewaehlt_Spieler1 = []

                hit_AufSpieler1 = []
                miss_AufSpieler1 = []
                complete_AufSpieler1 = []
                zuvorGeschosseneSchuesse_Spieler2 = []
                missed_AufSpieler1 = 0
                bereits_ausgewaehlt_Spieler2 = []


                battleships = [5, 4, 3, 3, 2, 2]  # Gibt die Flotten größe und größe jedes einzelnen Schiffes wieder

                schiffe_Spieler1, bereits_ausgewaehlt_Spieler1 = schiffe_bauen_Spieler1(bereits_ausgewaehlt_Spieler1,
                                                                                        battleships)  # spieler1, schiffe bauen
                show_board_c_Spieler1(bereits_ausgewaehlt_Spieler1)  # spieler1, gebaute schiffe anzeigen
                time.sleep(6)
                clear()
                schiffe_Spieler2, bereits_ausgewaehlt_Spieler2 = schiffe_bauen_Spieler2(bereits_ausgewaehlt_Spieler2,
                                                                                        battleships)  # spieler2, schiffe bauen
                show_board_c_Spieler2(bereits_ausgewaehlt_Spieler2)  # spieler2, gebaute schiffe anzeigen
                time.sleep(6)
                clear()

                # loop
                for i in range(100):
                    # guesses
                    zuvorGeschosseneSchuesse_Spieler1 = hit_AufSpieler2 + miss_AufSpieler2 + complete_AufSpieler2
                    # shot
                    schuss_VonSpieler1 = schuss_VonSpieler1_AufSpieler2(zuvorGeschosseneSchuesse_Spieler1)
                    # check_shot
                    schiffe_Spieler2, hit_AufSpieler2, miss_AufSpieler2, complete_AufSpieler2 = pruefung_schuss_VonSpieler1(
                        schuss_VonSpieler1, schiffe_Spieler2, hit_AufSpieler2, miss_AufSpieler2, complete_AufSpieler2)
                    # show_board
                    show_board_Spieler1(hit_AufSpieler2, miss_AufSpieler2, complete_AufSpieler2)
                    # repeat until ships empty
                    if check_if_empty_Spieler(schiffe_Spieler2):
                        # print("end of game - winner in", i)
                        clear = lambda: os.system('cls')  # Lässt die Überschrifft verschwinden
                        clear()
                        time.sleep(2)
                        fourh = render('Spieler 1', font='block', colors=['red', 'white'],
                                       align='center')
                        third = render('DU HAST GEWONNEN!', font='block', colors=['blue', 'white'],
                                       align='center')
                        print(third)
                        print("                 IN", i, "ZÜGEN GEWONNEN")
                        time.sleep(9)
                        # clear = lambda: os.system('cls')  # Lässt die Überschrifft verschwinden
                        clear()

                        break

                    # guesses Spieler2
                    zuvorGeschosseneSchuesse_Spieler2 = hit_AufSpieler1 + miss_AufSpieler1 + complete_AufSpieler1
                    # shot Spieler 2
                    schuss_VonSpieler2 = schuss_VonSpieler2_AufSpieler1(zuvorGeschosseneSchuesse_Spieler2)
                    # check_shot Spieler2
                    schiffe_Spieler1, hit_AufSpieler1, miss_AufSpieler1, complete_AufSpieler1 = pruefung_schuss_VonSpieler2(
                        schuss_VonSpieler2, schiffe_Spieler1, hit_AufSpieler1, miss_AufSpieler1, complete_AufSpieler1)
                    # show_board Spieler2
                    show_board_Spieler2(hit_AufSpieler1, miss_AufSpieler1, complete_AufSpieler1)
                    # repeat until ships empty Spieler2
                    if check_if_empty_Spieler(schiffe_Spieler1):
                        # print("end of game - winner in", i)
                        clear = lambda: os.system('cls')  # killt die ueberschrift
                        clear()
                        time.sleep(2)
                        fourh = render('Spieler 2', font='block', colors=['red', 'white'],
                                       align='center')
                        third = render('SPIELER 2 - DU HAST GEWONNEN!', font='block', colors=['blue', 'white'],
                                       align='center')
                        print(third)
                        print("                 IN", i, "ZÜGEN GEWONNEN")
                        time.sleep(9)
                        # clear = lambda: os.system('cls')  # killt die ueberschrift
                        clear()
                        break
                print("fertig")
                bs = "n"

            elif bestaetigung == "n":
                bs = "n"

            elif bestaetigung != "j" or bestaetigung != "n":
                print("Bitte nur j für ja und n für nein bestätigen.\n")
                bs = "n"

        elif "2" == check:
            #info
            bestaetigung = input(" Player vs. Computer ausführen? [j/n]:")
            if bestaetigung == "j":
                time.sleep(2)
                clear = lambda: os.system('cls')
                clear()

                def pruefung_auf_fehler(auswahl_position, bereits_ausgewaehlt):
                    auswahl_position.sort()
                    for i in range(len(auswahl_position)):
                        num = auswahl_position[i]
                        if num in bereits_ausgewaehlt:
                            auswahl_position = [-1]
                            break
                        elif num < 0 or num > 99:
                            auswahl_position = [-1]
                            break
                        elif num % 10 == 9 and i < len(auswahl_position) - 1:
                            if auswahl_position[i + 1] % 10 == 0:
                                auswahl_position = [-1]
                                break
                        if i != 0:
                            if auswahl_position[i] != auswahl_position[i - 1] + 1 and auswahl_position[i] != \
                                    auswahl_position[i - 1] + 10:
                                auswahl_position = [-1]
                                break

                    return auswahl_position

                def schiff_hinzufuegen(long, bereits_ausgewaehlt):

                    ok = True
                    while ok:
                        try:
                            print("          Schiffe Versenken   ")
                            print("     A  B  C  D  E  F  G  H  I  J")

                            place1 = 0
                            for x in range(10):
                                row1 = ""
                                for y in range(10):
                                    cz = " _ "
                                    row1 = row1 + cz
                                    place1 = place1 + 1

                                print(x, " ", row1)
                            schiff = []
                            # ask the user to enter numbers
                            print("Standpunkt von Schiff mit Länge ", long)
                            for i in range(long):
                                boat_num = input("Bitte Koordinate eingeben, wo sich dein Schiff befinden soll:")
                                if len(boat_num) != 2:
                                    print("\nFehler - Koordinate befindet sich nicht auf dem Feld.")
                                    print("...versuche stattdessen bspw: A1, C8, G3\n")
                                else:
                                    eins = boat_num[0:1]
                                    # print(eins)
                                    zwei = boat_num[-1:]
                                    # print(zwei)

                                    if eins == "a" or eins == "A":
                                        abc = 0
                                    elif eins == "b" or eins == "B":
                                        abc = 1
                                    elif eins == "c" or eins == "C":
                                        abc = 2
                                    elif eins == "d" or eins == "D":
                                        abc = 3
                                    elif eins == "e" or eins == "E":
                                        abc = 4
                                    elif eins == "f" or eins == "F":
                                        abc = 5
                                    elif eins == "g" or eins == "G":
                                        abc = 6
                                    elif eins == "h" or eins == "H":
                                        abc = 7
                                    elif eins == "i" or eins == "I":
                                        abc = 8
                                    elif eins == "j" or eins == "J":
                                        abc = 9
                                    else:
                                        print("Falsche Koordinate! Bitte Koordinate innerhalb des Feldes wählen")

                                    xyz = int(zwei)
                                    xyz = (xyz * 10)
                                    boat_num = abc + xyz

                                schiff.append(int(boat_num))
                                # check that ship
                            schiff = pruefung_auf_fehler(schiff, bereits_ausgewaehlt)
                            if schiff[0] != -1:
                                bereits_ausgewaehlt = bereits_ausgewaehlt + schiff
                                print("...Schiff wurde plaziert")
                                print()
                                print()
                                break
                            else:
                                print("Fehler - Platziertes Schiff überschneidet sich möglicherweise")
                        except:
                            print("        Bitte erneut eingeben")
                            print()
                    return schiff, bereits_ausgewaehlt

                def schiffe_bauen(bereits_ausgewaehlt, anzahl_schiffe):
                    schiffe = []
                    # schiffe = [5,4,3,3,2,2]

                    for auswahl_schiff in anzahl_schiffe:
                        schiff, bereits_ausgewaehlt = schiff_hinzufuegen(auswahl_schiff, bereits_ausgewaehlt)
                        schiffe.append(schiff)

                    return schiffe, bereits_ausgewaehlt

                def pruefung_boat_comp(b, start, richt, bereits_ausgewaehlt):
                    boat = []
                    if richt == 1:
                        for i in range(b):
                            boat.append(start - i * 10)
                    elif richt == 2:
                        for i in range(b):
                            boat.append(start + i)
                    elif richt == 3:
                        for i in range(b):
                            boat.append(start + i * 10)
                    elif richt == 4:
                        for i in range(b):
                            boat.append(start - i)
                    boat = pruefung_auf_fehler(boat, bereits_ausgewaehlt)
                    return boat

                def boate_bauen(bereits_ausgewaehlt, anzahl_schiffe):
                    schiffe = []
                    # anzahl_schiffe = [5,4,3,3,2,2]
                    for b in anzahl_schiffe:
                        boat = [-1]
                        while boat[0] == -1:
                            auswahl_schiff_start = random2.randrange(99)
                            auswahl_schiff_richt = random2.randrange(1, 4)
                            # print(b,boat_start,boat_direction)
                            boat = pruefung_boat_comp(b, auswahl_schiff_start, auswahl_schiff_richt,
                                                      bereits_ausgewaehlt)
                        schiffe.append(boat)
                        bereits_ausgewaehlt = bereits_ausgewaehlt + boat
                        # print(schiffe)

                    return schiffe, bereits_ausgewaehlt

                def show_board_c(bereits_ausgewaehlt):
                    print("          Schiffe Versenken   ")
                    print("Hier sind deine Schiffe in einer Übersicht")
                    print()
                    print("     A  B  C  D  E  F  G  H  I  J")

                    place = 0
                    for x in range(10):
                        row = ""
                        for y in range(10):
                            ch = " _ "
                            if place in bereits_ausgewaehlt:
                                ch = " o "
                            row = row + ch
                            place = place + 1

                        print(x, " ", row)

                def schuss_VonComputer(zuvorGeschosseneSchuesse, taktik):
                    ok = "n"
                    while ok == "n":
                        try:
                            if len(taktik) > 0:
                                schuss = taktik[0]
                            else:
                                schuss = random2.randrange(99)
                            if schuss not in zuvorGeschosseneSchuesse:
                                ok = "y"
                                zuvorGeschosseneSchuesse.append(schuss)
                                break
                        except:
                            print("Fehler - Bitte erneut versuchen")

                    return schuss, zuvorGeschosseneSchuesse

                def show_board_Spieler(hit, miss, comp):
                    schiffe_uebrig = 6
                    print("          Schiffe Versenken   ")
                    print("               Spieler")
                    print("     A  B  C  D  E  F  G  H  I  J")

                    place = 0
                    for x in range(10):
                        row = ""
                        for y in range(10):
                            ch = " _ "
                            if place in miss:
                                ch = " x "
                            elif place in hit:
                                ch = " o "
                            elif place in comp:
                                ch = " O "
                                schiffe_uebrig -= 1
                            row = row + ch
                            place = place + 1

                        print(x, " ", row)

                    print("Computer hat noch " + str(schiffe_uebrig) + " Schiffe übrig.\n")

                    # Funktion show_board_Computer gibt am Schlüss hit oder miss an. Tifft der Spieler, erscheint ein "o".
                    # Versenkt der Spieler ein Schiff, erscheint ein „0“.
                    # Trifft der Spieler nichts, erscheint ein „x“.

                def show_board_Computer(hit, miss, comp):
                    schiffe_uebrig = 6
                    print("          Schiffe Versenken   ")
                    print("               Computer")
                    print("     A  B  C  D  E  F  G  H  I  J")

                    place = 0
                    for x in range(10):
                        row = ""
                        for y in range(10):
                            ch = " _ "
                            if place in miss:
                                ch = " x "
                            elif place in hit:
                                ch = " o "
                            elif place in comp:
                                ch = " O "
                                schiffe_uebrig -= 1
                            row = row + ch
                            place = place + 1

                        print(x, " ", row)

                    print("Spieler hat noch " + str(schiffe_uebrig) + " Schiffe übrig.\n")

                    # Prüft die Schüsse, ob getroffen oder nicht.
                def pruefung_schuss(schuss, schiffe, hit, miss, comp):
                    missed = 0
                    for i in range(len(schiffe)):
                        if schuss in schiffe[i]:
                            schiffe[i].remove(schuss)
                            if len(schiffe[i]) > 0:
                                hit.append(schuss)
                                missed = 1
                            else:
                                comp.append(schuss)
                                missed = 2
                    if missed == 0:
                        miss.append(schuss)

                    return schiffe, hit, miss, comp, missed

                def taktik_strategie(schuss, taktik, zuvorGeschosseneSchuesse, hit):
                    temp = []
                    if len(taktik) < 1:
                        temp = [schuss - 1, schuss + 1, schuss - 10, schuss + 10]
                    else:
                        if schuss - 1 in hit:
                            temp = [schuss + 1]
                            for num in [2, 3, 4, 5, 6, 7, 8]:
                                if schuss - num not in hit:
                                    temp.append(schuss - num)
                                    break
                        elif schuss + 1 in hit:
                            temp = [schuss - 1]
                            for num in [2, 3, 4, 5, 6, 7, 8]:
                                if schuss + num not in hit:
                                    temp.append(schuss + num)
                                    break
                        if schuss - 10 in hit:
                            temp = [schuss + 10]
                            for num in [20, 30, 40, 50, 60, 70, 80]:
                                if schuss - num not in hit:
                                    temp.append(schuss - num)
                                    break
                        elif schuss + 10 in hit:
                            temp = [schuss - 10]
                            for num in [20, 30, 40, 50, 60, 70, 80]:
                                if schuss + num not in hit:
                                    temp.append(schuss + num)
                                    break
                    # erweiterte Strategie
                    erws = []
                    for i in range(len(temp)):
                        if temp[i] not in zuvorGeschosseneSchuesse and temp[i] < 100 and temp[i] > -1:
                            erws.append(temp[i])
                    random2.shuffle(erws)

                    return erws

                # Funktion def schuss_VonSpieler fordert dem Spieler ein Ziel anzugeben, falls die angegebene Koordinate falsch ist
                # so wird der Spieler aufgefordert eine andere Koordinate zu wählen.
                def schuss_VonSpieler(zuvorGeschosseneSchuesse):

                    ok = "n"
                    while ok == "n":
                        try:
                            print("Spieler - Du bist am Zug.")
                            anfrage = input("Bitte gebe dein Ziel ein: ")
                            print("Befehl zum Angriff auf folgendes Ziel: " + ">" + anfrage + "<")

                            if len(anfrage) != 2:
                                print("\nFehler - Koordinate befindet sich nicht auf dem Feld.")
                                print("...versuche stattdessen bspw: A1, C8, G3\n")
                            else:
                                print("Ziel anvisiert!")
                                eins = anfrage[0:1]
                                # print(eins)
                                zwei = anfrage[-1:]
                                # print(zwei)

                                if eins == "a" or eins == "A":
                                    abc = 0
                                elif eins == "b" or eins == "B":
                                    abc = 1
                                elif eins == "c" or eins == "C":
                                    abc = 2
                                elif eins == "d" or eins == "D":
                                    abc = 3
                                elif eins == "e" or eins == "E":
                                    abc = 4
                                elif eins == "f" or eins == "F":
                                    abc = 5
                                elif eins == "g" or eins == "G":
                                    abc = 6
                                elif eins == "h" or eins == "H":
                                    abc = 7
                                elif eins == "i" or eins == "I":
                                    abc = 8
                                elif eins == "j" or eins == "J":
                                    abc = 9
                                else:
                                    print("Falsche Koordinate! Bitte Koordinate innerhalb des Feldes wählen")

                                xyz = int(zwei)
                                xyz = (xyz * 10)
                                schuss = abc + xyz

                                if schuss not in zuvorGeschosseneSchuesse:
                                    # print(shot)
                                    print("FEUERFREI!!!\n")
                                    ok = "y"
                                    break

                                else:
                                    print("Ziel wurde bereits beschossen, bitte wähle ein anderes.")

                        except:
                            print("Falsche Koordinaten eingegeben, bitte erneut versuchen")

                    return schuss

                def check_if_empty_game(list_of_lists):
                    return all([not elem for elem in list_of_lists])

                # vor dem Spiel
                hit1 = []
                miss1 = []
                comp1 = []
                zuvorGeschosseneSchuesse1 = []
                missed1 = 0
                taktik1 = []
                bereits_ausgewaehlt1 = []

                bereits_ausgewaehlt2 = []
                hit2 = []
                miss2 = []
                comp2 = []
                zuvorGeschosseneSchuesse2 = []
                missed2 = 0
                taktik2 = []

                battleships = [5, 4, 3, 3, 2, 2]
                # anzahl der schiffe im Spiel
                # computer erstellt ein Spielfeld für Spieler 1
                schiffe1, bereits_ausgewaehlt1 = boate_bauen(bereits_ausgewaehlt1, battleships)
                # Spieler erstellt ein Spielfeld für Spieler 2
                schiffe2, bereits_ausgewaehlt2 = schiffe_bauen(bereits_ausgewaehlt2, battleships)
                show_board_c(bereits_ausgewaehlt2)

                # loop
                for i in range(100):

                    # Spieler schießt
                    zuvorGeschosseneSchuesse1 = hit1 + miss1 + comp1
                    schuss1 = schuss_VonSpieler(zuvorGeschosseneSchuesse1)
                    schiffe1, hit1, miss1, comp1, missed1 = pruefung_schuss(schuss1, schiffe1, hit1, miss1, comp1)
                    show_board_Spieler(hit1, miss1, comp1)
                    # repeat until ships empty
                    if check_if_empty_game(schiffe1):
                        # print("end of game - winner in", i)
                        clear = lambda: os.system('cls')  # killt die ueberschrift
                        clear()

                        time.sleep(2)
                        third = render('DU HAST GEWONNEN!', font='block', colors=['blue', 'white'], align='center')
                        print(third)
                        print("                 IN", i, "ZÜGEN GEWONNEN")
                        time.sleep(9)
                        # clear = lambda: os.system('cls')  # killt die ueberschrift
                        clear()
                        break

                    # Computer schießt

                    schuss2, zuvorGeschosseneSchuesse2 = schuss_VonComputer(zuvorGeschosseneSchuesse2, taktik2)
                    schiffe2, hit2, miss2, comp2, missed2 = pruefung_schuss(schuss2, schiffe2, hit2, miss2, comp2)
                    show_board_Computer(hit2, miss2, comp2)

                    if missed2 == 1:
                        taktik2 = taktik_strategie(schuss2, taktik2, zuvorGeschosseneSchuesse2, hit2)
                    elif missed2 == 2:
                        taktik2 = []
                    elif len(taktik2) > 0:
                        taktik2.pop(0)

                    if check_if_empty_game(schiffe2):
                        # print("end of game - computer wins", i)
                        clear = lambda: os.system('cls')  # killt die ueberschrift
                        clear()
                        time.sleep(2)
                        third = render('DU HAST VERLOREN!', font='block', colors=['blue', 'white'], align='center')
                        print("                 IN", i, "ZÜGEN VERLOREN")
                        time.sleep(9)
                        # clear = lambda: os.system('cls')  # killt die ueberschrift
                        clear()
                        break
                bs = "n"

            elif bestaetigung == "n":
                bs = "n"

            elif bestaetigung != "j" or bestaetigung != "n":
                print("Bitte nur j für ja und n für nein bestätigen.\n")
                bs = "n"

        elif "3" == check:
                # info
                bestaetigung = input("Spielanleitung ausführen? [j/n]:")
                if bestaetigung == "j":
                    print("\nSpielanleitung"
                          "\n")

                    print("Schiffe Versenken ist ursprünglich ein harmloses Symbolspiel,\n"
                          "wessen Herkunft mindestens bis zum Ende des 19. Jahrhundert zurückreicht\n"
                          "und seine Grundstruktur bis heute unverändert erhalten ist.\n"
                          "Diese Grundstruktur haben wir in der Programmiersprache Python übertragen.\n")

                    print(
                        "Vor Beginn des Spiels sucht sich der Spielre einen Ort auf dem 10x10 großen Feld aus, an dem seine Schiffe stehen sollen.\n"
                        "Dies geschieht in dem man die Koordinaten des Ortes nacheinander eintippt und bestätigt. (A1,A2,A3 etc.)\n"
                        "Es wird immer angezeigt, um welches Schiff es im Moment geht. Jeder Spieler hat 1-5er, 1-4er,2-3er und 2-2er Schiffe\n"
                        "Sind alle Schiffe platziert, erscheint noch ein letztes Mal das Spielfeld mit den Schiffen des Spielers.\n")

                    print(
                        "Das Spiel beginnt.  Es wird auf Koordinaten gefeuert auf den der Spieler ein feindliches Schiff vermutet.\n"

                        "Trifft der Spieler, erscheint ein „o“\n"
                        "Versenkt der Spieler ein Schiff, erscheint ein „0“\n"
                        "Trifft der Spieler nichts, erscheint ein „x“ \n")

                    print(
                        "Es wird so lange hin und her gefeuert, bis ein Spieler keine Schiffe mehr hat. Dieser Spieler ist dann der Verlierer.\n"
                        "Sollten Fehler bei der Eingabe entstehen, versucht das Spiel bei der Eingabe zu helfen und Tipps zu geben.\n"
                        "Bei dem Player vs. Computer Modus übernimmt ein Algorithmus den Platz des zweiten Spielers und versucht so taktisch den Spieler zu besiegen.\n"
                        "Ist das Spiel vorbei, verschwindet das Spielfeld und der Gewinner wird eingeblendet.\n"
                        "Als Zusatzfunktion wird angezeigt, in wie viel Runden der Spieler gewonnen hat.\n"
                        "\nFolgende Regeln sind zu beachten:\n"
                        "1.    Schiffe dürfen auf dem Rand liegen, jedoch nicht darüber hinaus.\n"
                        "2.    Schiffe können nicht diagonal aufgestellt werden.\n"
                        "3.    Koordinaten können groß als auch klein geschrieben werden, jedoch muss der Buchstabe stets vorne stehen\n"
                        "     und in der Koordinate darf höchstens ein Buchstabe und eine Zahl sein.\n")

                    print("\nZiel des Spiels:\n"
                          "\n"
                          "Der Gewinner des Spiels ist der Spieler der alle gegnerischen Schiffe vollständig versenkt hat.\n"
                          "\n"
                          "Viel Spaß wünschen Dir\n"
                          "Merve, Zak und Sam\n")
                    bs = "n"

                elif bestaetigung == "n":
                    bs = "n"

                elif bestaetigung != "j" or bestaetigung != "n":
                    print("Bitte nur j für ja und n für nein bestätigen.\n")
                    bs = "n"

        elif "4" == check:
            #ext
            bestaetigung = input("Möchten Sie das Spiel wirklich beenden? [j/n]:")
            if bestaetigung == "j":
                bs = "j"

            elif bestaetigung == "n":
                bs = "n"

            elif bestaetigung != "j" or bestaetigung != "n":
                print("Bitte nur j für ja und n für nein bestätigen.\n")
                bs = "n"
        else:
            print("Bitte nur j für ja und n für nein bestätigen.\n")
    except:
        print("")
        print("Fehler - Eingabe überprüfen.")

    return bs


check = mainMenu()
bs = finale(check)
def aufseher(bs):
    af = "n"
    while af == "n":
        check = mainMenu()
        bs = finale(check)
        if bs == "j":
            af = "y"
            break
        elif bs == "n":
            print("Wiederholung der Schleife.")

if bs != "j":
    aufseher(bs)
else:
    print("Vielen Dank fürs Spielen.")

