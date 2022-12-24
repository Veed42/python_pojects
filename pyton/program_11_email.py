#Python program to extract emails From 
# the String By Regular Expression. 
 
import re 
while True:
    email_address =  input("Введите email")
    addressToVerify = email_address
    match = re.match('[^@]+@[^@]+\.[^@]+', addressToVerify)
    if match == None:
        print('Bad Syntax in ' + addressToVerify)
        continue
    else:
        print("Mail find")
        break
# Printing of List 