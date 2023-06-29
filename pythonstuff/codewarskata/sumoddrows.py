def row_sum_odd_numbers(n):
    count = 0
    t=n
    while n >= 1:
        n-=1
        count = count + n
    b = count*2 + 1
    print(oddlist)
    while t != 1:
        b=b+2
        oddlist.append(b)
        print(oddlist)
        t-=1
    return sum(oddlist)



#my dumb ass didnt see the pattern first... its n to the power of 3.


row_sum_odd_numbers(1)
print("\n")
row_sum_odd_numbers(2)
print("\n")
row_sum_odd_numbers(3)
print("\n")
row_sum_odd_numbers(4)
