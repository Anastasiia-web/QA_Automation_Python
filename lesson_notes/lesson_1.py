my_str = "Hello\nworld!"
print(my_str)

my_str = "Hello world!\b   \\"  # экранирование: вывод 1 слэша через двойной слэш
print(my_str)                   # \b  удаление последнего символа

my_str = "Hello\a world!"
print(my_str)                   # sound \a

my_str = "Hello\t world!"
print(my_str)                   # \t  - табуляция на 4 пробела вправо
