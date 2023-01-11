def abbrev_name(name):
    w=name.split()
    fletter = w[0]
    lletter = w[1]
    result = fletter[0]+"."+lletter[0]
    return print(result)

abbrev_name("Sam David")

def abbrev_namee(name):
    w=(name.upper()).split()
    fletter,lletter = w[0],w[1]
    return fletter[0]+"."+lletter[0]

abbrev_namee("Sam David")
