# author:   Art Behluli
# date:     13.11.2025
# function: Monty-Hall-problem

import random

a = 'Tür 1'
b = 'Tür 2'
c = 'Tür 3'

g = random.choice(["a", "b", "c"])
j = "ja"
n = "nein"

ausgewaehltetuer = input('Wähle eine Tür aus: ')

if "a" == ausgewaehltetuer:
    if "a" == g:
        print("Tür", random.choice(["b", "c"]))
    if "b" == g:
        print("Tür c wird geöffnet.")
    if "c" == g:
        print("Tür b wird geöffent.")

if "b" == ausgewaehltetuer:
    if "a" == g:
        print("Tür c wird geöffent.")
    if "b" == g:
        print("Tür", random.choice(["b", "c"]))
    if "c" == g:
        print("Tür a wird geöffnet.")

if "c" == ausgewaehltetuer:
    if "a" == g:
        print("Tür b wird geöffnet.")
    if "b" == g:
        print("Tür a wird geöffnet.")
    if "c" == g:
        print("Tür", random.choice(["a", "c"]))

print('Ihre Tür ist:', ausgewaehltetuer)
zweitetuer = input('Wächselst du die Tür? j/n: ')

if "a" == ausgewaehltetuer:
    if "j" == zweitetuer:
        if "b" == g:
            print('Gewonnen!')
        elif "c" == g:
            print('Gewonnen!')
        else:
            print('Verloren!')
    elif "n" == zweitetuer:
        if "a" == g:
            print('Gewonnen!')
        else:
            print('Verloren!')

if "b" == ausgewaehltetuer:
    if "j" == zweitetuer:
        if "a" == g:
            print('Gewonnen!')
        elif "c" == g:
            print('Gewonnen!')
        else:
            print('Verloren!')
    elif "n" == zweitetuer:
        if "b" == g:
            print('Gewonnen!')
        else:
            print('Verloren!')

if "c" == ausgewaehltetuer:
    if "j" == zweitetuer:
        if "a" == g:
            print('Gewonnen!')
        elif "b" == g:
            print('Gewonnen!')
        else:
            print('Verloren!')
    elif "n" == zweitetuer:
        if "c" == g:
            print('Gewonnen!')
        else:
            print('Verloren!')