def CommonLetter(x):
    counter = 0
    l = ''
    for a in x:
        if not a == ' ':
            a2 = a.upper()
            c = x.count(a)
            c = c + x.count(a2)
            if c > counter:
                counter = c
                l = a

    print("%c is the most common letter, appearing %d times" % (l, counter))


x = "an apple is not a tomatooo"

CommonLetter(x)
