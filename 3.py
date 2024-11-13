import random

n = int(input("Введите размер списка: "))
lower_bound= -100
upper_bound= 100

random_list = [random.randint(lower_bound, upper_bound) for _ in range(n)]

przv = 1

for i in range(2, n, 2):
    przv *= random_list[i]

print(f"Произведение: {przv}")

poloj = []
otric = []

for i in random_list:
    if i < 0:
        otric.append(i)
    else:
        poloj.append(i)

print(f"*Отсортированный список: {otric + poloj}")