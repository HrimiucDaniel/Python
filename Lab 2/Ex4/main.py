def compose(notes, moves, start):
    move = [notes[start]]
    position = start
    for x in moves:
        position = position + x
        if position < 0:
            position = (len(notes) - 1) + x
        if position > len(notes) - 1:
            position = len(notes) - 2 - x

        move.append(notes[position])
    return move


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
