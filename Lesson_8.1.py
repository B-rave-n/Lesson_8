def add_one(some_list):
    number = 0
    nulls = (len(some_list) - 1)
    ten = 10 ** nulls
    for i in some_list:
        number += i * ten
        nulls -= 1
        ten = 10 ** nulls
    number += 1
    return [int(i) for i in str(number)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
# Додаткова перевірка, яка показує роботу і незалежність від розміру числа
assert add_one([4534999]) == [4, 5, 3, 5, 0, 0, 0], 'Test5'
assert add_one([45349999999999999]) == [4, 5, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Test5'
print("ОК")