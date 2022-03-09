import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,./<>?~'

string = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(string, length))

print("Your new password is:" + password)