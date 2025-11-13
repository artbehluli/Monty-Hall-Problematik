# author:   Art Behluli
# date:     13.11.2025
# function: Monty-Hall-problem

import random

# variables
a = 'Tür 1'
b = 'Tür 2'
c = 'Tür 3'

count = 1000
counter = 0
for _ in range(count):

    g = random.choice(["a", "b", "c"])
    j = "ja"
    n = "nein"

    ausgewaehltetuer = "a"

    # outcome if door a is selected
    if "a" == ausgewaehltetuer:
        if "a" == g:
            print("Tür", random.choice(["b", "c"]))
        if "b" == g:
            print("Tür c wird geöffnet.")
        if "c" == g:
            print("Tür b wird geöffent.")

    # outcome if door b is selected
    if "b" == ausgewaehltetuer:
        if "a" == g:
            print("Tür c wird geöffent.")
        if "b" == g:
            print("Tür", random.choice(["b", "c"]))
        if "c" == g:
            print("Tür a wird geöffnet.")

    # outcome if door c is selected
    if "c" == ausgewaehltetuer:
        if "a" == g:
            print("Tür b wird geöffnet.")
        if "b" == g:
            print("Tür a wird geöffnet.")
        if "c" == g:
            print("Tür", random.choice(["a", "c"]))

    # second input
    print('Ihre Tür ist:', ausgewaehltetuer)
    zweitetuer = "j"

    # outcome if 
    if "a" == ausgewaehltetuer:
        if "j" == zweitetuer:
            if "b" == g:
                print('Gewonnen!')
                counter += 1
            elif "c" == g:
                print('Gewonnen!')
                counter += 1
            else:
                print('Verloren!')
        elif "n" == zweitetuer:
            if "a" == g:
                print('Gewonnen!')
                counter += 1
            else:
                print('Verloren!')

    if "b" == ausgewaehltetuer:
        if "j" == zweitetuer:
            if "a" == g:
                print('Gewonnen!')
                counter += 1
            elif "c" == g:
                print('Gewonnen!')
                counter += 1
            else:
                print('Verloren!')
        elif "n" == zweitetuer:
            if "b" == g:
                print('Gewonnen!')
                counter += 1
            else:
                print('Verloren!')

    if "c" == ausgewaehltetuer:
        if "j" == zweitetuer:
            if "a" == g:
                print('Gewonnen!')
                counter += 1
            elif "b" == g:
                print('Gewonnen!')
                counter += 1
            else:
                print('Verloren!')
        elif "n" == zweitetuer:
            if "c" == g:
                print('Gewonnen!')
                counter += 1
            else:
                print('Verloren!')

# probability of winning in %
counter = counter / 1000 * 100
print(counter, "%")