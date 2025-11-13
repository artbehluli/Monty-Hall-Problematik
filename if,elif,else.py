gesuchtezahl = range(50, 101)

eingabe = int(input('Wähle eine Zahl von 1 bis 100, die hälfte der Zahlen sind richtig, der Rest nicht.\n'))


if eingabe > 50:
    print('Du hast die richtige Zahl geraten!\n')

elif eingabe == 6:
    print('Macher!\n')


else:
    print('Du hast die falsche Zahl geraten!\n')


