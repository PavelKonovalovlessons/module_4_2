def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


"""inner_function()"""
# Traceback (most recent call last):
#  File "C:\Users\Pavel\ module_4_2\ module_4_2\module_4_2.py", line 7, in <module>
#    inner_function()
#    ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function


test_function() # здесь вывод работает)