def last_2_letters(x):
    return x[len(x) - 2] + x[len(x) - 1]


def group_by_rhyme(x):
    y = list()
    for a1 in x:
        z = list()
        z.append(a1)
        for a2 in x:
            if not a1 == a2:
                if last_2_letters(a1) == last_2_letters(a2):
                        z.append(a2)
                        x.remove(a2)
        y.append(z)

    return y


print(group_by_rhyme(['ana', 'eleie','banana', 'carte', 'arme', 'cheie', 'parte']))
