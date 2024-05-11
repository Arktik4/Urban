immutable_var = (1, 'Один', 0.1, True)
print('Immutable tuple: ', immutable_var)

# immutable_var[1] = 2
# если элемент кортежа не является изменяемым типом данных (список),
# то внести изменения в состав кортежа невозможно

mutable_var = (1, 'Один', [0.1, 0.1], True)
mutable_var[2][1] = 0.2
print('Mutable_var: ', mutable_var)
