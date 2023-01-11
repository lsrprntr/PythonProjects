num = 0
total = 0.0
while True:
    stringinput = input('Enter a number: ')
    if stringinput == 'done':
        break
    try:
        floatinput = float(stringinput)
    except:
        print('Invalid input')
        continue #goes back to the start of the inner loop
    num=num+1
    total=total+floatinput
    print(floatinput)
print(total,num,total/num)
