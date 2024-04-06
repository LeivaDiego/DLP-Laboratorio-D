def listAlphabet():
    a = list(map(chr, range(97, 123)))
    new = []
    for i in a:
        new.append(i.upper())
    new.reverse()
    return new