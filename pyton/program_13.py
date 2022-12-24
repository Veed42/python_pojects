# slovo = str(input("Введите слово палиндром: "))
# a = slovo[::-1]
# if slovo == a:
#   print("yes")
# else:
#   print("no")
# Попроще 

string = input('Введите слово: ')
string_reversed = reversed(string)
if "yes" == "".join(set(["yes" if i == j else "no" for i, j in zip(string, string_reversed)])):
    print("yes")
else:
    print("no")