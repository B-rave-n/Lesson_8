def find_unique_value(some_list):
   for i in list(set(some_list)):
      if some_list.count(i) == 1:
         return i


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

# Повертає найменше унікальне значення
# Пройде тест:
# assert find_unique_value([5, 5, 1, 5, 2, 2, 6]) == 1, 'Test'
# Але провалить тест:
# assert find_unique_value([5, 5, 1, 5, 2, 2, 6]) == 6, 'Test'
# Але в ДЗ сказано, що не потрібно розглядати випадки, коли в списку декілька унікальних значень