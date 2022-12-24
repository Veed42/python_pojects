# print("This program 'is' designed to find the average of n numbers you input\n")

# first_question = 'Would you like to enter a number? (type "yes" if you do)\n\n'
# second_question = 'Would you like to enter another number after this? (type "yes" if you do)\n'

# sum_of_numbers = 0
# counter = 0
# if input(first_question) == "yes" :
#     sum_of_numbers += int(input("Enter your number here:"))
#     counter += 1
#     while input(second_question) == "yes" :
#         sum_of_numbers += int(input("Enter your next number here: "))
#         counter += 1
#     print("Your average is " + str(sum_of_numbers/counter))
n = int(input("Введите количество элементов списка: "))
a = []
for i in range(0, n):
    elem = int(input("Введите элемент списка: "))
    a.append(elem)
avg = sum(a) / n
print("Среднее значение элементов списка",round(avg, 2))