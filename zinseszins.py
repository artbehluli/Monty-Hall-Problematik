""" Autor: Art Behluli  Datum: 12.11.2025   Funktion: Zinseszinsrechner """

kontostand = int(input('Bitte gebe deinen Kontostand an: \n'))
zinssatz = float(input('Bitte gebe den Zinssatz an: \n'))
jahr = int(input('Bitte gebe an, bis zu welchem Jahr gerrechnet werden soll: \n'))

def calc(jahr, kontostand):
    kontostand = kontostand + kontostand * zinssatz
    print(f'Dein Kontostand liegt bei {kontostand} CHF')
    
    if jahr > 0:
        jahr -= 1
        calc(jahr, kontostand)

    else:
        print(f'Dein Kontostand liegt bei {kontostand} CHF')


calc(jahr, kontostand)