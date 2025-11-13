nummer = [1, 2, 3, 4, 5, 6]

try:
    sumnum = sum(nummer)
    print('Die Zahlen sind:\n ', sumnum)

except:
    print('Die Zahlen können nicht ausgegeben werden.')

finally:
    print('Viel Spass!')