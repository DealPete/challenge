import sys

note_line = {'G': 0, 'F': 1, 'E': 2, 'D': 3, 'C': 4, 'B': 5, 'A': 6, 'g': 7, 'f': 8, 'e': 9, 'd': 10, 'c': 11, 'b': 12, 'a': 13}

lines = sys.stdin.readlines()
notes = lines[1].split()

staff_length = -1
for note in notes:
    if len(note) == 2:
        staff_length += int(note[1]) + 1
    else:
        staff_length += 2

staff = [['G', ':', ' '] + ([' '] * staff_length)]
staff += [['F', ':', ' '] + (['-'] * staff_length)]
staff += [['E', ':', ' '] + ([' '] * staff_length)]
staff += [['D', ':', ' '] + (['-'] * staff_length)]
staff += [['C', ':', ' '] + ([' '] * staff_length)]
staff += [['B', ':', ' '] + (['-'] * staff_length)]
staff += [['A', ':', ' '] + ([' '] * staff_length)]
staff += [['g', ':', ' '] + (['-'] * staff_length)]
staff += [['f', ':', ' '] + ([' '] * staff_length)]
staff += [['e', ':', ' '] + (['-'] * staff_length)]
staff += [['d', ':', ' '] + ([' '] * staff_length)]
staff += [['c', ':', ' '] + ([' '] * staff_length)]
staff += [['b', ':', ' '] + ([' '] * staff_length)]
staff += [['a', ':', ' '] + (['-'] * staff_length)]

index = 0

for note in notes:
    if len(note) == 2:
        note_length = int(note[1])
    else:
        note_length = 1

    for n in range(0, note_length):
        staff[note_line[note[0]]][index + n + 3] = '*'

    index += note_length + 1

for j in staff:
    print("".join(j))
