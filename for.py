cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]

for i in cars:
    print(f'Я езжу на автомабиле марки, {i}')

print()

cars_count = 0
for i in cars:
    cars_count += 10
    print(f'Я езжу на автомабиле марки, {i}')
    print(cars_count)