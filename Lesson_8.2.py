def is_palindrome(text):
    lst = [i.lower() for i in text if i.isalpha() or i.isdigit()]
    return lst == lst[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
# Мої перевірки
assert is_palindrome('Я несу гусеня') == True, 'Test5'
assert is_palindrome('113454311') == True, 'Test6'
assert is_palindrome('Кит на морі - романтик.') == True, 'Test7'
assert is_palindrome('А це не паліндром') == False, 'Test4'
print("ОК")