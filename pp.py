#Program for bot
import random

name=input("Enter your name: ")
print("Your PP size {}".format(name))
size=random.randrange(10)
print("8"+"="*size+"D")
if size<=3 :
    print("Its too small")
elif size>3 and size<=10:
    print("Its good one")
else:
    print("Its damn big")