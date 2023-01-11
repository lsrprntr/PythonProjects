
#tuples cannot be altered
#tuples are a list ()
#more efficient though
#tuples can be in a list
#dictionaries can have tuples too
d = {'a':10,'c':1,'b':22}
t = sorted(d.items())
print(t)

tmp = list()
for k, v in d.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp)
print(tmp)
tmp = sorted(tmp,reverse=True)
print(tmp)


filehandler = open('mbox.txt')#open file
dictionary = dict()#making a dictionary list is a tuple

for line in filehandler:
    words = line.split() #reads and splits the lines
    for word in words:
        dictionary[word] = dictionary.get(word,0)+1 #reads the words in the line above and gives it a key

alt=sorted([(k,v) for v,k in dictionary.items()])
print(alt[:10])

list = list()
for k, v in dictionary.items():
    newtup = (v,k)
    list.append(newtup)

list = sorted(list, reverse=True)

for k,v in list[:10]:
    print(v,k)
