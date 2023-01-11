#open(filename,mode)

#what is a handle? wrapper
fhand = open('mbox.txt')
print(fhand) #prints the file details from handle

#for cheese in fhand: #prints every line
    #print(cheese)

cound = 0
for line in fhand:
    cound = cound +1
print('Line Count: ', cound)

fhand = open('mbox.txt') #not sure why it needs to open handle again
inp = fhand.read()
print('Length: ', len(inp))


fhand = open('mbox.txt')
for search in fhand:
    search = search.rstrip()
    if search.startswith('From: '):
        continue
        #print(search)

fhand = open('mbox.txt')
for search in fhand:
    search = search.rstrip()
    if not '@uct.ac.za' in search:
        continue
    print(search)

fname = input('Filename: ')
try:
    fhand = open(fname)
except:
    print('Filename error: ',fname)
    quit()

cound = 0
for lx in fhand:
    ly = lx.rstrip()
    lz = ly.upper()
    if not 'FROM: ' in lz: #string needs to be upper since im dumb
        continue
    cound = cound +1
    print(lz)
print('Line Count: ', cound)
