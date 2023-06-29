def romtonum(roman):
    numeraldict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    last=0
    current=0
    total=[0]
    for letter in roman:
        current=numeraldict.get(letter)
        if last >= current:
            total.append(current)
        else:
            total.pop()
            total.append(current-last)
        last = numeraldict.get(letter)
    return total


romtonum("III")
romtonum("IIII")
romtonum("IV")
romtonum("IX")
romtonum("XIV")
romtonum("IL")
romtonum("XII")
romtonum("VII")
romtonum("MCMXCIV")
