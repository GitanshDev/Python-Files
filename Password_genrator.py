import random
import string

length = int(input("Enter Your Length:- "))

char = string.ascii_letters + string.ascii_uppercase + string.digits + string.punctuation

password = "".join(random.choice(char) for i in range(length))

print("Your Password is:",password)

