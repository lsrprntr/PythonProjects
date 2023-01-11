def thing() : #store phase in a recall folder
    print('Does thing')
    print('doing things')

def greet(lang):
    if lang == 'eng':
        print('Hello')
    elif lang == 'es':
        print('Hola!')
    else:
        print('aliens')
    return "done" #the residual value left after def

thing() #calls what you set

print(greet('eng'))
greet('es')
greet('fr')
greet('asdf')
