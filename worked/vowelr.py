def shortcut( s ):
    import re
    list_of_char = ['a', 'e', 'i','o','u']
    #pattern = '[' + ''.join(list_of_char) + ']'
    pattern = '[aeiou]'
    print(pattern)
    what=type(pattern)
    print(what)
    s = re.sub(pattern, "", s)
    print(s)
shortcut('how are you today')
