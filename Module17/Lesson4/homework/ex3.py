#Задача 3. Удаление части

import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = random.randint(0, 9)
b = random.randint(0, 9)

if a > b:
    a, b = b, a

nums[:] = nums[a:b]

print(nums)