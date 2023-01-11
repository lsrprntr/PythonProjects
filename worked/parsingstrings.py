str = 'X-DSPAM-Confidence: 0.8475'

print(str)
#array starts at 0

ipos = str.find(':')
print(ipos)#18

piece = str[ipos+2:]
print(piece)

value = float(piece)
print(value)
