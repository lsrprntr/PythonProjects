try:
    hour = input('Enter your hours:')
    rate = input('Enter your rate:')
    hours = float(hour)
    rates = float(rate)
except:
    print('Error: input needs to be numerical')
    quit()
print(hours, rates)
if hours > 40:
    print('Overtime hours: ',hours-40)
    print('Normal hours payout: ',rates*40)
    print('Overtime payout: ',(hours-40)*1.5*rates)
else:
    print('Your payout is: ',hours*rates)
