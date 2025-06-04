names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
x = names.pop()
while x != 'Валера':
    print(x)
    x = names.pop()
print(f'Привет Валера!')