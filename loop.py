names = ['Beterbiev', 'Lomachenko', 'Kabayel', 'Canelo']
nums = [9, 10, 11, 12, 13, 14, 15]
e = 6

for num in nums:
    print(num + 1)

print('While Loops:\n')

while e <= 2333:
    print(e)
    e = e * 2

#for name in names:
    #if 'k' in name.lower():
        #pass
    #else:
        #print(name)

#for name in names:
    #if 'l' in name.lower():
        #break
    #else:
        #print(name)

for name in names:
    if 'y' in name.lower():
        continue
    else:
        print(name)