"""

x = 0

while x < 10:
    if x == 3:
        x += 1
        continue

    print(x)
    x = x + 1

print('Acabou!')
y = 0
while y < 5:
    if y == 3:
        y += 1
        break

    print(y)
    y = y + 1

print('Acabou!')
"""

x= 0  #coluna


while x < 10:
    y = 0  # linha

    while y < 5:
      print(f'X vale {x} e Y vale {y}')
      y += 1

    x+=1

print('Acabou!')

