import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "()"



temp = ""

upper = input("Do you want to use upper case letters in the password? : ")
lower = input("Do you want to use lower case letters in the password? : ")
nums = input("Do you want to use digits in the password? : ")
syms = input("Do you want to use symbols in the password? : ")

if upper.lower() != 'no':
    temp += uppercase_letters 
if lower.lower() != 'no':
    temp += lowercase_letters
if nums.lower() != 'no':
    temp += numbers
if syms.lower() != 'no':
    temp += symbols

length = input("what should be the length of the password? :  ")
value = int(length)


password = "".join(random.sample(temp, value))

print(password)
