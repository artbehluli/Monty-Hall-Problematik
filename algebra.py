zahl1 = input('Wähle eine Zahl aus.\n')
zahl2 = input ('Wähle eine Zahl aus, mit der die erste Zahl multipliziert werden soll.\n')
Produkt = int(zahl1)*int(zahl2)

print(f'{zahl1} multipliziert mit {zahl2} ergibt {Produkt}.\n')

zahl3 = input('Wähle eine Zahl mit Dezimalstellen aus.\n')
zahl4 = input('Wähle eine Zahl mit Dezimalstellen aus, mit der multipliziert werden soll.\n')
zahl5 = input('Wähle eine dritte Zahl mit Dezimalstellen, mit der multipliziert werden soll.\n')
Lösung = float(zahl3)*float(zahl4)*float(zahl5)

print(f'Die Lösung von {zahl3} mal {zahl4} mal {zahl5} ist {Lösung}\n')

x = 10
y = 10

print('Die Variablen x und y addiert ergeben:' , x + y,'aber das Produkt der beiden Variablen ergibt' , (x + y) * 5,'.\n')
print('x = y und x > y ist:' , x == y and x > y)