picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]

for d1 in picture:
    total = ''
    for d2 in d1:
        if d2 == 0:
            total += ' '
        elif d2 == 1:
            total += '#'
    print(total)

print('\n')

i = 0
while i < len(picture):
    j = 0
    final_str = ''
    while j < len(picture[i]):
        final_str += ' ' if picture[i][j] == 0 else '*'
        j += 1
    print(final_str)
    i += 1

