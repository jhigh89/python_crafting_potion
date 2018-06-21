#importing random function from python
import random
#default value of health
health = 50

print("You are wounded and find a health potion. You have 50 out of 100 total hp points. Let's see if you can get to a perfect 100!")

potion_health = random.randint(25,50)

health = health + potion_health

print(health)
