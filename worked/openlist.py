
#file wrapper

hand = open('mbox.txt')

for line in hand:
    line = line.rstrip()

#guardian checks
#    if line == '':#skips blank lines
#        print("Skip Blank")
#        continue

    wds = line.split()
    print('Words:',wds)

#guardian checks
    if len(wds)<3 or wds[0]!='From':#checks if line has words
        print("Skipped")
        continue

    print(wds[2])#the day
