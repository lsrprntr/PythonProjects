bag = dict()
bag['money'] = 12
bag['candy'] = 3
bag['keys'] = 75
#dictionaries are like bags with no order just labels
print(bag)

ccc = {} #empty dictionaries
ccc = {'sam':5,'han':0}#make a dictionaries
lister = ['sam','han','bec','dav','sam','sam','han','bec']

for var in lister:
    ccc[var] = ccc.get(var,0)+1
print(ccc)

#Find commonmost word in file

ddd = {}
handle = open('mbox.txt')

for line in handle:
    line=line.rstrip()
    line=line.split()
    for var in line:
        ddd[var]=ddd.get(var,0)+1

#print(ddd.max())

bigcount=None
bigword=None
for word,count in ddd.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)


print(ccc)
stringy = "sadfkljhwfiuhakv"
eee=set(stringy)

test = eee
print(test)
