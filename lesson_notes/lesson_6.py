f = lambda: print('Hello')
f()


# Recursion
# В функциональном программировании цикл организован рекурсией.
# Рекурсия используется через оператор-выражение if:  EXAMPLE:   lambda x: x + 2 if x > 0 else x*2
# Для рекурсии нужна ссылка на хранилище для анонимной функции, которая использует эту ссылку в лямбда-функции.

a = lambda x: x + 2 if x > 0 else x*2
print(a(5))    # 7
print(a(-5))   # -10
#___
fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(fact(3))  # 6
print(fact(0))  # 1

#___
full_name = lambda first, last: f'Full name: {first} {last}'
print(full_name('guido', 'van rossum'))

#____
print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))

#____
print(f"###{(lambda s: s[::-1])('dlroW olleH')}###")   #   ###Hello World###

#+++++++++++++++++++++++++++++++
# list comprehensions

# [ <expression> for <element> in <iterable> ]
numbers = [x for x in (1, 2, 3, 4)]
print(numbers)  # [1, 2, 3, 4]
squares = [x * x for x in numbers]
print(squares)  # [1, 4, 9, 16]

# [ <expression> for <element> in <iterable> if <condition> ]
evens = [x * x for x in numbers if 0 == x % 2]
print(evens)  # [4, 16]

#____
import random

l = [v for x in range(10) for v in (lambda size: [random.randint(1, 100) for i in range(size)])(x) if v > 10]
print(l)  # [100, 54, 73, 97, 45, 46, 48, 56, 75, 34, 99, 92, 21, 99, 93, 93, 16, 32, 32, 49, 15, 54, 63, 99, 95, 59, 64, 42, 15, 82, 48, 36, 66, 97, 58, 12, 26, 58, 59, 38, 14]

#++++++
L = [1, 2, 3, 4]
print(list(map(lambda x: x**2, L)))   # [1, 4, 9, 16]

#____
L = [1,3,2,5, 20, 21]   #  фильтруем нечётные
print(list(filter(lambda x: not x%2 ==0, L)))  # [1, 3, 5, 21]

#____
