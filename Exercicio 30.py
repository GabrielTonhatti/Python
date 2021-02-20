resto = 0
for i in range(1, 51):
    resto = i % 4
    if i % 4 == 0:
        print('PI', end=', ')
    else:
        print(i, end=', ')

