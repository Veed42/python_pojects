# print('Решаем уравнение a•x²+b•x+c=0')
# a = input('Введите значение a: ')
# b = input('Введите значение b: ')
# c = input('Введите значение c: ')
# a = float(a)
# b = float(b)
# c = float(c)
# discriminant = b**2 - 4*a*c
# print('Дискриминант = ' + str(discriminant))
# if discriminant < 0:
#     print('Корней нет')
# elif discriminant == 0:
#     x = -b / (2 * a)
#     print('x = ' + str(x))
# else:
#     x1 = (-b + discriminant ** 0.5) / (2 * a)
#     x2 = (-b - discriminant ** 0.5) / (2 * a)
#     print('x₁ = ' + str(x1))
#     print('x₂ = ' + str(x2))
# Python program to find roots of quadratic equation
# Python program to find roots of quadratic equation
print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b**2 - 4 * a * c;
print("Дискриминант D = %.2f" % discr)
if discr > 0:
    import math
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
