def romtonum(roman):
    numeraldict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    last,current=0,0
    for letter in roman:
        if last < current:
            last = numeraldict.get(letter)
            print(last)
            


    return
romtonum("III")
romtonum("IIII")
romtonum("IV")
romtonum("IX")
romtonum("XIV")
romtonum("L")
romtonum("C")
romtonum("D")
romtonum("ID")
