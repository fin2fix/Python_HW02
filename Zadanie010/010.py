# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2


from random import randint
numberOfCoins = int(input("Введите количество монет на столе  "))
coins = []
firstSide = 0

for i in range(numberOfCoins):
    tempNumber = randint(0, 1)
    coins.append(tempNumber)
    if tempNumber == 0:
        firstSide += 1

print()
print(* coins)
print()
secondSide = len(coins) - firstSide
if firstSide > secondSide:
    print(f"Нужно перевернуть {secondSide} монет(-ы)")
else:
    print(f"Нужно перевернуть {firstSide} монет(-ы)")
