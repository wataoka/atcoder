x = int(input())

for a in range(-122, 122):
    for b in range(-122, 122):
        if a**5 - b**5 == x:
            print(a, b)
            exit(0)