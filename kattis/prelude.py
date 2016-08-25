import sys

index = 1

for line in sys.stdin:
    words = line.split()
    note = words[0]
    tonality = words[1]
    if len(note) == 1:
        print('Case ' + str(index) + ': UNIQUE')
    else:
        if note[1] == '#':
            note1 = 'b'
            if note[0] == 'G':
                note0 = 'A'
            else:
                note0 = chr(ord(note[0]) + 1)
        else:
            note1 = '#'
            if note[0] == 'A':
                note0 = 'G'
            else:
                note0 = chr(ord(note[0]) - 1)
        print('Case ' + str(index) + ': ' + note0 + note1 + ' ' + tonality)
    index += 1
