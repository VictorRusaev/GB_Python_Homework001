# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input('Введите X: ')
y = input('Введите Y: ')
z = input('Введите Z: ')

a = not(x or y or z)
b = not x and not y and not z

print(a == b)