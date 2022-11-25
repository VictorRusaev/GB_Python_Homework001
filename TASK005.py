# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.

print('Введите координату x точки А')
xA = int(input())
print('Введите координату y точки А')
yA = int(input())

print('Введите координату x точки B')
xB = int(input())
print('Введите координату y точки B')
yB = int(input())

print()
print ('A (' ,xA, ';' ,yA, ')')
print ('B (', xB, ';' ,yB, ')')
print()

x = float((xA - xB)**2)
y = float((yA - yB)**2)
d = round(float((x + y)**0.5), 3)
print(d)