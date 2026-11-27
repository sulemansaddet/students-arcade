import random

# Each student names their file plugins/github_username.py

AUTHOR = "Suleman Saddet"
APP_NAME = "Magic 8-Ball"



def run():
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    total = num1+num2
    return total
    
print(AUTHOR)
print(APP_NAME)
print(run())

