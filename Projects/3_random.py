import random

random_num = random.random()
if random_num < 0.25:
    print("go right")
elif random_num > 0.25 and random_num < 0.5:
    print("try to go left")
elif random_num>0.5 and random_num<0.75:
    print("Try to go top")
else:
    print("try to go bottom")