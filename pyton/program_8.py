import random as rand

rand_num = rand.randrange(1, 100)
guess = int(input("Назовите число от 1 до 100:"))
tries=1
while guess != rand_num:
    if guess > rand_num:
        print("Меньше")
    else:
        print("Больше")
    guess = int(input("Назовите число"))
    tries +=1
print("Вам удалось отгадать число,это в самом деле" ,rand_num)
print("На это вам потребовалось" , tries ,"Попыток") 