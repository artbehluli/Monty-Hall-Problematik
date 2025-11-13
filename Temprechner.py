# author: Art Behluli
# date: 13.11.2025
# function: temperature calculator
import re
eingabe = input('Bitte gebe die Temperatur mit der Bezeichnung ein.\n')

# extract all numbers
filter = re.findall(r'-?\d+[.,]?\d*', eingabe)

if not filter:
    print('Sie haben keine güldige Temperatur eingegeben!')
    exit()
zahl = float(filter[0].replace(',', '.'))

# celsius in fahrenheit and/or kelvin
if 'celsius' in eingabe.casefold():
    eingabe2 = input('Bitte wählen sie zum umrechnen zwischen Fahrenheit und Kelvin.\n')
    if 'fahrenheit' in eingabe2.casefold():
        if zahl * 1.8 + 32 > -459.670:
            print(f'{zahl} Grad Celsius in Grad Fahrenheit sind {round(zahl * 1.8 + 32, 2)} °F\n')
        elif zahl * 1.8 + 32 < -459.670:
            print('Deine Eingabe überschreitet den absoluten Nullpunkt!')
            exit()
    elif 'kelvin' in eingabe2.casefold():
        if zahl + 273.15 > 0:
            print(f'{zahl} Grad Celsius in Grad Kelvin sind {round(zahl + 273.15, 2)} K\n')
        elif zahl + 273.15 < 0:
            print('Deine Eingabe überschreitet den absoluten Nullpunkt!')
            exit()

# kelvin in fahrenheit and/or celsius
elif 'kelvin' in eingabe.casefold():
    eingabe3 = input('Bitte wählen sie zum umrechnen zwischen Fahrenheit und Celsius\n')
    if 'fahrenheit' in eingabe3.casefold():
        if (zahl - 273.15) * 1.8 + 32 > -459.670:
            print(f'{zahl} Grad Kelvin in Fahrenheit sind {round((zahl - 273.15) * 1.8 + 32, 2)} °F\n')
        elif (zahl - 273.15) * 1.8 + 32 < -459.670:
            print('Deine Eingabe überschreitet den absoluten Nullpunkt!')
            exit()
    elif 'celsius' in eingabe3.casefold():
        if zahl - 273.15 > -273.15:
            print(f'{zahl} Grad Kelvin in Grad Celsius sind {round(zahl - 273.15, 2)} °C\n')
        elif zahl - 273.15 < -273.15:
            print('Deine Eingabe überschreitet den absoluten Nullpunkt!')
            exit()

# fahrenheit in celsius and/or kelvin
elif 'fahrenheit' in eingabe.casefold():
    eingabe4 = input('Bitte wählen sie zum umrechnen zwischen Celsius und Kelvin\n')
    if 'celsius' in eingabe4.casefold():
        if (zahl - 32) / 1.8 > -273.15:
            print(f'{zahl} Grad Fahrenheit in Grad Celsius sind {round((zahl - 32) / 1.8, 2)} °C\n')
        elif (zahl - 32) / 1.8 < -273.15:
            print('Deine Eingabe überschreitet den absoluten Nullpunkt!')
            exit()
    elif 'kelvin' in eingabe4.casefold():
        if (zahl - 32) / 1.8 + 273.15 > 0:
            print(f'{zahl} Grad Fahrenheit in Grad Kelvin sind {round((zahl - 32) / 1.8 + 273.15, 2)} K\n')
        elif (zahl - 32) / 1.8 + 273.15 < 0:
            print('Deine Eingabe überschreitet den absoluten Nullpunkt!')
            exit()

else:
     print('Sie haben keine güldige Temperatur eingegeben!')
     exit()