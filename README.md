
# Schiffe-Versenken
Ein Projekt von Zakaria, Merve und Sam.

# Bitte folgende Plug-Ins installieren:

    Für „random2“ : pip install random2
   
    Für „os“: pip install os

    Für „cfonts“: pip install python-cfonts
    
    Falls es zu Problem geben sollte, dann bitte auch Colorama installieren
    Für „colorama“: pip install colorama 

Die weiteren importierten Plug-Ins sollten in Python bereits installiert sein.

# Was ist Schiffe Versenken und wie wird es gespielt?
Schiffe Versenken ist ursprünglich ein harmloses Symbolspiel ,wessen Herkunft mindestens bis zum Ende des 19. Jahrhundert zurückreicht und seine Grundstruktur bis heute unverändert erhalten ist.Diese Grundstruktur haben wir in der Programmiersprache Python übertragen.
Vor Beginn des Spiels sucht sich der Spielre einen Ort auf dem 10x10 großen Feld aus, an dem seine Schiffe stehen sollen
Dies geschieht in dem man die Koordinaten des Ortes nacheinander eintippt und bestätigt. (A1,A2,A3 etc.)
Es wird immer angezeigt, um welches Schiff es im Moment geht. Sind alle Schiffe platziert,
erscheint noch ein letztes Mal das Spielfeld mit den Schiffen des Spielers.

Das Spiel beginnt.Es wird auf Koordinaten gefeuert auf den der Spieler ein feindliches Schiff vermutet.
      
  "Trifft der Spieler, erscheint ein „o“
  "Versenkt der Spieler ein Schiff, erscheint ein „0“
  "Trifft der Spieler nichts, erscheint ein „x“ 

Es wird so lange hin und her gefeuert, bis ein Spieler keine Schiffe mehr hat. Dieser Spieler ist dann der Verlierer.
Sollten Fehler bei der Eingabe entstehen, versucht das Spiel bei der Eingabe zu helfen und Tipps zu geben.\n"
      "Bei dem Player vs. Computer Modus übernimmt ein Algorithmus den Platz des zweiten Spielers und versucht so taktisch den Spieler zu besiegen.\n"
      "Ist das Spiel vorbei, verschwindet das Spielfeld und der Gewinner wird eingeblendet.\n"
      "Als Zusatzfunktion wird angezeigt, in wie viel Runden der Spieler gewonnen hat.\n"
      ""
      "Folgende Regeln sind zu beachten:
      "1.    Schiffe dürfen auf dem Rand liegen, jedoch nicht darüber hinaus.
      "2.    Schiffe können nicht diagonal aufgestellt werden.
      "3.    Koordinaten können groß als auch klein geschrieben werden, jedoch muss der Buchstabe stets vorne stehen
      und in der Koordinate darf höchstens ein Buchstabe und eine Zahl sein.

# Ziel des Spiels:
 Der Gewinner des Spiels ist der Spieler der alle gegnerischen Schiffe vollständig versenkt hat.
    
   **Viel Spaß wünschen Dir**
   
   *Zakaria, Merve und Sam* **😊**
