# author:   Art Behluli
# date:     14.11.2025
# function: general knowledge quiz

import tkinter as tk
import tkinter.font as tkfont

punkte = 0

def erstesquiz():
    global punkte
    usereingabe = eingabe.get().lower()
    if usereingabe == "bern":
        punkte += 1
    else:
        punkte += 0
    quiz1.pack(fill="both", expand=True)

def zweitefrage():
    global punkte
    usereingabe = eingabe1.get().lower()
    if usereingabe == "paris":
        punkte += 1
    else:
        punkte += 0
    fragezwei.pack(fill="both", expand=True)

def drittefrage():
    global punkte
    usereingabe = eingabe2.get().lower()
    if usereingabe == "tirana":
        punkte += 1
    else:
        punkte += 0
    fragedrei.pack(fill="both", expand=True)

def viertefrage():
    global punkte
    usereingabe = eingabe3.get().lower()
    if usereingabe == "moskau":
        punkte += 1
    else:
        punkte += 0
    fragevier.pack(fill="both", expand=True)

def fünftefrage():
    global punkte
    usereingabe = eingabe4.get().lower()
    if usereingabe == "kopenhagen":
        punkte += 1
    else:
        punkte += 0
    fragefünf.pack(fill="both", expand=True)

def sechstefrage():
    global punkte
    usereingabe = eingabe5.get().lower()
    if usereingabe == "sofia":
        punkte += 1
    else:
        punkte += 0
    fragesechs.pack(fill="both", expand=True)

def siebtefrage():
    global punkte
    usereingabe = eingabe6.get().lower()
    if usereingabe == "stockholm":
        punkte += 1
    else:
        punkte += 0
    fragesieben.pack(fill="both", expand=True)

def achtefrage():
    global punkte
    usereingabe = eingabe7.get().lower()
    if usereingabe == "amsterdam":
        punkte += 1
    else:
        punkte += 0
    frageacht.pack(fill="both", expand=True)

def ergebnis_anzeigen():
    ergebnis_label.config(text=f"Du hast {punkte} von 8 Punkten!")
    ergebnis_frame.pack(fill="both", expand=True)

start = tk.Tk()

titel = tk.Label(start, text="Herzlich Willkommen! \n", font=("arial", 50))
untertitel = tk.Label(start, text="Teste dein Allgemeinwissen:", font=("arial", 30))
button1 = tk.Button(start, text="Hauptstädte", command=erstesquiz, width=50, height=10)

titel.place(x=450, y=250)
untertitel.place(x=520, y=330)
button1.place(x=600, y=500)

quiz1 = tk.Frame(start)
frage1 = tk.Label(quiz1, text="Wie heisst die Hauptstadt von der Schweiz: ", font=("Arial", 14))

eingabe = tk.Entry(quiz1)
button3 = tk.Button(quiz1, text="weiter", command=zweitefrage, width=10, height=1)

frage1.place(x=580, y=400)
eingabe.place(x=700, y=450)
button3.place(x=830, y=445)

fragezwei = tk.Frame(quiz1)
frage2 = tk.Label(fragezwei, text="Wie heisst die Hauptstadt von Frankreich: ", font=("Arial", 14))

eingabe1 = tk.Entry(fragezwei)
button4 = tk.Button(fragezwei, text="weiter", command=drittefrage, width=10, height=1)

frage2.place(x=580, y=400)
eingabe1.place(x=700, y=450)
button4.place(x=830, y=445)

fragedrei = tk.Frame(fragezwei)
frage3 = tk.Label(fragedrei, text="Wie heisst die Hauptstadt von Albanien: ", font=("Arial", 14))

eingabe2 = tk.Entry(fragedrei)
button5 = tk.Button(fragedrei, text="weiter", command=viertefrage, width=10, height=1)

frage3.place(x=590, y=400)
eingabe2.place(x=700, y=450)
button5.place(x=830, y=445)

fragevier = tk.Frame(fragedrei)
frage4 = tk.Label(fragevier, text="Wie heisst die Hauptstadt von Russland: ", font=("Arial", 14))

eingabe3 = tk.Entry(fragevier)
button6 = tk.Button(fragevier, text="weiter", command=fünftefrage, width=10, height=1)

frage4.place(x=590, y=400)
eingabe3.place(x=700, y=450)
button6.place(x=830, y=445)

fragefünf = tk.Frame(fragevier)
frage5 = tk.Label(fragefünf, text="Wie heisst die Hauptstadt von Dänemark: ", font=("Arial", 14))

eingabe4 = tk.Entry(fragefünf)
button7 = tk.Button(fragefünf, text="weiter", command=sechstefrage, width=10, height=1)

frage5.place(x=590, y=400)
eingabe4.place(x=700, y=450)
button7.place(x=830, y=445)

fragesechs = tk.Frame(fragefünf)
frage6 = tk.Label(fragesechs, text="Wie heisst die Hauptstadt von Bulgarien: ", font=("Arial", 14))

eingabe5 = tk.Entry(fragesechs)
button8 = tk.Button(fragesechs, text="weiter", command=siebtefrage, width=10, height=1)

frage6.place(x=590, y=400)
eingabe5.place(x=700, y=450)
button8.place(x=830, y=445)

fragesieben = tk.Frame(fragesechs)
frage7 = tk.Label(fragesieben, text="Wie heisst die Hauptstadt von Schweden: ", font=("Arial", 14))

eingabe6 = tk.Entry(fragesieben)
button9 = tk.Button(fragesieben, text="weiter", command=achtefrage, width=10, height=1)

frage7.place(x=590, y=400)
eingabe6.place(x=700, y=450)
button9.place(x=830, y=445)

frageacht = tk.Frame(fragesieben)
frage8 = tk.Label(frageacht, text="Wie heisst die Hauptstadt von den Niederlanden: ", font=("Arial", 14))

eingabe7 = tk.Entry(frageacht)
button10 = tk.Button(frageacht, text="fertig", command=ergebnis_anzeigen, width=10, height=1)

frage8.place(x=590, y=400)
eingabe7.place(x=700, y=450)
button10.place(x=830, y=445)

ergebnis_frame = tk.Frame(frageacht)
ergebnis_label = tk.Label(ergebnis_frame, font=("Arial", 30))
ergebnis_label.place(x=550, y=400)

start.mainloop()