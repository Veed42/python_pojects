substring = "Белый" or "белый"
string = input("Введите слово чтобы узнать белый или не белый")
if string.find(substring) != -1:
    print ("Подстрока " + substring + " белый найдена!")
else:
    print ("Подстрока не белый не найдена!")
