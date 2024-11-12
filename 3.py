list = [1, 2, 3, -1, -4, 5, 6]
n = len(list)

przv = 1

for i in range(2, n, 2):
    przv *= list[i]

print(f"Произведение: {przv}")

poloj = []
otric = []

for i in list:
    if i < 0:
        otric.append(i)
    else:
        poloj.append(i)

print(f"*Отсортированный список: {otric + poloj}")