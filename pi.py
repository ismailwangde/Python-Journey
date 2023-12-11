import random
pi=0.0
i=0
for i in range(10000):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        pi=pi + 1
    i=i+1
print((pi*4/i))