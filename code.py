import random
letters = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()"

string = letters+capital+numbers+symbols
length = 16
password = "".join(random.sample(string,length))
print("Password Generated : " + password)
