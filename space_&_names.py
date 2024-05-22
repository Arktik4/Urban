
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

# inner_function()
# Traceback (most recent call last):
#  File "C:\Users\фвьшт\Desktop\projects_for_urban\homeworks\modul_4\space_&_names.py", line 8, in <module>
#    inner_function()
#    ^^^^^^^^^^^^^^
#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

test_function()