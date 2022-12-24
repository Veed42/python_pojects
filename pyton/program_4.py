# import sys
# x=int(1)
# min=int(input("Введите целое число от 0 до 10: "))
# if min>10 or min<0:
#     print("Неверное число!!! Выход их программы!!!")
#     sys.exit(0)
# else:
#     while x<10:
#         y=int(input("Введите целое число от 0 до 10: "))
#         if y>10 or y<0:
#             print("Неверное число!!! Выход их программы!!!")
#             sys.exit(0)
#         if y%2==0 and y%3!=0: 
#             if y<min: 
#                 min=y 
#         x=x+1 
# print("Минимум равен:",min)

numbers = [int(input("Enter numb: 10")) for _ in range(10)]
valid_numbers = [n for n in numbers if not n % 2 and n % 3]

if valid_numbers:
    print(f"Ответ: {min(valid_numbers)}")
else:
    print('Нет чисел, которые соответствуют условию')