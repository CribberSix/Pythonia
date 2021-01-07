#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
#__author__ = 'Victor Seifert'
import sys
import StringIO, sys
from Tkinter import *
import pygame

########### GAME INITIALIZING ###########

root = Tk()
rtitle = root.title("Let's learn Python!")
root.geometry(("%dx%d")%(960,690)) # Window size



def on_closing():
    # Description: Empties the communication_file and set it up to continue the game
    #   - If the file is empty, the game isn't slowed down anymore.
    # Parameters: None
    # Returns: None
    comm_file2 = open("communication_file.txt","w")
    comm_file2.write("")
    comm_file2.close()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', on_closing)




########### TEXT VARIABLES FOR ALL LESSONS ###########

# This variable controls the achieved lessons.
# (used in the archive function e.g. to display only those buttons of the lessons we have access to yet)
Lesson_Number = -1

# This variable controls the current Lesson to load all specific variables and data into the coding part of the game
current_Lesson = -1

# Maximum of lessons implemented
maxLessons = 25





# Text: Introduction and tasks

# GivenCode: given Code at the beginning
# SolutionCode: What we want them to programm

# StringBoolean: True if String Checking is needed for this lesson
# SolutionOutput: expected String

# AddedCodeBoolean: True if Variable value checking is needed for this lesson
# AddedCode: variable value checking code


Lesson0_0_Text = "Lektion 0: \n\nHerzlich willkommen zu unserem Pythonlerntutorial! \n\nImmer wenn du ein Abenteuer bestanden" \
           " hast, wirst du mit einer Python Lektion belohnt und kannst so spielerisch Programmieren lernen.\n"\
           "Dabei wirst du Schritt für Schritt in eine der meist verwendeten Skriptsprachen, Python, eingeführt.\n\n"\
           "Zum Verständnis der Aufgaben werden die Befehle und vorgegebene Begriffe in spitze Klammern <Befehl> gesetzt.\n\n\nUm eine Lektion abzuschließen und zur nächsten zu kommen, " \
           "klicke auf 'Check Code'. Hast du den richtigen Code programmiert, wird dir das Ergebnis ausgegeben und der 'Weiter' Knopf wird eingeblendet. \n" \
           "Wenn du etwas Falsches eingibst, wird dir eine Fehlermeldung angezeigt. \n\nDa wir im Moment keine Aufgabe gestellt haben, probiere es einfach mal aus und klicke auf 'Check Code'. " \
	       "Python ist sehr sensitiv, wenn es um Leerzeichen und Groß- und Kleinschreibung geht! Achte auf Leerzeichen am Anfang, Einrückungen mit Tab und dass dein Ergebnis exakt der Aufgabenstellung entspricht!\n\n\n\n\n\n\n\n"

Lesson0_0_GivenCode = "\n\n\n\n\n"
Lesson0_0_SolutionCode = ""

Lesson0_0_StringBoolean = False
Lesson0_0_SolutionOutput =""

Lesson0_0_AddedCodeBoolean = False
Lesson0_0_AddedCode = ""

Lesson0_0_Name = "Intro"




Lesson0_1_Text ="Lektion 0.1: \n\nUnsere Charakter kann im Moment noch nicht hoch genug springen um auf einen Block zu kommen. \n" \
				"In Python verwenden wir Variablen um Werte zu speichern. Variablen können wir fast beliebig bennennen. Spaeter dazu mehr.\n\n"\
				"Wir haben in diesem Spiel eine Variable, die die Hoehe eines Sprungs unseres Charakters bestimmt. Im Moment ist diese allerdings auf 0.7 "\
				"eingestellt. \n\nVeraendere den Wert der Variable <sprunghoehe> auf '3.5' um die Sprunghoehe unserer Spielfigur anzupassen und ihn hoeher springen zu lassen.\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson0_1_GivenCode = "sprunghoehe = 0.7"
Lesson0_1_SolutionCode = "sprunghoehe = 3.5"

Lesson0_1_StringBoolean = False
Lesson0_1_SolutionOutput= ""

Lesson0_1_AddedCodeBoolean= True
Lesson0_1_AddedCode = "\nif sprunghoehe == 3.5:\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable sprunghoehe hat einen falschen Wert')"

Lesson0_1_Name = "Sprunghoehe"


Lesson1_0_Text = "Lektion 1.0: \n\nWillkommen zu deiner ersten Lektion.\n\nJedes Programm muss mit der Welt kommunizieren können. \n" \
                  "Dazu gibt es in Python die Funktion <print> (ausdrucken/ausgeben). \n\n\nDas einfachste Beispiel " \
                  "hierfür ist sich \n'Hello World' ausgeben zu lassen. \nDazu muss der Befehl <print> und die gewünschte " \
                  "Ausgabe in Anführungszeichen <'Hello World'> eingegeben werden, da in diesem Fall die Ausgabe ein String (also eine Reihenfolge von Buchstaben) ist. \n\n\n\nAufgabe: \n\nGeben Sie folgenden Satz aus: \n" \
                  "'Python ist KEINE Schlange'\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_0_GivenCode = "print 'Hello World'\n\n\n\n\n"
Lesson1_0_SolutionCode = "print 'Python ist KEINE Schlange'"

Lesson1_0_StringBoolean = True
Lesson1_0_SolutionOutput ="Python ist KEINE Schlange"

Lesson1_0_AddedCodeBoolean = False
Lesson1_0_AddedCode = ""
Lesson1_0_Name = "Print"

Lesson1_1_Text = "Lektion 1.1:\n\nUm Werte und Ergebnisse wieder verwenden zu können," \
                 " gibt es in Programmiersprachen Variablen. \nDiese haben einen Namen und können " \
                 "mit Werten belegt werden. Für den Namen können " \
                 "Groß- und Kleinbuchstaben, Ziffern und das Zeichen _ (Unterstrich) verwendet werden.\n" \
                 "Das erste Zeichen darf aber keine Ziffer sein und es dürfen keine " \
                 "reservierten Wörter der Programmiersprache verwendet werden. \n\n\n" \
                 "Wie in der Mathematik kann man mit diesen Variablen die Grundrechenarten " \
                 "Addition ( + ), Subtraktion ( - ), Multiplikation ( * ) und Division ( / ) ausführen.\n" \
                 "Dabei kann sowohl mit ganzen Zahlen (Integer), als auch mit Fließkomma Zahlen " \
                 "(Floats) gerechnet werden. Bei Floats wird wie im Englischen üblich der < . > (Punkt) " \
                 "statt des Kommas verwendet.\n\n\n\n" \
                 "Aufgabe: \n\nWeisen Sie der Variablen x die Differenz aus 14.56 - 7 zu. \n" \
                 "Berechnen Sie anschließend für y das " \
                 "Produkt von 35 * x. \nGeben Sie " \
                 "das Ergebnis jeweils in dieser Reihenfolge (x,y) aus.\n\n\n\n\n\n\n"

Lesson1_1_GivenCode = "x = 3 + 1732\nprint x\n\n\n\n\n"
Lesson1_1_SolutionCode = "x = 14.56 - 7\nprint x\ny = 35 * 49\nprint y\nz = 50.4 / 3.6\nprint z"

Lesson1_1_StringBoolean = True
Lesson1_1_SolutionOutput ="7.56\n264.6"

Lesson1_1_AddedCodeBoolean = True
Lesson1_1_AddedCode =  \
    "\nif (x == (14.56 - 7):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable x hat einen falschen Wert')" \
    "\nif (y == 264.6):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable y hat einen falschen Wert')" \

Lesson1_1_Name = "Integer und Rechenzeichen"



Lesson1_2_Text = "Lektion 1.2 \n\nZusätzlich zu dem normalen Divisionsoperator < / > gibt es die ganzzahlige Division. Der Operator dazu ist der < // >. " \
                 "Mit diesem wird das ganzzahlige Ergebnis der Division berechnet. Zusätzlich gibt es den Modulo Operator < % >, mit dem der Rest berechnet wird.\n\n\n" \
                 "Speziell in Python 2 liefert auch schon 7/5 das ganzzahlige Ergebnis 1, dies kann aber mit 7.0/5 oder 7/5.0 umgangen werden um die Kommastelle auch zu berechnen. \n\n\n\n" \
		 "Aufgabe: \n\nBerechne den Wert von 7 geteilt durch 2 als ganzzahlige Divison mit dem Operator < // >, weise das Ergebnis der Variable 'GanzeZahl' zu und gebe ihn aus.  \n\n" \
                 "Berechne zusätzlich den Rest von 7 geteilt durch 5 mit Modulo < % >, weise ihn der Variable 'mod' zu und gebe ihn aus.\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson1_2_GivenCode = "GanzeZahl = 7 / 2\n\n\n\n\n"
Lesson1_2_SolutionCode = "mod = 7 % 5\nprint mod"

Lesson1_2_StringBoolean = True
Lesson1_2_SolutionOutput ="3\n2"

Lesson1_2_AddedCodeBoolean = True
Lesson1_2_AddedCode = \
    "\nif (GanzeZahl == 1.0:\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable GanzeZahl hat einen falschen Wert')" \
    "\nif (mod == 2:\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable mod hat einen falschen Wert')" \

Lesson1_2_Name = "Modulo 1"




########################################_2_Lektion_########################################

Lesson2_0_Text = "Lektion 2.0: \n\nUm nicht nur mit Zahlen arbeiten zu können, sondern auch mit Texten, gibt es auch Variablen " \
                 "für Zeichenketten (Strings). Die Zuweisung erfolgt dadurch, dass die entsprechende Zeichenkette " \
                 "in '_____' (Anfuehrungsstrichen) gesetzt wird. Für Zeichenketten gibt es die Operationen + und *. " \
                 "Bei + werden die Inhalte zweier Stringvariablen aneinander gehaengt, bei * kann die " \
                 "Stringvariable mit einer ganzen Zahl multipliziert werden:\n" \
                 "\nprint 'rot' * 3\n" \
                 "# Die Ausgabe hierzu ist: 'rotrotrot'\n\n" \
                 "Wir wollen nun unserem Spieler einen eigenen Namen geben. \n\n\nAufgabe:\n\n" \
                 "Weise hierzu den Variablen 'vorname' und 'nachname' beliebige Werte zu. \nAnschließend belege die Variable " \
                 "'vollerName' mit vorname und nachname (Operator: < + >). Ueberlege wie du mit dem Wissen der Lektion in den vollen Namen ein String " \
                 "mit einem einzelnen Leerzeichen zwischen Vor- und Nachname einbauen kannst. \nAnschließend gebe die Variable 'vollerName' aus um zu kontrollieren ob du auch ein Leerzeichen eingebaut hast." \



Lesson2_0_GivenCode = "HelloWorld ='Hello'+'World'" \
                      "\n# In diesem String ist KEIN Leerzeichen enthalten!" \
                      "\n" \
                      "\n# Das Hashtag Symbol steht fuer einen Kommentar" \
                      "\n# Die Zeile wird nicht als Code gewertet und nicht beachtet" \
                      "\n# bei der Ausfuehrung, ist aber hilfreich zur Dokumentation." \
                      "\n\n\nvorname = ''" \
                      "\nnachname = ''" \
                      "\nvollerName = ''" \
                      "\n\n\n\n"

Lesson2_0_SolutionCode = ""
Lesson2_0_StringBoolean = False
Lesson2_0_SolutionOutput =""

Lesson2_0_AddedCodeBoolean = True
Lesson2_0_AddedCode = "\nif (vorname == ''):\n\tErrorlist.append('Error: Variable vorname hat einen falschen Wert')" \
    "\nif (nachname == ''):\n\tErrorlist.append('Error: Variable nachname hat einen falschen Wert')" \
    "\nif (vollerName == ''):\n\tErrorlist.append('Error: Variable vollerName hat einen falschen Wert')" \
    "\nif (' ' not in vollerName):\n\tErrorlist.append('Error: Variable vollerName enthaelt kein Leerzeichen!)"

Lesson2_0_Name = "String Variablen"





Lesson2_1_Text = 	"Lektion 2.1: \n\nWir können auch Zahlen in einen String einfügen und dann ausgeben. Es funktioniert fast wie in der Lektion davor, bloß müssen wir noch "	\
			"an der Zahl eine kleine Veränderung vornehmen. \n\nUm eine Zahl mit dem < + > Operator an einen String anfügen zu können, wie wir das vorher mit " \
			"Strings an Strings gemacht haben, müssen wir die Zahl zu einem String formatieren. Ausgabe-technisch verändert sich an der Zahl nichts." \
			"\nUm die Zahl zu einem String zu formatieren benötigen wir den Befehl < str() > :\n\n" \
            "stringZahl = str(zahl)" \
            "\n\n\nAufgabe:\n" \
            "\n1. Lege eine Variable mit dem Namen 'Unsere_Zahl' an und belege sie mit dem Wert <1337>. Gebe diesen Wert aus. " \
            "\n\n2. Anschließend lege einen String an mit dem Namen 'Unser_String' mit dem Inhalt: 'Dies ist ein String.' Gebe auch diesen aus. " \
            "\n\n3. Wir wollen beide Variablen einzeln unverändert behalten, deshalb verändern wir sie nur temporär und weisen Sie nicht neu zu" \
            " - in einem einzigen <print> Befehl: Hänge an 'Unser_String' die (formatierte) Variable 'Unsere_Zahl' an und gebe die Variable aus. \n\n\n" \


Lesson2_1_GivenCode = "Rote_Blume = 'Rote'+'_'+'Blume'"
Lesson2_1_SolutionCode = "Unsere_Zahl = 1337\nprint Unsere_Zahl\nUnser_String ='Dies ist ein String.'\nprint Unser_String\nprint Unser_String + str(Unsere_Zahl)"

Lesson2_1_StringBoolean = True
Lesson2_1_SolutionOutput ="1337\nDies ist ein String.\nDies ist ein String.1337"
Lesson2_1_AddedCodeBoolean = False
Lesson2_1_AddedCode = \
    		"\nif (Unser_String == 'Dies ist ein String.'):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Unser_String hat einen falschen Wert')"     		\
            "\nif (Unsere_Zahl == 1337):\n\t 1+1\nelse:\n\tErrorlist.append('Error: Variable Unsere_Zahl hat einen falschen Wert')"

Lesson2_1_Name = "String Varialben II"







########################################_3_Lektion_########################################



Lesson3_0_Text = "Lektion 3.0: \n\nWir nehmen wir uns " \
                 "jetzt einem sehr essentiellem Thema an, und zwar Listen. \n\n\nListen sind besondere Datenstrukturen. " \
                 "In ihnen können mehrere Werte gespeichert werden. Der Zugriff auf diese Werte erfolgt mit einem Index " \
                 "(die Stelle in der Liste, an der der Wert gespeichert ist — beginnend bei 0 !). \n\nEine Liste wird mit < [ ] > definiert. " \
                 "Stellen wir uns vor unser Charakter soll ein Inventar haben. Dann müssen wir eine Liste anlegen mit allen Gegenständen die sich darin befinden. " \
                 "\n\nAufgabe:" \
                 "\nWir wollen folgende Dinge in dieser Reihenfolge mitnehmen: " \
                 "Einen 'Apfel', ein paar 'Muenzen', ein 'Schwert', ein 'Schild' und natürlich eine 'Rose' für die Prinzessin. \n\nLege eine Variable mit dem Namen " \
                 "'inventar' an und füge sämtliche Gegenstände hinzu. Lasse anschließend die Liste auf dem Bildschirm ausgeben.\n\n" \
                 "Als letztes gib das letzte Element in der Liste aus indem du mit dem Index darauf zugreifst." \
                 "\nUm ueber den Index auf etwas zuzugreifen, schreibe:" \
                 "\nprint liste[Index-Nummer]" \
                 "\n\nBedenke: Das erste Element steht nicht an dem Index 1 sondern an Index 0!\n"


Lesson3_0_GivenCode = "liste = [] # Da wir in der dritten Zeile die Liste gleich füllen," \
                      "\n# können wir die erste Zeile auch weglassen" \
                      "\n\n#    liste = [0, 1, 2, 3]" \
                      "\n#    print liste[1] # Die zweite (!) Stelle wird ausgegeben. \n\n\n\n\n"
Lesson3_0_SolutionCode = "inventar = ['Apfel', 'Muenzen', 'Schwert', 'Schild', 'Rose']\nprint(inventar)"

Lesson3_0_StringBoolean = True
Lesson3_0_SolutionOutput ="['Apfel', 'Muenzen', 'Schwert', 'Schild', 'Rose']\nRose"

Lesson3_0_AddedCodeBoolean = True
Lesson3_0_AddedCode = "\nif (inventar == ['Apfel', 'Muenzen', 'Schwert', 'Schild', 'Rose']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable inventar hat einen falschen Wert')"

Lesson3_0_Name = "Listen"




Lesson3_1_Text = "Lektion 3.1: \n\n " \
	"Wir schreiten fort zu dem Themenkomplex der Kontrollstrukturen. " \
	"In einem Programm möchte man oftmals in Abhängigkeit von einer bestimmten Bedingung unterschiedlich " \
	"verfahren. Dazu wird die Bedingung, die nach dem Befehl < if > (wenn) folgt, überprüft. " \
	"Ist diese wahr (True), so wird der Code ausgeführt, der direkt im Anschluss folgt. Um zu kennzeichnen, " \
	"dass der Code zu dem if-Block gehört, wird er mit einem Tab eingerückt. Wenn der Code nicht mehr zu " \
	"dem if-Block gehört, wird er nicht mehr eingedrückt.\n\n"\
	"Ist die Bedingung falsch (False), so wird  der Code nach < else > (‘sonst’) ausgeführt. Else selber wird nicht eingerückt. " \
	"Zwischen den if/else Blöcken darf nichts stehen, das nicht eingerückt ist!" \
    "\n\nAufgabe:" \
    "Wir würden lieber die 'Axt' statt dem 'Speer' kaufen aber wenn wir uns es leisten können beides." \
    "Die Axt kostet 5 Münzen, der Speer 2 Münzen. " \
    "\n\nSchreibe einen if-else Konstrukt in dem wir testen ob unser Geld reicht für die 'Axt', wenn ja, dann teste ob wir uns den Speer auch noch kaufen können. Wenn wir nicht genug" \
    "Geld für die 'Axt' haben, teste ob unser Geld immerhin noch für den 'Speer' reicht." \
    "\n\nUm die Aufgabe abzuschließen, gebe auf dem Bildschirm den Namen der Gegenstände aus die wir uns kaufen können wenn wir 10 Muenzen (gespeichert in der Variable: 'muenzen') haben und dann das Restgeld. " \
    "\n\nProbiere es jedoch vielleicht zuerst mit 1 / 4 / 6 Münzen um die " \
    "verschiedenen Wege in der Kontrollstruktur zu erkennen.  " \


Lesson3_1_GivenCode =   "\nblumenstrauss = 0 "\
			"\nschokolade = 0 "\
			"\nmuenzen = 1 " \
			"\n#Modifiziere das Beispiel oder schreibe es selber neu!" \
			"\n" \
			"\nif geld >= preis:"\
    			"\n\tprint 'Wir können uns etwas kaufen'" \
                "\n\tgeld = geld - preis"\
			"\nelse: "\
    			"\n\tprint 'Wir können uns nichts leisten.'\n\n\n\n\n" \

Lesson3_1_SolutionCode = "if taschengeld > blumenstrauss:" \
				"\n\tprint 'Blumenstrauss' " \
				"\n\ttaschengeld = taschengeld - blumenstrauss" \
				"\nif taschengeld > schokolade " \
				"\n\tprint 'Schokolade' " \
				"\n\ttaschengeld = taschengeld - schokolade" \
				"\nprint taschengeld"

Lesson3_1_StringBoolean = True
Lesson3_1_SolutionOutput = "Axt\nSpeer\n3"

Lesson3_1_AddedCodeBoolean = True
Lesson3_1_AddedCode = 	"\nif (muenzen == 3 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable muenzen hat einen falschen Wert')" \
			"\nif (Axt == 5 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Axt hat einen falschen Wert')" \
			"\nif (Speer == 2 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Speer hat einen falschen Wert')"

Lesson3_1_Name = "if/else Konditionen"


Lesson3_2_Text = "Lektion 3.2: Kontrollstrukturen II\n\n Anstatt etwas auszuwerten durch " \
                 "Vergleichsoperatoren, können wir einer Variable auch einen sogenannten -Boolean- Wert zuweisen. Boolean beinhaltet nur zwei Werte: <True> und <False>. " \
                 "\n\nWeiterhin können wir in dem <else> Block auch noch einen alternativen Wert prüfen - damit wir aber nicht zu oft Blöcke einrücken müssen, können wir den Operator <elif> wie rechts im Beispiel nutzen!" \
                 "\n\nDesweiteren gibt es eine Reihe von Vergleichsoperatoren über die du Bescheid wissen solltest, einige davon kennst du sicherlich schon aus dem" \
                 "Mathematik Unterricht:\n  < (kleiner)\n   > (größer) \n  <= (kleiner gleich)\n  >= (größer gleich) \n  == (gleich)\n   != (ungleich) \n" \
                 "\nAufgabe:\n\n" \
                 "1. Wenn die BooleanVariable 'verletzt' <False> (falsch) ist, dann weise der 'Farbe' unseres Charakters den String 'Normal' zu." \
                 "\n\n2. Wenn die Variable 'verletzt' <True> ist, prüfe ob wir noch mehr als 0 Lebenspunkte haben und verändere die 'Farbe' des Spielers auf 'Rot'. " \
                 "\n\n3. Sollten wir 0 'Lebenspunkte' haben, gib den Satz aus: 'Game Over!' " \
                 "\n\nUm die Lektion abzuschließen, setze die Variable 'verletzt' auf <True> und 'Lebenspunkte' auf '0'." \


Lesson3_2_GivenCode =   "BooleanVariable = True" \
                        "\nbooleanVar2 = False" \
                        "\n\n# Statt:\n\nif booleanVar2:\n\tprint'1'\nelse:\n\tif 1==2:\n\t\tprint'2'\n\telse:\n\t\tprint'3'\n\n\n\n# mit <elif>\n\nif 1==0:\n\tprint '1'\nelif 1==2:\n\tprint'2'\nelse:\n\tprint'3'" \
                        "\n\nFarbe = 'Grün'" \

Lesson3_2_SolutionCode = ""

Lesson3_2_StringBoolean = True
Lesson3_2_SolutionOutput = "Game Over!"

Lesson3_2_AddedCodeBoolean = True
Lesson3_2_AddedCode = 	"\nif (verletzt == True ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable verletzt hat einen falschen Wert')" \
                        "\nif (Lebenspunkte == 0 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Lebenspunkte hat einen falschen Wert')" \
                        "\nif (farbe == 'Rot' ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Lebenspunkte hat einen falschen Wert')"

Lesson3_2_Name = "elif und Vergleiche"


########################################_4_Lektion_########################################



Lesson4_1_Text = "Lektion 4.1 \n\nEine kurze Zwischenlektion um mit Vergleichen effizienter zu arbeiten, da Kontrollstrukturen einen sehr großen Teil von Programmieren ausmachen:" \
                 "\nStatt direkt hintereinander zwei <if>-Abfragen zu schreiben können wir diese auch verbinden mit dem Operator < and > wenn wir wissen wollen ob BEIDE richtig sind:" \
                 "\n\n" \
                 "if (x > z)  and  (z > y):\n\tprint 'x ist die größte Variable'" \
                 "\n\nDasselbe funktioniert auch wenn es uns reicht wenn NUR EINER von zwei Vergleichen wahr (True) ist, mit dem Operator < or > :" \
                 "\n\n" \
                 "if (x > z)  or  (x > y):\n\tprint 'x ist größer als mindestens eine der anderen Variablen'" \
                 "\n\nZu guter Letzt gibt es noch den Operator \n< not >. Dieser dreht einen Wahrheitswert (Boolean = True / False) um. " \
                 "\n\n" \
                 "not True # ergibt False" \
                 "\nnot not False # ergibt False (2x negiert)" \
                 "\n\n(1 > 2) or not (2 > 3) #ergibt:" \
                 "\n(False) or not (False) #ergibt:" \
                 "\nFalse or True #ergibt: " \
                 "\nTrue" \
                 "\n\n" \
                 "Überlege zuerst welche der gestellten Beispiele im Codebereich Wahr (True) oder Falsch (False) ergeben. Dann führe den Code aus um zu sehen ob du richtig gelegen hast!"

Lesson4_1_GivenCode =   "\nTrue and True" \
                        "\nprint '1. ' +str(True and True)" \
                        "\n" \
                        "\nFalse and True" \
                        "\nprint '2. '+str(False and True)" \
                        "\n" \
                        "\n1 == 1 and 2 == 1" \
                        "\nprint '3. '+str(1==1 and 2==1) " \
                        "\n" \
                        "\nFalse and 0 != 0" \
                        "\nprint '4. ' +str(False and 0 != 0)" \
                        "\n" \
                        "\nnot (10 == 1 or 1000 == 1000)" \
                        "\nprint '5. ' +str(not (10 == 1 or 1000 == 1000))" \
                        "\n" \
                        "\nnot (1 != 10 or 3 == 4)" \
                        "\nprint '6. ' +str (not (1 != 10 or 3 == 4))" \
                        "\n" \
                        "\nnot ('testing' == 'testing' and 'Zed' == 'Cool Guy')" \
                        "\nprint '7. ' +str (not('testing' == 'testing' and 'Zed' == 'Cool Guy'))" \
                        "\n" \
                        "\n3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun'))" \
                        "\nprint '8. ' +str(3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun')))" \
                        "\n" \
                        "\n1 == 1 and (not ('testing' == 1 or 1 == 0))" \
                        "\nprint '9. ' +str(1 == 1 and (not ('testing' == 1 or 1 == 0)))" \
                        "\n\n"

Lesson4_1_SolutionCode = ""

Lesson4_1_StringBoolean = False
Lesson4_1_SolutionOutput = ""

Lesson4_1_AddedCodeBoolean = False
Lesson4_1_AddedCode = 	""

Lesson4_1_Name = "And; Or; Not"




Lesson4_2_Text = "Lektion 4.1: \n\nNachdem wir jetzt den Grundstein für komplexere Entscheidungsstrukturen und Listen" \
		 "gelegt haben, gehen wir jetzt dazu über Listen dynamisch im Code zu manipulieren basierend auf Entscheidungen, die wir vorher treffen. " \
		 "Um zu einer bestehenden Liste etwas hinzuzufügen (anzuhängen) ist der folgende Befehl nötig:\n " \
		 "<listenname.append(something)>. 'something' kann zum Beispiel ein String sein oder eine Zahl.\n\n" \
		 "Um etwas aus einer Liste zu entfernen ist der folgende Befehl nötig: \n" \
		 "listenname.remove(something). \n\n\n" \
		 "Aufgabe: \n\nSchreibe einen if-else-Block mit dem du auswertest, ob unser Charakter 3 Lebenspunkte hat oder nicht. \n\nWenn ja ist, will " \
		 "unser Charakter zusätzlich zuerst (!) seine 'Axt' und dann den 'Apfel' einpacken aber nimmt den 'Schild' nicht mit. \n\nFalls er weniger als 3 Lebenspunkte hat, werte aus ob er noch 2 Lebenspunkte hat. " \
         "In diesem Fall nimmt er einen 'Apfel' und ein 'Buch' mit. " \
		 "\nAnsonsten nimmt er zuerst einen 'Apfel' und dann den 'Speer', aber kein 'Schwert' mit. " \
         "\n\nNach dem if/else Konstrukt gebe die inventar-Liste mit <print> aus. Gehe davon aus, dass unser Charakter nur 1 Lebenspunkt hat um die Aufgabe abzuschließen. "



Lesson4_2_GivenCode =   "Lebenspunkte = 3 \ninventar = ['Muenzen', 'Schwert', 'Schild', 'Rose']\n\n\n\n\n"

Lesson4_2_SolutionCode = "Lebenspunkte = 1 \ninventar = ['Muenzen', 'Schwert', 'Schild', 'Rose']]\n\nif Sommer:" \
			 "\n\tgepaeck.append('Badehose') " \
			 "\n\tgepaeck.append('Sonnenbrille') " \
			 "\n\tgepaeck.remove('Jeans') " \
			 "\nelse: " \
			 "\n\tgepaeck.append('Pullover') " \
			 "\n\tgepaeck.append('Jacke') " \
			 "\n\tgepaeck.remove('Hemd')" \
			 "\n\tprint gepaeck"

Lesson4_2_StringBoolean = True
Lesson4_2_SolutionOutput = "['Muenzen', 'Schild', 'Rose', 'Apfel', 'Speer']"

Lesson4_2_AddedCodeBoolean = True
Lesson4_2_AddedCode = 	"\nif (inventar == ['Muenzen', 'Schild', 'Rose', 'Apfel', 'Speer'] ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable inventar hat einen falschen Wert')" \
                         "\nif (Lebenspunkte == 1 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Lebenspunkte hat einen falschen Wert')"

Lesson4_2_Name = "Listenmanipulation I"



########################################_5_Lektion_########################################



Lesson5_0_Text = "Lektion 5.0: \n\n" \
		"Oft möchte man Code wiederholt ausführen — " \
		"hierfür verwenden wir sogenannte Schleifen (engl. ‘loops’). " \
		"Loops funktionieren vom Aufbau wie if/else-Blöcke. Alles was eine Ausführung des Loops ausführen soll, wird eingerückt. " \
		"Angenommen wir haben eine Liste mit ganzzahligen Werten und "\
		"möchten zu jedem Wert 1 addieren und anschließend ausgeben, dann sähe das wie folgt aus:"\
		"\n\n\nliste = [0, 1, 2, 3]" \
		"\nfor zahl in liste:" \
		"\n\tzahl = zahl + 1"\
        "\n\t# liste.remove(zahl)" \
		"\nprint liste" \
        "\n\nWir möchten unser Inventar mit einer for-Schleife durchsuchen ob wir noch einen Apfel dabei haben. Wenn wir einen gefunden haben, wollen wir ihn essen. " \
        "Gebe also den Apfel aus wenn du ihn gefunden hast, dann entferne ihn mit dem Befehl <liste.remove(Objekt)> und erhöhe die Lebenspunkte um 1 (nur wenn ein Apfel auch tatsächlich dabei ist). " \
        "Benutze in der for-Schleife eine if-Klausel um den Apfel zu identifizieren. " \
        "\n\n\n" \
        "Diese For-Schleife ist speziell, da wir ein Gegenstand aus der Liste entfernen während wir sie durchsuchen, dadurch ändern sich die Indexe! Um zu vermeiden etwas zu überspringen, " \
        "müssen wir eine kleine Veränderung vornehmen < [:]: > wie folgt:" \
        "\n\n" \
        "for element in liste[:]:" \
        "\n\tBlock"

Lesson5_0_GivenCode =   "lebenspunkte = 1\n" \
                        "inventar = ['Schwert', 'Speer', 'Apfel', 'Rose', 'Muenzen']\n\n\n\n\n"

Lesson5_0_SolutionCode = "gepaeck = ['Jeans', 'Hemd', 'Socken', 'Schuhe', 'Zahnbuerste']" \
			"\nfor x in gepaeck[:]: " \
			"\n\tKleiderschrank.append(x) " \
			"\n\t gepaeck.remove(x) " \
			"\nprint gepaeck" \
			"\nprint kleiderschrank"

Lesson5_0_StringBoolean = True
Lesson5_0_SolutionOutput = "Apfel"

Lesson5_0_AddedCodeBoolean = True
Lesson5_0_AddedCode = 	"\nif (inventar = ['Schwert', 'Speer', 'Rose', 'Muenzen'] ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable inventar hat einen falschen Wert')"
Lesson5_0_Name = "For-Schleife"



Lesson5_1_Text = 	"Lektion 5.1: \n\nWie wir schon am Anfang bei Listen gelernt haben, Listen fangen bei '0' zu zählen an. Denke daran bei dieser Aufgabe! \n\n" \
			"Um den Index (also die Stelle) eines Elements in einer Liste herauszufinden, gibt es in Python den folgenden Befehl: \n" \
			"<listenname.index(something)>. \n\n\nAufgabe:\n" \
            "\n1. Gebe den Index mit dem dazugehörenden Element aller Elemente in der Liste mit <print> aus: " \
            "\n\nprint (liste.index(element) +' ' + element)" \
            "\n\n2. Anschließend füge mit dem Befehl <listenname.insert(index,'something')> an die Index-Stelle der Stiefel "  \
			"einen 'Apfel' ein. " \
            "\nAlle Elemente die darauf folgen, werden im Index um 1 erhöht, da ein Index immer nur mit einer Zahl belegt sein kann. " \
            "\n\n3. Gebe mit einer for-Schleife jeweils die Indexe der einzelnen gepackten Gegenstände mit dem Gegenstand selber aus (Wie oben)." \
			"\n\nWenn du die Aufgabe abgeschlossen hast, kontrolliere den Index der Stiefel vor und nach dem Einfügen des Apfels am selben Index!\n\n" \
            "Denke daran, dass du den Index zu einem String mit < str(index) > formatieren musst!"

Lesson5_1_GivenCode =   "inventar = ['Schwert', 'Stiefel', 'Rose', 'Muenzen']\n\n\n\n\n"

Lesson5_1_SolutionCode = ""


Lesson5_1_StringBoolean = True
Lesson5_1_SolutionOutput = "0 Schwert\n1 Stiefel\n2 Rose\n3 Muenzen" \
                           "\n0 Schwert\n1 Apfel\n2 Stiefel\n3 Rose\n4 Muenzen"

Lesson5_1_AddedCodeBoolean = True
Lesson5_1_AddedCode = 	"\nif (inventar == ['Schwert', 'Apfel', 'Stiefel', 'Rose', 'Muenzen'] ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable inventar hat einen falschen Wert')" \

Lesson5_1_Name = "Listen - Index und Insert"





Lesson5_2_Text = "Lektion 5.2: \n\nIn dieser Aufgabe wollen wir nun kombinieren, was wir bisher gelernt haben. " \
		"Wir möchten einige Gegenstände die wir gefunden haben in Kisten verstauen. \n\nSchreibe eine for-Schleife " \
		"und teile die Gegenstände so auf die Kisten auf, dass sich in keiner Kiste mehr als 5 Dinge befinden!\n\n\n" \
		"Packe mit einer for-Schleife, in der ein oder mehrere if-else-Blöcke sind, so lange Gegenstände in die ersten Kiste hinein bis diese voll ist . \n" \
		"Dann beginne die zweiten Kiste zu packen und schließlich die dritte. \n\nAnschließend gebe die " \
        "Kisten in dieser Reihenfolge aus mit dem Befehl <print ListenName>. \nIn dieser Lektion brauchst du kein <remove()> benutzen, also wird die Variable 'gepaeck' am Ende noch voll sein. " \
        "(Im Widerspruch zur Realität)\n\n\n" \
        "Um diese Aufgabe zu lösen, musst du noch zwei weitere Befehle kennen:\n\n" \
        "1. Die Länge einer Liste können wir mit <len(listenname)> herausfinden. (Denke daran, letzter Index = Länge-1, da wir " \
        "bei Listen anfangen mit 0 zu zählen!" \
        "\n\n" \
        "2. Mit dem Vergleichsoperator < == > können wir Zahlen, Listen und andere Variablen vergleichen!\n"

Lesson5_2_GivenCode =  "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe', 'Schokolade', 'Buch', " \
            "'Kamera', 'Bonbons', 'Souvenirs', 'Kuchen', 'Taschenlampe']\n" \
            "\n4 == 5 # Dies ergibt 'False'" \
            "\n5 == 5 # Dies ergibt 'True'" \
            "\nkiste_1 = []" \
            "\nkiste_2 = []" \
            "\nkiste_3 = []\n\n\n\n\n\n"

Lesson5_2_SolutionCode = "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe', 'Schokolade', 'Buch',  'Kamera', 'Bonbons', 'Souvenirs', 'Kuchen', 'Taschenlampe'] "\
            "koffer_1 = []" \
            "koffer_2 = []" \
            "koffer_3 = []" \
            "zaehler = 1" \
            "\nfor x in gepaeck: " \
                "if (len(koffer_1) == 5):" \
                    "if (len(koffer_2) == 5):" \
                        "koffer_3.append(x)" \
                    "else:" \
                        "koffer_2.append(x)" \
                "else:"\
                    "koffer_1.append(x)" \
            "print koffer_1" \
            "print koffer_2" \
            "print koffer_3"

Lesson5_2_StringBoolean = True
Lesson5_2_SolutionOutput = "['Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                            "\n['Schokolade', 'Buch', 'Kamera', 'Bonbons', 'Souvenirs']" \
                            "\n['Kuchen', 'Taschenlampe']"

Lesson5_2_AddedCodeBoolean = True
Lesson5_2_AddedCode =   "\nif (kiste_1 == ['Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable kiste_1 hat einen falschen Wert')" \
                        "\nif (kiste_2 == ['Schokolade', 'Buch',  'Kamera', 'Bonbons', 'Souvenirs']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable kiste_2 hat einen falschen Wert')" \
                        "\nif (kiste_3 == ['Kuchen', 'Taschenlampe']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable kiste_3 hat einen falschen Wert')"

Lesson5_2_Name = "Listen splitten"





Lesson5_3_Text =    "Lektion 5.3:\n\nUm noch etwas vertrauter mit dem Thema Listen zu werden, das sehr elementar und wichtig ist, " \
		            "noch eine Aufgabe hierzu: \n\nDrehe den Inhalt einer gegebenen Liste um und speichere ihn in einer " \
		            "neuen Variablen. Gebe diese am Ende mit print aus.\n\n\nWeißt du noch wie man in eine Liste einfügt? Wenn nicht, klicke auf den Archiv-Button." \
                    "\n\n\n(Denke darüber nach, in welcher Reihenfolge eine for-Schleife " \
                    "die Liste durchgeht und an welcher Stelle (Index) du Variablen in eine neue Liste einfügen musst, um die Variablen" \
                    "-Reihenfolge umzudrehen.)\n\n\n" \
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson5_3_GivenCode =  "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                        "\ngepaeck_gedreht = []"

Lesson5_3_SolutionCode = "gepaeck = [ 'Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                        "gepaeck_gedreht = []" \
                        "for x in gepaeck:"\
                            "gepaeck_gedreht.insert(0, x)" \
                        "print gepaeck_gedreht"

Lesson5_3_StringBoolean = True
Lesson5_3_SolutionOutput = "['Winterschuhe', 'Pullover', 'Zahnbuerste', 'Schuhe', 'Socken']" \

Lesson5_3_AddedCodeBoolean = True
Lesson5_3_AddedCode =  "\nif (gepaeck_gedreht == ['Winterschuhe', 'Pullover', 'Zahnbuerste', 'Schuhe', 'Socken']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck_gedreht hat einen falschen Wert')"

Lesson5_3_Name = "Listen umdrehen"





Lesson5_4_Text = "Lektion 5.4:\n\nOftmals ist es sehr praktisch zu prüfen, ob sich ein bestimmtes Element in einer Liste befindet, oder nicht. \n\n" \
                 "Dies können wir mit der Python-Funktion <in> prüfen -- zum Beispiel <'Stiefel' in gepaeck> ergibt True oder False, " \
                 "je nachdem, ob sich das Element 'Stiefel' in der Liste gepaeck befindet. \n\n\nSchreibe ein Programm, " \
                 "welches die Schnittmenge von 2 Listen in einer neuen Liste speichert und diese auf dem Bildschirm ausgibt.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson5_4_GivenCode =  "gepaeck_1 = ['Socken', 'Stiefel', 'Speer', 'Axt', 'Rose']" \
                        "\ngepaeck_2 = ['Muenzen', 'Socken', 'Axt', 'Schild', 'Stiefel']" \
                        "\nschnittmenge = []"

Lesson5_4_SolutionCode = "gepaeck_1 = ['Socken', 'Schuhe', 'Zahnbuerste', 'Pullover', 'Winterschuhe']" \
                        "\ngepaeck_2 = ['Buecher', 'Socken', 'Pullover', 'Schokolade', 'Schuhe']" \
                        "\nfor x in gepaeck_1:"\
                            "\n\tif x in gepaeck_2:"\
                                "\n\t\tschnittmenge.append(x)" \
                        "\nprint schnittmenge"

Lesson5_4_StringBoolean = True
Lesson5_4_SolutionOutput = "['Socken', 'Stiefel', 'Axt']"

Lesson5_4_AddedCodeBoolean = True
Lesson5_4_AddedCode = "\nif (gepaeck == ['Socken', 'Schuhe', 'Pullover']):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable gepaeck hat einen falschen Wert')"

Lesson5_4_Name = "Schnittmengen von Listen"






Lesson5_5_Text = "Lektion 5.5: \n\n" \
                 "In dieser Lektion lernen wir noch ein paar nützliche Befehle um mit Listen effizienter umzugehen. Der erste Befehl ist \n< listenname.sort() > \nDamit sortieren wir die Liste " \
                 "in aufsteigender Reihenfolge, egal ob in der Liste Zahlen oder Strings enthalten sind. \n\nDer zweite Befehl ist < listenname.reverse() >, hiermit können wir die Reihenfolge der Elemente in der Liste " \
                 "umdrehen, egal ob diese sortiert sind oder nicht. Die sortierte " \
                 "bzw. umgedrehte Liste müssen wir nicht in einer neuen Variablen speichern oder zuweisen, sie wird automatisch unter derselben Variable gespeichert. \n\n\n" \
                 "Der letzte Befehl den wir in dieser Lektion lernen ist < liste.pop() >. \n" \
                 "pop() entfernt das letzte Element aus der Liste und gibt es zurück, das heißt wir können es in einer Variable speichern:\n\n" \
                 "liste = [1,2,3]\n" \
                 "var1 = liste.pop()\n" \
                 "var 1 => 3\n" \
                 "liste => [1,2]\n" \
                 "liste.reverse()\n" \
                 "liste => [2,1]\n" \
                 "liste.sort()\n" \
                 "liste => [1,2]\n\n" \
                 "Aufgabe:\n" \
                 "Entferne aus der angegebenen Liste die größte, zweit-größte und kleinste Zahl mit dem pop-Befehl. Anschließend gebe zuerst die vorherige größte Zahl aus und dann " \
                 "die Liste 'Reihe', beginnend mit der aktuell größten Zahl."

Lesson5_5_GivenCode =  "Reihe = [1.3, 0.5, 6.7, 3, 5, 10.55, 10.5, 0.3]"

Lesson5_5_SolutionCode = "Reihe.sort()\n" \
                         "Reihe.pop()\n" \
                         "Reihe.reverse()\n" \
                         "b= Reihe.pop()\n" \
                         "Reihe.pop()\n" \
                         "print b\n" \
                         "print Reihe"

Lesson5_5_StringBoolean = True
Lesson5_5_SolutionOutput = "10.55\n[6.7, 5, 3, 1.3, 0.5]"

Lesson5_5_AddedCodeBoolean = True
Lesson5_5_AddedCode =   "\nif (Reihe == [6.7, 5, 3, 1.3, 0.5] ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable Reihe hat einen falschen Wert')" \


Lesson5_5_Name = "Listenmanipulation II"


Lesson5_6_Text = "Lektion 5.6:\n\nManchmal ist es ganz nützlich, wenn man die Anzahl gewisser Zeichen in einem String zählen kann.\n" \
                 "Strings funktionieren eigentlich wie Listen. Wir können für jedes Zeichen etwas testen, wenn wir wie bei den Listen " \
                 "mit einer for-Schleife <for x in String> statt jedem Element in einer Liste, jeden einzelnen Buchstaben eines Strings 'einmal in die Hand nehmen.'\n\nFür Vergleiche mit Strings " \
                 "benutzen wir den Vergleichsoperator <'a' == 'b'> (der uns in diesem Fall 'False' herausgeben würde).\n\n\n "\
		        "Suche dazu die Anzahl der 'e' und die der 'l' in dem Satz: 'Man belohnt seinen Lehrer schlecht, wenn man immer sein Schueler bleibt.' (Nietzsche). \n\n" \
                 "Gebe am Ende erst 'Anzahl der e: X' (mit angehängter Anzahl und Leerzeichen nach dem Doppelpunkt) aus und dann dasselbe mit 'l'. \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson5_6_GivenCode = "Text ='Man belohnt seinen Lehrer schlecht, wenn man immer sein Schueler bleibt.'"\
		       "\nanzahl_e=0"\
		       "\nanzahl_l=0" \
               "\n\n\n\n\n" \
               "\nstring_anzahl_e = str(anzahl_e)" \
               "\nprint 'Anzahl der e: ' + string_anzahl_e\n\n"

Lesson5_6_SolutionCode = "Text ='Man belohnt seinen Lehrer schlecht, wenn man immer sein Schueler bleibt.'"\
		          "anzahl_e=0"\
		          "anzahl_l=0"\
			  "for zeichen in Text:"\
				"if zeichen == 'e':"\
					"anzahl_e=anzahl_e+1"\
			  "print 'Anzahl der e: ', anzahl_e"\
			  "for zeichen in Text:"\
				"if zeichen == 'l':"\
					"anzahl_l=anzahl_l+1"\
			  "print 'Anzahl der l: ', anzahl_l"\

Lesson5_6_StringBoolean = True
Lesson5_6_SolutionOutput =  "Anzahl der e: 12" \
			                "\nAnzahl der l: 4"

Lesson5_6_AddedCodeBoolean = True
Lesson5_6_AddedCode = 	"\nif (anzahl_e == 12 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable anzahl_e hat einen falschen Wert')" \
                        "\nif (anzahl_l == 4 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable anzahl_l hat einen falschen Wert')"

Lesson5_6_Name = "Stringsuche"




Lesson6_0_Text = "Lektion 6.0 Methoden:\n\n" \
                 "Methoden sind feste Blöcke die einen bestimmten Nutzen abbilden, meist beschrieben mit ihrem Namen. " \
                 "Der Vorteil an ihnen ist, wir können sie öfters nutzen, aber jeweils mit unterschiedlichen Werten (=Parameter). Die Methode führt jedoch immer dasselbe " \
                 "aus.\nMethoden sind einfach aufgebaut: Es gibt einen Header der aus dem Kennzeichen für Methoden, einem Namen und eventuell Parametern besteht und einem 'Körper' der eingerückt ist. Sobald der " \
                 "Code nicht mehr eingerückt ist, kennzeichnet dies das Ende der Methode.\n\n" \
                 "def Methodenname (parameter1, parameter2):\n" \
                 "\t<eingerückter Block, >\n" \
                 "\t<Funktion der Methode >\n" \
                 "\t<eventuell mit Rückgabe: >\n" \
                 "\treturn value1\n\n" \
                 "Schreibe die Beispiel Funktion (rechts) so um, dass die Funktion das Quadrat des ersten Parameters berechnet und dann den zweiten Parameter (neu!) davon abzieht und mit <return> zurückgibt. " \
                 "Führe die Methode aus mit den Parametern 5 (=param.1) und 10(=param.2). Speicher die Rückgabe in der Variable <ergebnis> und gib sie aus.\n\n" \
                 "Die Parameter können beliebige Namen haben und wir können auf diese in der Methode zugreifen. Wir können keine, einen, oder mehrere Parameter haben. Bei keinem Parameter bleiben " \
                 "leere Klammern, bei mehreren trennen wir sie mit Kommata.\n\n" \
                 "Um die Methode auszuführen brauchen wir nur den Namen und die Parameter in Klammern zu schreiben. Falls die Methode etwas zurückgibt, weisen wir es einer \n" \
                 "Variable zu. "

Lesson6_0_GivenCode = "#Verändere den Methodennamen nicht, nur die Parameterliste!\n\n" \
                      "def ersteMethode(var1):\n" \
                      "\tvar3 = var1*2 -10\n\t\n" \
                      "\t#Methodenblöcke können beliebig lang sein,\n" \
                      "\t#müssen aber eingerückt sein bis die Methode zuende ist.\n\t\n" \
                      "\treturn var3\n" \
                      "\n" \
                      "\n" \
                      "ergebnis = ersteMethode(50)\n\n" \
                      "#Erst hier bei der tatsächlichen Ausführung\n" \
                      "#geben wir als Parameter reale Zahlen an. " \
                      "\n\nprint ergebnis\n\n\n\n"

Lesson6_0_SolutionCode = "def ersteMethode(var1, var2):\n" \
                         "\treturn var1*var1 - var2"

Lesson6_0_StringBoolean = True
Lesson6_0_SolutionOutput =  "15"

Lesson6_0_AddedCodeBoolean = True
Lesson6_0_AddedCode = 	"\nif (ergebnis == 15 ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Variable ergebnis hat einen falschen Wert')"

Lesson6_0_Name = "Methoden"



Lesson6_1_Text = "Lektion 6.0 Klassen:\n\n" \
                 "Klassen repräsentieren Datenstrukturen. Eine Klasse kann als Sammlung von Variablen und Methoden gesehen werden. \n" \
                 "Die Variablen beschreiben die Klasse, die Methoden stehen der Klasse zur Verfügung um die Variablen zu verändern oder etwas aufgrund der Klasse zu berechnen. " \
                 "Das Beispiel 'Mensch' als Klasse siehst du auf der rechten Seite. Die Eigenschaften werden durch die Variablen " \
                 "beschrieben. Eine Klasse kann beliebig viele Variablen haben. Entweder weisen wir den Variablen Default Werte zu, oder wir lassen sie leer (zb: farbe = ''). \n\n" \
                 "Mit den Methoden können wir die Variablen der Klasse (auch Attribute) verändern oder auch etwas ganz anderes machen. Auf Variablen und Methoden einer Klasse außerhalb (!) der Klasse wird immer auf dieselbe Art zugegriffen: \n\n" \
                 "KlassenObjektName.var1\n" \
                 "KlassenObjektName.methode1(parameter1)\n\n" \
                 "Innerhalb der Klasse können wir auf die eigenen Variablen mit <self.Variable> zugreifen. \n\n" \
                 "Bevor wir eine Klasse nutzen können müssen wir erst eine 'Instanz' von ihr mit eigenem Namen erzeugen. Wir wählen eine neue Variable und weisen der Klasse diese zu. Wir können mehrere Variablen der gleichen Klasse mit verschiedenen Namen erzeugen. " \
                 "\n\n" \
                 "Schreibe eine Klasse mit dem Namen 'Auto' und den Attributen: 'farbe', 'marke' und 'preis'. Wähle beliebige Werte für diese Attribute aus. Erzeuge ein Objekt der Klasse \n" \
                 "unter dem Namen 'meinErstesAuto'. Verändere die Farbe zu 'Rot' und gib sie danach aus."

Lesson6_1_GivenCode = "class Mensch:\n" \
                      "\t#Die KlassenAttribute und Methoden muessen eingerueckt werden!\n" \
                      "\thaarfarbe = ''\n" \
                      "\tweiblich = True\n\t\n" \
                      "\tdef färben(self, farbe):" \
                      "\n\t\t# 'self' ist kein Attribut, es bezieht sich nur auf die " \
                      "\n\t\t# aktuelle Instanz wenn wir die Methode einsetzen." \
                      "\n\t\tself.haarfarbe = farbe\n" \
                      "\n\t\t#Um auf ein Attribut der Klasse in der eigenen Methode\n" \
                      "\t\t#zuzugreifen schreiben wir: <self.Attribut>\n\n" \
                      "Laura = Mensch\n" \
                      "Charlie = Mensch\n" \
                      "Charlie.weiblich = False\n" \
                      "print Charlie.weiblich\n\n\n"

Lesson6_1_SolutionCode = ""

Lesson6_1_StringBoolean = True
Lesson6_1_SolutionOutput =  "Rot"

Lesson6_1_AddedCodeBoolean = True
Lesson6_1_AddedCode = 	"meinErstesAuto.marke\n" \
                        "meinErstesAuto.preis\n" \
                        "meinErstesAuto.farbe"

Lesson6_1_Name = "Klassen"






Lesson7_0_Text = "Lektion 7.0 While:\n\n" \
                 "Wir haben schon die for-Schleife gelernt, die jedes Element in einer Liste genau einmal 'in die Hand nimmt'. Jedoch brauchen wir manchmal auch eine Schleife die nicht auf Listen basiert. " \
                 "Aus diesem Grund gibt es die < while >-Schleife. \n" \
                 "Die <while>- Schleife funktionier ähnlich wie die for-Schleife, der Unterschied ist jedoch, dass wir nicht eine Liste einmal abarbeiten, sondern dass der eingerückte Block nur so lange immer wieder ausgeführt wird, wie der Vergleich " \
                 "zu <True> ausgewertet wird:\n\n" \
                 "x = 10" \
                 "\nwhile ( x < 0 ):" \
                 "\n\ty = x -2" \
                 "\n\tprint y" \
                 "\n\tx = x -1" \
                 "\n\n\n" \
                 "Aufgabe:" \
                 "Schreibe eine while-Schleife in der du von <100>  '3' abziehst wenn die Zahl gerade ist " \
                 "und '5' wenn die Zahl gerade ungerade ist, bis die ursprüngliche Zahl " \
                 "kleiner als 49 ist. " \
                 "\nGebe die Zahl am Ende mit <print> aus. " \
                 "\n\n\n" \
                 "Tipp: Du kannst mit Modulo herausfinden ob eine Zahl gerade oder ungerade ist. "


Lesson7_0_GivenCode = "\nx = 100 \n\n\n\n\n\n\n\n\n\n"

Lesson7_0_SolutionCode = ""

Lesson7_0_StringBoolean = True
Lesson7_0_SolutionOutput =  "44"

Lesson7_0_AddedCodeBoolean = False
Lesson7_0_AddedCode = 	""

Lesson7_0_Name = "while"



Lesson7_1_Text = "Lektion 7.1: Klassen II\n\n" \
                 "Schreibe die Klasse <Computer> mit den folgenden Variablen:" \
                 "\n" \
                 "\ntastatur (boolean) - False" \
                 "\nstrom (integer) - 750" \
                 "\neingeschalten (boolean) - False" \
                 "\ndesktopBereit (boolean) - False" \
                 "\n\n\nUnd den Methoden:" \
                 "\n\ncheckTastatur() - Gibt <True> oder <False> zurück, je nachdem ob die Tastatur angeschlossen ist. " \
                 "\n\neinschalten() - Schaltet den PC ein wenn <strom> zwischen 500 und 900 Watt ist und ruft dann <bootVorgang()> auf." \
                 "\n\nbootVorgang() - Der PC soll nur gebootet werden wenn eine Tastatur angeschlossen ist, wenn nein, dann fährt der PC wieder herunter, wenn ja, dann verändere <desktopBereit> auf <True>." \
                 "\n\nausschalten() - Fährt den PC herunter und setzt <desktopBereit> und <eingeschalten> auf <False>.  " \
                 "\n\n\nTipp: denke daran, dass Klassenmethoden mindestens den Parameter < self > haben müssen, mit dem auf die Instanz-eigenen Attribute zugegriffen und andere Klassenmethoden aufgerufen werden können.\n\n" \
                 "Beispiel:\n\n" \
                 "self.methode2( )\n" \
                 "self.variable1\n"



Lesson7_1_GivenCode = "\n\n\n\n\n\n\n\n\n\n\n\n"

Lesson7_1_SolutionCode = ""

Lesson7_1_StringBoolean = False
Lesson7_1_SolutionOutput =  ""

Lesson7_1_AddedCodeBoolean = True
Lesson7_1_AddedCode = 	"\n pc = Computer" \
                         "\nif (pc.strom != None ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Die Klasse Computer hat kein Attribut <Strom>.')" \
                         "\nif (pc.eingeschalten != None ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Die Klasse Computer hat kein Attribut <eingeschalten>.')" \
                         "\nif (pc.desktopBereit != None ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Die Klasse Computer hat kein Attribut <desktopBereit>.')" \
                         "\nif (pc.tastatur != None ):\n\t1+1\nelse:\n\tErrorlist.append('Error: Die Klasse Computer hat kein Attribut <Tastatur>.')"

Lesson7_1_Name = "while"

















########## Set Global Variables for the coding part of the game #######
global textfield
textfield = ""
cmdfield = "-----Kommandozeile-----"

global Errorlist
Errorlist = []
global GlobalOutput
GlobalOutput = ""

########### FUNCTIONS ###########

def retrieve_input():
    # Description: Take input from the Textfield in which the user codes.
    # - saves it in the global variable for access
    # Parameters: None
    # Returns: None
    global textfield
    textfield = txt.get(1.0,END)

def get_cmd():
    # Description: Get Text from command_line_field and save it in a global variable for access
    # Parameters: None
    # Returns: None
    global cmdfield
    cmdfield = cmd.get(1.0,END)

def set_cmd():
    # Description: Sets the command line (at the beginning of a lesson - afterwards we need some more stuff in there)
    # Parameters: None
    # Returns: None
    global cmdfield
    cmdfield = "-----Kommandozeile-----"
    cmd.configure(state='normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------",END)
    cmd.configure(state='disabled')


def reset():
    # Description: Resets code to original state at the beginning of the specific lesson
    # Parameters: None
    # Returns: None

    # Accessing the following global variables:
    global current_Lesson
    global Lesson0_0_GivenCode
    global Lesson1_0_GivenCode
    global Lesson1_1_GivenCode
    global Lesson1_2_GivenCode
    global Lesson2_0_GivenCode
    global Lesson2_1_GivenCode
    global Lesson3_0_GivenCode
    global Lesson3_1_GivenCode
    global Lesson3_2_GivenCode
    global Lesson4_1_GivenCode
    global Lesson4_2_GivenCode
    global Lesson5_0_GivenCode
    global Lesson5_1_GivenCode
    global Lesson5_2_GivenCode
    global Lesson5_3_GivenCode
    global Lesson5_4_GivenCode
    global Lesson5_5_GivenCode
    global Lesson5_6_GivenCode
    global Lesson6_0_GivenCode
    global Lesson6_1_GivenCode

    # Clear Code
    txt.delete(1.0,'end')

    if current_Lesson == (-1):
		txt.insert(1.0,Lesson0_0_GivenCode, END)
    elif current_Lesson == 0:
        txt.insert(1.0,Lesson0_1_GivenCode, END)
    elif current_Lesson == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    elif current_Lesson == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    elif current_Lesson == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    elif current_Lesson == 5:
        txt.insert(1.0,Lesson2_0_GivenCode, END)
    elif current_Lesson == 6:
        txt.insert(1.0,Lesson2_1_GivenCode, END)
    elif current_Lesson == 8:
        txt.insert(1.0,Lesson3_0_GivenCode, END)
    elif current_Lesson == 9:
        txt.insert(1.0,Lesson3_1_GivenCode, END)
    elif current_Lesson == 10:
        txt.insert(1.0,Lesson3_2_GivenCode, END)
    elif current_Lesson == 12:
        txt.insert(1.0,Lesson4_1_GivenCode, END)
    elif current_Lesson == 13:
        txt.insert(1.0,Lesson4_2_GivenCode, END)
    elif current_Lesson == 14:
        txt.insert(1.0,Lesson5_0_GivenCode, END)
    elif current_Lesson == 15:
        txt.insert(1.0,Lesson5_1_GivenCode, END)
    elif current_Lesson == 16:
        txt.insert(1.0,Lesson5_2_GivenCode, END)
    elif current_Lesson == 17:
        txt.insert(1.0,Lesson5_3_GivenCode, END)
    elif current_Lesson == 18:
        txt.insert(1.0,Lesson5_4_GivenCode, END)
    elif current_Lesson == 19:
        txt.insert(1.0,Lesson5_5_GivenCode, END)
    elif current_Lesson == 20:
        txt.insert(1.0,Lesson5_6_GivenCode, END)
    elif current_Lesson == 21:
        txt.insert(1.0,Lesson6_0_GivenCode, END)
    elif current_Lesson == 22:
        txt.insert(1.0,Lesson6_1_GivenCode, END)




def checkStringCode(output_Solution):
    # Description: Checks if the output was right (String based)
    #   This function is completely generic and works with the lesson datasets
    # Parameters: the specific solution to the lesson
    # Returns: None
    global Errorlist
    global GlobalOutput
    Errorlist=[]
    bb = True
    cc = True

    # Delete following tabs, blanks and newlines of the GlobalOutput
    # Had an bug here with an endless loop when I used a while-loop.
    # So I decided to do this 5 times. should be enough.
    # Same down below for the leading characters.
    for x in [1,2,3,4,5]:

            if not GlobalOutput == "" :

                a = GlobalOutput[len(GlobalOutput)-1]
                if a == " " or a == "\t" or a == "\n":
                    GlobalOutput = GlobalOutput[0:len(GlobalOutput)-1]

    # Deleting leading newlines of the GlobalOutput
    for x in [1,2,3,4,5]:
        if not GlobalOutput == "" :
            a = GlobalOutput[0]
            if a == "\n":
                GlobalOutput = GlobalOutput[1:len(GlobalOutput)]

    if GlobalOutput != output_Solution:
        Errorlist.append("Die Ausgabe ist nicht korrekt!")



def checkRunCode():
    # Description: Checks if the code is:
    #   - executable,
    #   - if variables have the right value and
    #   - if the output is correct.
    # This function is the key-element of the coding part of the game.
    #
    # Parameters: None
    # Returns: None - Does it all internally.

    # Global Variables for access
    global cmdfield
    global textfield
    global Errorlist
    global GlobalOutput
    global Lesson_Number
    global button1


    global Lesson0_0_StringBoolean
    global Lesson0_0_SolutionOutput#
    global Lesson0_0_AddedCodeBoolean
    global Lesson0_0_AddedCode

    global Lesson0_1_StringBoolean
    global Lesson0_1_SolutionOutput#
    global Lesson0_1_AddedCodeBoolean
    global Lesson0_1_AddedCode

    global Lesson1_0_StringBoolean
    global Lesson1_0_SolutionOutput#
    global Lesson1_0_AddedCodeBoolean
    global Lesson1_0_AddedCode

    global Lesson1_1_StringBoolean
    global Lesson1_1_SolutionOutput#
    global Lesson1_1_AddedCodeBoolean
    global Lesson1_1_AddedCode

    global Lesson1_2_StringBoolean
    global Lesson1_2_SolutionOutput#
    global Lesson1_2_AddedCodeBoolean
    global Lesson1_2_AddedCode

    global Lesson2_0_StringBoolean
    global Lesson2_0_SolutionOutput#
    global Lesson2_0_AddedCodeBoolean
    global Lesson2_0_AddedCode

    global Lesson2_1_StringBoolean
    global Lesson2_1_SolutionOutput#
    global Lesson2_1_AddedCodeBoolean
    global Lesson2_1_AddedCode


    global Lesson3_0_StringBoolean
    global Lesson3_0_SolutionOutput#
    global Lesson3_0_AddedCodeBoolean
    global Lesson3_0_AddedCode

    global Lesson3_1_StringBoolean
    global Lesson3_1_SolutionOutput#
    global Lesson3_1_AddedCodeBoolean
    global Lesson3_1_AddedCode

    global Lesson3_2_StringBoolean
    global Lesson3_2_SolutionOutput#
    global Lesson3_2_AddedCodeBoolean
    global Lesson3_2_AddedCode

    global Lesson4_1_StringBoolean
    global Lesson4_1_SolutionOutput#
    global Lesson4_1_AddedCodeBoolean
    global Lesson4_1_AddedCode

    global Lesson4_2_StringBoolean
    global Lesson4_2_SolutionOutput#
    global Lesson4_2_AddedCodeBoolean
    global Lesson4_2_AddedCode

    global Lesson5_0_StringBoolean
    global Lesson5_0_SolutionOutput#
    global Lesson5_0_AddedCodeBoolean
    global Lesson5_0_AddedCode

    global Lesson5_1_StringBoolean
    global Lesson5_1_SolutionOutput#
    global Lesson5_1_AddedCodeBoolean
    global Lesson5_1_AddedCode

    global Lesson5_2_StringBoolean
    global Lesson5_2_SolutionOutput#
    global Lesson5_2_AddedCodeBoolean
    global Lesson5_2_AddedCode

    global Lesson5_3_StringBoolean
    global Lesson5_3_SolutionOutput#
    global Lesson5_3_AddedCodeBoolean
    global Lesson5_3_AddedCode

    global Lesson5_4_StringBoolean
    global Lesson5_4_SolutionOutput#
    global Lesson5_4_AddedCodeBoolean
    global Lesson5_4_AddedCode

    global Lesson5_5_StringBoolean
    global Lesson5_5_SolutionOutput#
    global Lesson5_5_AddedCodeBoolean
    global Lesson5_5_AddedCode

    global Lesson5_6_StringBoolean
    global Lesson5_6_SolutionOutput#
    global Lesson5_6_AddedCodeBoolean
    global Lesson5_6_AddedCode

    global Lesson6_0_StringBoolean
    global Lesson6_0_SolutionOutput#
    global Lesson6_0_AddedCodeBoolean
    global Lesson6_0_AddedCode

    global Lesson6_1_StringBoolean
    global Lesson6_1_SolutionOutput#
    global Lesson6_1_AddedCodeBoolean
    global Lesson6_1_AddedCode

    # Set working variables
    StringBoolean = ""
    SolutionOutput = ""
    AddedCodeBoolean = ""
    AddedCode = ""

    # Set all variables important for the code checking depending on the specific lection.
    if current_Lesson == (-1):
        StringBoolean = Lesson0_0_StringBoolean
        SolutionOutput = Lesson0_0_SolutionOutput
        AddedCodeBoolean = Lesson0_0_AddedCodeBoolean
        AddedCode = Lesson0_0_AddedCode

    if current_Lesson == 0:
        StringBoolean = Lesson0_1_StringBoolean
        SolutionOutput = Lesson0_1_SolutionOutput
        AddedCodeBoolean = Lesson0_1_AddedCodeBoolean
        AddedCode = Lesson0_1_AddedCode

    if current_Lesson == 1:
        StringBoolean = Lesson1_0_StringBoolean
        SolutionOutput = Lesson1_0_SolutionOutput
        AddedCodeBoolean = Lesson1_0_AddedCodeBoolean
        AddedCode = Lesson1_0_AddedCode

    if current_Lesson == 2:
        StringBoolean = Lesson1_1_StringBoolean
        SolutionOutput = Lesson1_1_SolutionOutput
        AddedCodeBoolean = Lesson1_1_AddedCodeBoolean
        AddedCode = Lesson1_1_AddedCode


    if current_Lesson == 3:
        StringBoolean = Lesson1_2_StringBoolean
        SolutionOutput = Lesson1_2_SolutionOutput
        AddedCodeBoolean = Lesson1_2_AddedCodeBoolean
        AddedCode = Lesson1_2_AddedCode

    if current_Lesson == 5:
        StringBoolean = Lesson2_0_StringBoolean
        SolutionOutput = Lesson2_0_SolutionOutput
        AddedCodeBoolean = Lesson2_0_AddedCodeBoolean
        AddedCode = Lesson2_0_AddedCode

    if current_Lesson == 6:
        StringBoolean = Lesson2_1_StringBoolean
        SolutionOutput = Lesson2_1_SolutionOutput
        AddedCodeBoolean = Lesson2_1_AddedCodeBoolean
        AddedCode = Lesson2_1_AddedCode


    if current_Lesson == 8:
        StringBoolean = Lesson3_0_StringBoolean
        SolutionOutput = Lesson3_0_SolutionOutput
        AddedCodeBoolean = Lesson3_0_AddedCodeBoolean
        AddedCode = Lesson3_0_AddedCode

    if current_Lesson == 9:
        StringBoolean = Lesson3_1_StringBoolean
        SolutionOutput = Lesson3_1_SolutionOutput
        AddedCodeBoolean = Lesson3_1_AddedCodeBoolean
        AddedCode = Lesson3_1_AddedCode

    if current_Lesson == 10:
        StringBoolean = Lesson3_2_StringBoolean
        SolutionOutput = Lesson3_2_SolutionOutput
        AddedCodeBoolean = Lesson3_2_AddedCodeBoolean
        AddedCode = Lesson3_2_AddedCode

    if current_Lesson == 12:
        StringBoolean = Lesson4_1_StringBoolean
        SolutionOutput = Lesson4_1_SolutionOutput
        AddedCodeBoolean = Lesson4_1_AddedCodeBoolean
        AddedCode = Lesson4_1_AddedCode

    if current_Lesson == 13:
        StringBoolean = Lesson4_2_StringBoolean
        SolutionOutput = Lesson4_2_SolutionOutput
        AddedCodeBoolean = Lesson4_2_AddedCodeBoolean
        AddedCode = Lesson4_2_AddedCode

    if current_Lesson == 14:
        StringBoolean = Lesson5_0_StringBoolean
        SolutionOutput = Lesson5_0_SolutionOutput
        AddedCodeBoolean = Lesson5_0_AddedCodeBoolean
        AddedCode = Lesson5_0_AddedCode

    if current_Lesson == 15:
        StringBoolean = Lesson5_1_StringBoolean
        SolutionOutput = Lesson5_1_SolutionOutput
        AddedCodeBoolean = Lesson5_1_AddedCodeBoolean
        AddedCode = Lesson5_1_AddedCode

    if current_Lesson == 16:
        StringBoolean = Lesson5_2_StringBoolean
        SolutionOutput = Lesson5_2_SolutionOutput
        AddedCodeBoolean = Lesson5_2_AddedCodeBoolean
        AddedCode = Lesson5_2_AddedCode

    if current_Lesson == 17:
        StringBoolean = Lesson5_3_StringBoolean
        SolutionOutput = Lesson5_3_SolutionOutput
        AddedCodeBoolean = Lesson5_3_AddedCodeBoolean
        AddedCode = Lesson5_3_AddedCode

    if current_Lesson == 18:
        StringBoolean = Lesson5_4_StringBoolean
        SolutionOutput = Lesson5_4_SolutionOutput
        AddedCodeBoolean = Lesson5_4_AddedCodeBoolean
        AddedCode = Lesson5_4_AddedCode

    if current_Lesson == 19:
        StringBoolean = Lesson5_5_StringBoolean
        SolutionOutput = Lesson5_5_SolutionOutput
        AddedCodeBoolean = Lesson5_5_AddedCodeBoolean
        AddedCode = Lesson5_5_AddedCode

    if current_Lesson == 20:
        StringBoolean = Lesson5_6_StringBoolean
        SolutionOutput = Lesson5_6_SolutionOutput
        AddedCodeBoolean = Lesson5_6_AddedCodeBoolean
        AddedCode = Lesson5_6_AddedCode

    if current_Lesson == 21:
        StringBoolean = Lesson6_0_StringBoolean
        SolutionOutput = Lesson6_0_SolutionOutput
        AddedCodeBoolean = Lesson6_0_AddedCodeBoolean
        AddedCode = Lesson6_0_AddedCode

    if current_Lesson == 22:
        StringBoolean = Lesson6_1_StringBoolean
        SolutionOutput = Lesson6_1_SolutionOutput
        AddedCodeBoolean = Lesson6_1_AddedCodeBoolean
        AddedCode = Lesson6_1_AddedCode





    Errorlist = []
    # Enable access to the command window
    cmd.configure(state='normal')

    # Get the code
    code = txt.get(1.0,END)

    # create file-like string to capture output
    codeOut = StringIO.StringIO()
    codeErr = StringIO.StringIO()

    # capture output and errors
    sys.stdout = codeOut
    sys.stderr = codeErr

    # Try to execute print. If the code is not executable we
    # send the error to the command line of the game.
    try:
        exec code
    except:
        print "Unexpected error:", sys.exc_info()[0]


    # restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    codeOutput = ""  # Fixed an old bug. Probably deprecated by now.
    codeErrors = ""
    codeErrors = codeErr.getvalue()
    codeOutput = codeOut.getvalue()
    print "Code Errors: \n" +codeErrors
    # For String checking
    GlobalOutput = codeOutput

    # Close pipe to executed programm.
    codeOut.close()
    codeErr.close()

    # Set first line of the command line
    cmdfield = "------------------------------Kommandozeile------------------------------\n"

    errorValue = "" # If any errors appear we save them in here. If its empty, the player must have done everything right
    # Display negative Results (errors)

    if codeErrors == "":
               # code is executable without errors
        if StringBoolean: # depends on the lesson. For some lessons we might dont want to check String-based.
            # Check string-based output solution.
            checkStringCode(SolutionOutput)

        if AddedCodeBoolean: # depends on the lesson. For some lessons we might dont want to check variable-based.
            # Check values of important variables
            addCode(AddedCode)

        if Errorlist != []:
            # Errors found during variable value/string code check
            for x in Errorlist:
                errorValue = errorValue + x + "\n" # each error should be in a new line

            cmdfield = cmdfield + "### Fehler! #### \n%s\n" % errorValue # Print the errors.
    else:
        # Errors found during execution
        cmdfield = cmdfield + "### Fehler! ### \n%s\n" % codeErrors # Display Syntax Errors etc

    message = "" # initialize

    # Display positive results
    if codeErrors == "" and errorValue == "":
        message = "Gut gemacht! Klicke auf 'Weiter' um die nächste Aufgabe zu beginnen!"
        if current_Lesson == Lesson_Number:
            button.destroy() # Destroy check Code button
        if (button1.winfo_exists() == 0): # If we are not in an archived lesson we now need to display the continue button
            button1 = Button(root, text='Weiter', command = nextLesson )
            button1.grid(row=30, column=3) # button placement

    # Display messages to the Command Line
    cmdfield = cmdfield + "### Ausgabe #### \n%s\n" % codeOutput
    cmdfield = cmdfield + "\n" + message
    cmd.delete(1.0,'end') # Delete whatever was there before
    cmd.insert(1.0,cmdfield, END) # Insert current results
    cmd.configure(state='disabled') # close window access
    codeErrors == ""
    errorValue == ""

# check variable values
def addCode(addedCode):
    # Description: This function is part of the code control.
    # We add code which checks the variable for the correct value
    # Parameters: added Code (specific to lesson we have extra code which checks the variables.
    # These are contained in the string data for the lessons at the top of the file.
    # Returns: None
    global cmdfield
    global textfield
    global Errorlist

    # Get code from window
    textfield= txt.get(1.0,END)
    textfield = textfield + addedCode # Add code

    # Open file to be able to execute again, this time with our own code
    codeOut2 = StringIO.StringIO()
    codeErr2 = StringIO.StringIO()

    code = textfield

    sys.stdout2 = codeOut2
    sys.stderr2 = codeErr2

    # The followin part will send an error review if: the value wasnt correct / the variable didnt exist (or our code was faulty!)
    try:
        exec code
    except:
        print "Unexpected error:", sys.exc_info()[0]

    sys.stdout2 = sys.__stdout__
    sys.stderr2 = sys.__stderr__

    # all errors were reported earlier so we dont need to check again.

    codeOut2.close()
    codeErr2.close()


def nextLesson():
    # Description: Continue to the next lesson and prepare all variables for it
    # Parameters: None
    # Returns: None

    # Global variables for access
    global current_Lesson
    global Lesson_Number
    global maxLessons
    global button1
    global button
    global current_Lesson
    global Lesson0_0_Text
    global Lesson0_1_Text
    global Lesson1_0_Text
    global Lesson1_1_Text
    global Lesson1_2_Text
    global Lesson2_0_Text
    global Lesson2_1_Text
    global Lesson3_0_Text
    global Lesson3_1_Text
    global Lesson3_2_Text
    global Lesson4_1_Text
    global Lesson4_2_Text
    global Lesson5_0_Text
    global Lesson5_1_Text
    global Lesson5_2_Text
    global Lesson5_3_Text
    global Lesson5_4_Text
    global Lesson5_5_Text
    global Lesson5_6_Text
    global Lesson6_0_Text
    global Lesson6_1_Text
    global Lesson7_0_Text
    global Lesson7_1_Text
    global Lesson0_0_GivenCode
    global Lesson0_1_GivenCode
    global Lesson1_0_GivenCode
    global Lesson1_1_GivenCode
    global Lesson1_2_GivenCode
    global Lesson2_0_GivenCode
    global Lesson2_1_GivenCode
    global Lesson3_0_GivenCode
    global Lesson3_1_GivenCode
    global Lesson3_2_GivenCode
    global Lesson4_1_GivenCode
    global Lesson4_2_GivenCode
    global Lesson5_0_GivenCode
    global Lesson5_1_GivenCode
    global Lesson5_2_GivenCode
    global Lesson5_3_GivenCode
    global Lesson5_4_GivenCode
    global Lesson5_5_GivenCode
    global Lesson5_6_GivenCode
    global Lesson6_0_GivenCode
    global Lesson6_1_GivenCode
    global Lesson7_0_GivenCode
    global Lesson7_1_GivenCode

    # Lesson_Number is only increased if we actually successfully completed the task we were
    #   supposed to do next. It shouldnt count up if we do the first lesson over and over again.
    # current_lesson controls the current window & tasks with all background data (check codes etc)
    # Lesson_Number controls the archive function (how many lessons it shows) and when the player can
    #   continue to play
    if Lesson_Number == current_Lesson:
        Lesson_Number+= 1
        current_Lesson += 1
    else:
        current_Lesson +=1

    # After the lessons 0,5,8,10,12,18 we want to continue playing
    # First we reset the communication file to signal the end of
    # the coding. (on_closing() )

    if current_Lesson ==1:
        on_closing()
        sys.exit(0)
    elif current_Lesson == 4:
        on_closing()
        sys.exit(0)
    elif current_Lesson == 7:
        on_closing()
        sys.exit(0)
    elif current_Lesson == 11:
        on_closing()
        sys.exit(0)
    elif current_Lesson == 14:
        on_closing()
        sys.exit(0)
    elif current_Lesson == 18:
        on_closing()
        sys.exit(0)
    elif current_Lesson ==21:
        on_closing()
        sys.exit(0)
    elif current_Lesson == 23:
        on_closing()
        sys.exit(0)
    elif current_Lesson == 25:
        on_closing()
        sys.exit(0)

    # In case we count too high, we reset. Probably deprecated by now, as we controlled it very carefully
    # when and at what point the lesson counter/current counter goes up.
    if current_Lesson > maxLessons:
        current_Lesson = maxLessons
    if Lesson_Number > maxLessons:
        Lesson_Number = maxLessons

    # Set check Code Button in the next lesson
    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=30, column = 1)

    # Reset the Command Window
    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    # Change Text (instructions to the lessons)
    if current_Lesson == (-1):
        label1.config(text=Lesson0_0_Text)
    if current_Lesson == 0:
        label1.config(text=Lesson0_1_Text)
    if current_Lesson == 1:
        label1.config(text= Lesson1_0_Text)
    if current_Lesson == 2:
        label1.config(text= Lesson1_1_Text)
    if current_Lesson == 3:
        label1.config(text= Lesson1_2_Text)
    if current_Lesson == 5:
        label1.config(text= Lesson2_0_Text)
    if current_Lesson == 6:
        label1.config(text= Lesson2_1_Text)
    if current_Lesson == 8:
        label1.config(text= Lesson3_0_Text)
    if current_Lesson == 9:
        label1.config(text= Lesson3_1_Text)
    if current_Lesson == 10:
        label1.config(text= Lesson3_2_Text)
    if current_Lesson == 12:
        label1.config(text= Lesson4_1_Text)
    if current_Lesson == 13:
        label1.config(text= Lesson4_2_Text)
    if current_Lesson == 14:
        label1.config(text= Lesson5_0_Text)
    if current_Lesson == 15:
        label1.config(text= Lesson5_1_Text)
    if current_Lesson == 16:
        label1.config(text= Lesson5_2_Text)
    if current_Lesson == 17:
        label1.config(text= Lesson5_3_Text)
    if current_Lesson == 18:
        label1.config(text= Lesson5_4_Text)
    if current_Lesson == 19:
        label1.config(text= Lesson5_5_Text)
    if current_Lesson == 20:
        label1.config(text= Lesson5_6_Text)
    if current_Lesson == 21:
        label1.config(text= Lesson6_0_Text)
    if current_Lesson == 22:
        label1.config(text= Lesson6_1_Text)
    if current_Lesson == 23:
        label1.config(text= Lesson7_0_Text)
    if current_Lesson == 24:
        label1.config(text= Lesson7_1_Text)
    # Change given Code
    txt.delete(1.0,'end')

    if current_Lesson == (-1):
		txt.insert(1.0,Lesson0_0_GivenCode, END)
    elif current_Lesson == 0:
        txt.insert(1.0,Lesson0_1_GivenCode, END)
    elif current_Lesson == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    elif current_Lesson == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    elif current_Lesson == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    elif current_Lesson == 5:
        txt.insert(1.0,Lesson2_0_GivenCode, END)
    elif current_Lesson == 6:
        txt.insert(1.0,Lesson2_1_GivenCode, END)
    elif current_Lesson == 8:
        txt.insert(1.0,Lesson3_0_GivenCode, END)
    elif current_Lesson == 9:
        txt.insert(1.0,Lesson3_1_GivenCode, END)
    elif current_Lesson == 10:
        txt.insert(1.0,Lesson3_2_GivenCode, END)
    elif current_Lesson == 12:
        txt.insert(1.0,Lesson4_1_GivenCode, END)
    elif current_Lesson == 13:
        txt.insert(1.0,Lesson4_2_GivenCode, END)
    elif current_Lesson == 14:
        txt.insert(1.0,Lesson5_0_GivenCode, END)
    elif current_Lesson == 15:
        txt.insert(1.0,Lesson5_1_GivenCode, END)
    elif current_Lesson == 16:
        txt.insert(1.0,Lesson5_2_GivenCode, END)
    elif current_Lesson == 17:
        txt.insert(1.0,Lesson5_3_GivenCode, END)
    elif current_Lesson == 18:
        txt.insert(1.0,Lesson5_4_GivenCode, END)
    elif current_Lesson == 19:
        txt.insert(1.0,Lesson5_5_GivenCode, END)
    elif current_Lesson == 20:
        txt.insert(1.0,Lesson5_6_GivenCode, END)
    elif current_Lesson == 21:
        txt.insert(1.0,Lesson6_0_GivenCode, END)
    elif current_Lesson == 22:
        txt.insert(1.0,Lesson6_1_GivenCode, END)
    elif current_Lesson == 23:
        txt.insert(1.0,Lesson7_0_GivenCode, END)
    elif current_Lesson == 24:
        txt.insert(1.0,Lesson7_1_GivenCode, END)
    button1.destroy()



def reinstate_buttons():
    # Description: Sets the buttons in each lesson (check Code, Archive, Reset Code)
    # Parameters: None
    # Returns: None

    # Access to global variables
    global button
    global button2
    global button3

    # Resets Command line window
    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.insert(1.0,"------------------------------Kommandozeile------------------------------","end")
    cmd.configure(state='disabled')

    # Resets buttons
    button = Button(root, text='Check Code', command=checkRunCode )
    button.grid(row=30, column = 1)
    button2 = Button(root, text ='Archiv', command = archive )
    button2.grid(row=30, column = 2)
    button3 = Button (root, text='Reset Code', command=reset )
    button3.grid(row =30, column = 6)



# The following applies to all lesson0-17 functions as the functionality is basically the same.

# Description:
#  They are used in the archive function to load the new lesson.
#   - delete all buttons which are left
#   - set the current_lesson to the new
#   - delete all left over code in the coding window
#   - set the given_code specific to the lesson in the coding window
#   - reinstate all buttons needed for the next lesson

# Parameters: None
# Returns: None

# Note: the following lessons probably could be refactored into one big lesson.
#       With a parameter setting the current_lesson and a huge if-elif clause for the
#       setting of the given code/text etc.



def lesson0():
    global button
    global button1
    global button2
    global button3
    global current_Lesson
    global Lesson0_0_Text
    global Lesson0_0_GivenCode
    # set current lesson
    current_Lesson = 0
    # delete buttons
    deletebuttons()
    # set given code
    label1.config(text= Lesson0_0_Text)
    txt.delete(1.0,END)
    txt.insert(1.0,Lesson0_0_GivenCode, END)
    # reinstate buttons
    reinstate_buttons()


def lesson1():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_0_Text
    global Lesson1_0_GivenCode

    current_Lesson = 1
    deletebuttons()

    label1.config(text= Lesson1_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_0_GivenCode, END)

    reinstate_buttons()


def lesson2():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_1_Text
    global Lesson1_1_GivenCode

    current_Lesson = 2
    deletebuttons()

    label1.config(text= Lesson1_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_1_GivenCode, END)

    reinstate_buttons()


def lesson3():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson1_2_Text
    global Lesson1_2_GivenCode

    current_Lesson = 3
    deletebuttons()

    label1.config(text= Lesson1_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson1_2_GivenCode, END)

    reinstate_buttons()



def lesson5():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson2_0_Text
    global Lesson2_0_GivenCode

    deletebuttons()

    current_Lesson = 5
    label1.config(text= Lesson2_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson2_0_GivenCode, END)

    reinstate_buttons()

def lesson6():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson2_1_Text
    global Lesson2_1_GivenCode

    current_Lesson = 6
    deletebuttons()

    label1.config(text= Lesson2_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson2_1_GivenCode, END)

    reinstate_buttons()



def lesson8():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson3_0_Text
    global Lesson3_0_GivenCode

    deletebuttons()

    current_Lesson = 8
    label1.config(text= Lesson3_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson3_0_GivenCode, END)

    reinstate_buttons()


def lesson9():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson3_1_Text
    global Lesson3_1_GivenCode

    deletebuttons()

    current_Lesson = 9
    label1.config(text= Lesson3_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson3_1_GivenCode, END)

    reinstate_buttons()

def lesson10():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson3_2_Text
    global Lesson3_2_GivenCode

    deletebuttons()

    current_Lesson = 10
    label1.config(text= Lesson3_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson3_2_GivenCode, END)

    reinstate_buttons()




def lesson12():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson4_1_Text
    global Lesson4_1_GivenCode

    deletebuttons()

    current_Lesson = 12
    label1.config(text= Lesson4_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson4_1_GivenCode, END)

    reinstate_buttons()


def lesson13():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson4_2_Text
    global Lesson4_2_GivenCode

    deletebuttons()

    current_Lesson = 13
    label1.config(text= Lesson4_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson4_2_GivenCode, END)

    reinstate_buttons()



def lesson14():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_0_Text
    global Lesson5_0_GivenCode

    deletebuttons()

    current_Lesson = 14
    label1.config(text= Lesson5_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_0_GivenCode, END)

    reinstate_buttons()



def lesson15():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_1_Text
    global Lesson5_1_GivenCode

    deletebuttons()

    current_Lesson = 15
    label1.config(text= Lesson5_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_1_GivenCode, END)

    reinstate_buttons()


def lesson16():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_2_Text
    global Lesson5_2_GivenCode

    deletebuttons()

    current_Lesson = 16
    label1.config(text= Lesson5_2_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_2_GivenCode, END)

    reinstate_buttons()


def lesson17():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_3_Text
    global Lesson5_3_GivenCode

    deletebuttons()

    current_Lesson = 17
    label1.config(text= Lesson5_3_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_3_GivenCode, END)

    reinstate_buttons()



def lesson18():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_4_Text
    global Lesson5_4_GivenCode

    deletebuttons()

    current_Lesson = 18
    label1.config(text= Lesson5_4_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_4_GivenCode, END)

    reinstate_buttons()


def lesson19():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_5_Text
    global Lesson5_5_GivenCode

    deletebuttons()

    current_Lesson = 19
    label1.config(text= Lesson5_5_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_5_GivenCode, END)

    reinstate_buttons()


def lesson20():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson5_6_Text
    global Lesson5_6_GivenCode

    deletebuttons()

    current_Lesson = 20
    label1.config(text= Lesson5_6_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson5_6_GivenCode, END)

    reinstate_buttons()


def lesson21():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson6_0_Text
    global Lesson6_0_GivenCode

    deletebuttons()

    current_Lesson = 21
    label1.config(text= Lesson6_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson6_0_GivenCode, END)

    reinstate_buttons()



def lesson22():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson6_1_Text
    global Lesson6_1_GivenCode

    deletebuttons()

    current_Lesson = 22
    label1.config(text= Lesson6_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson6_1_GivenCode, END)

    reinstate_buttons()


def lesson23():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson7_0_Text
    global Lesson7_0_GivenCode

    deletebuttons()

    current_Lesson = 23
    label1.config(text= Lesson7_0_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson7_0_GivenCode, END)

    reinstate_buttons()


def lesson24():
    global current_Lesson
    global button
    global button1
    global button2
    global button3
    global Lesson7_0_Text
    global Lesson7_0_GivenCode

    deletebuttons()

    current_Lesson = 24
    label1.config(text= Lesson7_1_Text)

    txt.delete(1.0,END)
    txt.insert(1.0,Lesson7_1_GivenCode, END)

    reinstate_buttons()



def deletebuttons():
    # Description: Deletes all buttons of the lessons we have completed
    #       and which are shown in the archive function (based on lesson_number)
    #       This is necessary so we dont delete a button that wasnt even there in
    #       the beginning as the player didnt have access to the lesson yet
    # Parameters: None
    # Returns: None

    global Lesson_Number
    global buttonlesson0
    global buttonlesson1
    global buttonlesson2
    global buttonlesson3
    global buttonlesson5
    global buttonlesson6
    global buttonlesson8
    global buttonlesson9
    global buttonlesson10
    global buttonlesson12
    global buttonlesson13
    global buttonlesson13
    global buttonlesson14
    global buttonlesson15
    global buttonlesson16
    global buttonlesson17
    global buttonlesson18
    global buttonlesson19

    if Lesson_Number >= -1:
        buttonlesson0.destroy()
    if Lesson_Number >= 1:
        buttonlesson1.destroy()
    if Lesson_Number >= 2:
        buttonlesson2.destroy()
    if Lesson_Number >= 3:
        buttonlesson3.destroy()
    if Lesson_Number >= 5:
        buttonlesson5.destroy()
    if Lesson_Number >= 6:
        buttonlesson6.destroy()
    if Lesson_Number >= 8:
        buttonlesson8.destroy()
    if Lesson_Number >= 9:
        buttonlesson9.destroy()
    if Lesson_Number >= 10:
        buttonlesson10.destroy()
    if Lesson_Number >= 12:
        buttonlesson12.destroy()
    if Lesson_Number >= 13:
        buttonlesson13.destroy()
    if Lesson_Number >= 14:
        buttonlesson14.destroy()
    if Lesson_Number >= 15:
        buttonlesson15.destroy()
    if Lesson_Number >= 16:
        buttonlesson16.destroy()
    if Lesson_Number >= 17:
        buttonlesson17.destroy()
    if Lesson_Number >= 18:
        buttonlesson18.destroy()
    if Lesson_Number >= 19:
        buttonlesson19.destroy()
    if Lesson_Number >= 20:
        buttonlesson20.destroy()
    if Lesson_Number >= 21:
        buttonlesson21.destroy()
    if Lesson_Number >= 22:
        buttonlesson22.destroy()
    if Lesson_Number >= 23:
        buttonlesson23.destroy()
    if Lesson_Number >= 24:
        buttonlesson24.destroy()




def archive():
    # Description: The archive function displays buttons for each lesson we have access to (we completed earlier)
    # Parameters: None
    # Returns: None

    # Clear Console
    cmd.configure(state = 'normal')
    cmd.delete(1.0,'end')
    cmd.configure(state='disabled')
    # Clear Code field
    txt.delete(1.0,END)
    txt.insert(1.0,"", END)

    # Add to label
    label1.configure(text="")

    # access to global variables
    global button
    global button1
    global button2
    global button3

    global buttonlesson0
    global buttonlesson1
    global buttonlesson2
    global buttonlesson3
    global buttonlesson5
    global buttonlesson6
    global buttonlesson8
    global buttonlesson9
    global buttonlesson10
    global buttonlesson12
    global buttonlesson13
    global buttonlesson14
    global buttonlesson15
    global buttonlesson16
    global buttonlesson17
    global buttonlesson18
    global buttonlesson19
    global buttonlesson20
    global buttonlesson21
    global buttonlesson22
    global buttonlesson23
    global buttonlesson24
    global Lesson0_0_Name
    global Lesson1_0_Name
    global Lesson1_1_Name
    global Lesson1_2_Name
    global Lesson2_0_Name
    global Lesson2_1_Name
    global Lesson3_0_Name
    global Lesson3_1_Name
    global Lesson3_2_Name
    global Lesson4_1_Name
    global Lesson4_2_Name
    global Lesson5_0_Name
    global Lesson5_1_Name
    global Lesson5_2_Name
    global Lesson5_3_Name
    global Lesson5_4_Name
    global Lesson5_5_Name
    global Lesson5_6_Name
    global Lesson6_0_Name
    global Lesson6_1_Name
    global Lesson7_0_Name
    global Lesson7_1_Name

    # Destroy existing buttons (reset code / archive / check Code / continue)
    button.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()

    # Set the lesson buttons if they are available to the player


    if Lesson_Number >= -1:
        buttonlesson0 = Button(root, text='L.0.1 %r' %Lesson0_0_Name, command=lesson0 )
        buttonlesson0.grid(row=0, column = 0)

    if Lesson_Number >= 1:
        buttonlesson1 = Button(root, text='L.1 %r' %Lesson1_0_Name, command=lesson1 )
        buttonlesson1.grid(row=1, column = 0)

    if Lesson_Number >= 2:
        buttonlesson2 = Button(root, text='L.1.1 %r' %Lesson1_1_Name, command=lesson2 )
        buttonlesson2.grid(row=2, column = 0)

    if Lesson_Number >= 3:
        buttonlesson3 = Button(root, text='L.1.2 %r' %Lesson1_2_Name, command=lesson3 )
        buttonlesson3.grid(row=3, column = 0)

    if Lesson_Number >= 5:
        buttonlesson5 = Button(root, text='L.2.0 %r' %Lesson2_0_Name, command=lesson5 )
        buttonlesson5.grid(row=4, column = 0)

    if Lesson_Number >= 6:
        buttonlesson6 = Button(root, text='L.2.1 %r' %Lesson2_1_Name, command=lesson6 )
        buttonlesson6.grid(row=5, column = 0)

    if Lesson_Number >= 8:
        buttonlesson8 = Button(root, text='L.3.0 %r' %Lesson3_0_Name, command=lesson8 )
        buttonlesson8.grid(row=6, column = 0)

    if Lesson_Number >= 9:
        buttonlesson9 = Button(root, text='L.3.1 %r' %Lesson3_1_Name, command=lesson9 )
        buttonlesson9.grid(row=7, column = 0)

    if Lesson_Number >= 10:
        buttonlesson10 = Button(root, text='L.3.2 %r' %Lesson3_2_Name, command=lesson9 )
        buttonlesson10.grid(row=8, column = 0)


    if Lesson_Number >= 12:
        buttonlesson12 = Button(root, text='L.4.1 %r' %Lesson4_1_Name, command=lesson12)
        buttonlesson12.grid(row=9, column = 0)

    if Lesson_Number >= 13:
        buttonlesson13 = Button(root, text='L.4.2 %r' %Lesson4_2_Name, command=lesson13)
        buttonlesson13.grid(row=10, column = 0)

    if Lesson_Number >= 14:
        buttonlesson14 = Button(root, text='L.5.0 %r' %Lesson5_0_Name, command=lesson14)
        buttonlesson14.grid(row=11, column = 0)

    if Lesson_Number >= 15:
        buttonlesson15 = Button(root, text='L.5.1 %r' %Lesson5_1_Name, command=lesson15)
        buttonlesson15.grid(row=12, column = 0)

    if Lesson_Number >= 16:
        buttonlesson16 = Button(root, text='L.5.2 %r' %Lesson5_2_Name, command=lesson16)
        buttonlesson16.grid(row=13, column = 0)

    if Lesson_Number >= 17:
        buttonlesson17 = Button(root, text='L.5.3 %r' %Lesson5_3_Name, command=lesson17 )
        buttonlesson17.grid(row=14, column = 0)

    if Lesson_Number >= 18:
        buttonlesson18 = Button(root, text='L.5.4 %r' %Lesson5_4_Name, command=lesson18 )
        buttonlesson18.grid(row=15, column = 0)

    if Lesson_Number >= 19:
        buttonlesson19 = Button(root, text='L.5.5 %r' %Lesson5_5_Name, command=lesson19 )
        buttonlesson19.grid(row=16, column = 0)

    if Lesson_Number >= 20:
        buttonlesson20 = Button(root, text='L.5.6 %r' %Lesson5_6_Name, command=lesson20 )
        buttonlesson20.grid(row=17, column = 0)


    if Lesson_Number >= 21:
        buttonlesson21 = Button(root, text='L.6.0 %r' %Lesson6_0_Name, command=lesson21 )
        buttonlesson21.grid(row=18, column = 0)


    if Lesson_Number >= 22:
        buttonlesson22 = Button(root, text='L.6.1 %r' %Lesson6_1_Name, command=lesson22 )
        buttonlesson22.grid(row=19, column = 0)


    if Lesson_Number >= 23:
        buttonlesson23 = Button(root, text='L.7.0 %r' %Lesson7_0_Name, command=lesson23 )
        buttonlesson23.grid(row=20, column = 0)


    if Lesson_Number >= 24:
        buttonlesson24 = Button(root, text='L.7.1 %r' %Lesson7_1_Name, command=lesson24 )
        buttonlesson24.grid(row=21, column = 0)


def get_current_and_achieved_Lesson_number():
    # Description:
    # Parameters: None
    # Returns: None
    global current_Lesson
    global Lesson_Number
    global maxLessons
    global Lesson0_0_GivenCode
    global Lesson1_0_GivenCode
    global Lesson1_1_GivenCode
    global Lesson1_2_GivenCode
    global Lesson2_0_GivenCode
    global Lesson2_1_GivenCode
    global Lesson3_0_GivenCode
    global Lesson3_1_GivenCode
    global Lesson3_2_GivenCode
    global Lesson4_1_GivenCode
    global Lesson4_2_GivenCode
    global Lesson5_0_GivenCode
    global Lesson5_1_GivenCode
    global Lesson5_2_GivenCode
    global Lesson5_3_GivenCode
    global Lesson5_4_GivenCode
    global Lesson5_5_GivenCode
    global Lesson5_6_GivenCode
    global Lesson6_0_GivenCode
    global Lesson6_1_GivenCode
    global Lesson7_0_GivenCode
    global Lesson7_1_GivenCode
    global Lesson0_0_Text
    global Lesson0_1_Text
    global Lesson1_0_Text
    global Lesson1_1_Text
    global Lesson1_2_Text
    global Lesson2_0_Text
    global Lesson2_1_Text
    global Lesson3_0_Text
    global Lesson3_1_Text
    global Lesson3_2_Text
    global Lesson4_1_Text
    global Lesson4_2_Text
    global Lesson5_0_Text
    global Lesson5_1_Text
    global Lesson5_2_Text
    global Lesson5_3_Text
    global Lesson5_4_Text
    global Lesson5_5_Text
    global Lesson5_6_Text
    global Lesson6_0_Text
    global Lesson6_1_Text
    global Lesson7_0_Text
    global Lesson7_1_Text
    global txt
    global label1


    # Access the communication file (read only) to get the lesson which is supposed to be loaded
    comm_file = open("communication_file.txt","r")
    communication = [x.strip('\n') for x in comm_file.readlines()]
    comm_file.close()

    # if the file is empty we just load lesson zero
    if communication != []:
        current_Lesson = int(communication[0])
        Lesson_Number = current_Lesson
    print current_Lesson



    # if the file has a number which is higher than the available lessons we set it to the maxLesson
    if current_Lesson > maxLessons:
        current_Lesson = maxLessons
    if Lesson_Number > maxLessons:
        Lesson_Number = maxLessons


    # Insert given Code specific to lesson
    txt.delete(1.0,'end') # empty the text


    if current_Lesson == (-1):
        txt.insert(1.0,Lesson0_0_GivenCode, END)
    if current_Lesson == (0):
        txt.insert(1.0,Lesson0_1_GivenCode, END)
    if current_Lesson == 1:
        txt.insert(1.0,Lesson1_0_GivenCode, END)
    if current_Lesson == 2:
        txt.insert(1.0,Lesson1_1_GivenCode, END)
    if current_Lesson == 3:
        txt.insert(1.0,Lesson1_2_GivenCode, END)
    if current_Lesson == 5:
        txt.insert(1.0,Lesson2_0_GivenCode, END)
    if current_Lesson == 6:
        txt.insert(1.0,Lesson2_1_GivenCode, END)
    if current_Lesson == 8:
        txt.insert(1.0,Lesson3_0_GivenCode, END)
    if current_Lesson == 9:
        txt.insert(1.0,Lesson3_1_GivenCode, END)
    if current_Lesson == 10:
        txt.insert(1.0,Lesson3_2_GivenCode, END)
    if current_Lesson == 12:
        txt.insert(1.0,Lesson4_1_GivenCode, END)
    if current_Lesson == 13:
        txt.insert(1.0,Lesson4_2_GivenCode, END)
    if current_Lesson == 14:
        txt.insert(1.0,Lesson5_0_GivenCode, END)
    if current_Lesson == 15:
        txt.insert(1.0,Lesson5_1_GivenCode, END)
    if current_Lesson == 16:
        txt.insert(1.0,Lesson5_2_GivenCode, END)
    if current_Lesson == 17:
        txt.insert(1.0,Lesson5_3_GivenCode, END)
    if current_Lesson == 18:
        txt.insert(1.0,Lesson5_4_GivenCode, END)
    if current_Lesson == 19:
        txt.insert(1.0,Lesson5_5_GivenCode, END)
    if current_Lesson == 20:
        txt.insert(1.0,Lesson5_6_GivenCode, END)
    if current_Lesson == 21:
        txt.insert(1.0,Lesson6_0_GivenCode, END)
    if current_Lesson == 22:
        txt.insert(1.0,Lesson6_1_GivenCode, END)
    if current_Lesson == 23:
        txt.insert(1.0,Lesson7_0_GivenCode, END)
    if current_Lesson == 24:
        txt.insert(1.0,Lesson7_1_GivenCode, END)


    # Insert Text specific to lesson
    if current_Lesson == (-1):
        label1.config(text=Lesson0_0_Text)
    if current_Lesson == 0:
        label1.config(text=Lesson0_1_Text)
    if current_Lesson == 1:
        label1.config(text= Lesson1_0_Text)
    if current_Lesson == 2:
        label1.config(text= Lesson1_1_Text)
    if current_Lesson == 3:
        label1.config(text= Lesson1_2_Text)
    if current_Lesson == 5:
        label1.config(text= Lesson2_0_Text)
    if current_Lesson == 6:
        label1.config(text= Lesson2_1_Text)
    if current_Lesson == 8:
        label1.config(text= Lesson3_0_Text)
    if current_Lesson == 9:
        label1.config(text= Lesson3_1_Text)
    if current_Lesson == 10:
        label1.config(text= Lesson3_2_Text)
    if current_Lesson == 12:
        label1.config(text= Lesson4_1_Text)
    if current_Lesson == 13:
        label1.config(text= Lesson4_2_Text)
    if current_Lesson == 14:
        label1.config(text= Lesson5_0_Text)
    if current_Lesson == 15:
        label1.config(text= Lesson5_1_Text)
    if current_Lesson == 16:
        label1.config(text= Lesson5_2_Text)
    if current_Lesson == 17:
        label1.config(text= Lesson5_3_Text)
    if current_Lesson == 18:
        label1.config(text= Lesson5_4_Text)
    if current_Lesson == 19:
        label1.config(text= Lesson5_5_Text)
    if current_Lesson == 20:
        label1.config(text= Lesson5_6_Text)
    if current_Lesson == 21:
        label1.config(text= Lesson6_0_Text)
    if current_Lesson == 22:
        label1.config(text= Lesson6_1_Text)
    if current_Lesson == 23:
        label1.config(text= Lesson7_0_Text)
    if current_Lesson == 24:
        label1.config(text = Lesson7_1_Text)



########### GUI & INITIALIZING ###########
# The following parts set the User Interface for the first time
# and loads variables for initialization purposes.

texter = ""

#__________ Background of instruction text __________#
w = Canvas(root, width=300, height=650)
w.grid(row=0, column =0, columnspan = 4, rowspan=30)
w.create_rectangle(0, 0, 305, 655, fill="white")

#__________instruction text __________#
label1 = Label(root, text=texter ,  justify=LEFT, wraplength= 250, bg ="white")
label1.grid(row=0, column =0, columnspan = 4, rowspan = 30) # 0-29

#__________Grey line between text and coding area __________#
c = Canvas(root, width=5, height=650)
c.grid(row=0, column =5, rowspan = 30) # 0-29
c.create_rectangle(0, 0, 200, 655, fill="grey")

#__________ Coding window __________#
txt_frm = Frame(root,width=100, height=100).grid(row=0, column=6)
txt = Text(txt_frm,height = 27, width = 80,  bg="black", fg="green")
txt.config(font=("Courier", 10), undo=True, wrap='word')
txt.grid(row=0, column=6, columnspan=1, rowspan = 29 ,sticky="n") # 0-28
txt.config(insertbackground="white")
txt.config(tabs = ('0.25i', '0.5i', '0.75i'))
txt.pack_propagate()

#__________ Command line __________#
cmd_frm = Frame(root).grid(row=29,column=6,sticky="nsew")
cmd = Text(cmd_frm, height = 13, width = 80, bg="white", fg="black")
cmd.config(font=("Courier", 10), undo=True, wrap='word')
cmd.grid(row = 29, column = 6, sticky="nw")
cmd.configure(state='disabled')
cmd.pack_propagate()

#__________ Buttons __________#
button = Button(root, text='Check Code', command=checkRunCode)
button.grid(row=30, column = 1)
button1 = Button(root, text='Weiter', command = nextLesson)
button1.grid(row=30, column=3)
button2 = Button(root, text ='Archiv', command = archive)
button2.grid(row=30, column = 2)
button3 = Button (root, text='Reset Code', command=reset)
button3.grid(row =30, column = 6)


######## Initialize via functions ##############
# The following functions set up the lessons
# depending on the lessons and levels completed so far.

#__________ Initialize the functionality  & beginning of the game __________#
get_current_and_achieved_Lesson_number() # Get lesson number from the comm-file
reset() # Set coding area
set_cmd() # Set command line
button1.destroy() # No "Weiter" / continue button in the first lesson - press "Check Code" first

####### Main Loop #########
mainloop()









