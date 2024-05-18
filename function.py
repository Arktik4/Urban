def print_params(a = 1, b = 'строка', c = True):
        print(a, b, c)

print_params()
print_params(5)
print_params(0, 2)
print_params([3, 5, 7], 'Hi!', False)

print_params(b = 25)
print_params(c = [1,2,3])

print()

alues_list = ('code', 4, True)
values_dict = {'a': False, 'b': 'start', 'c': 0}

print_params(*alues_list)
print_params(**values_dict)

print()

values_list_2 = (69, 'inch')
print_params(*values_list_2)
print_params(*values_list_2, 42)