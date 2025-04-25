#Задача 1. Анализ цен
import random

original_prices = [random.randint(-20, 20) for _ in range(5)]

new_prices = original_prices[:]

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))