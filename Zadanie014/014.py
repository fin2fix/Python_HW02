# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k ), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите любое положительное число  "))
count = 0
while 2**count < number:
    print(2 ** count, end=" ")
    count += 1
