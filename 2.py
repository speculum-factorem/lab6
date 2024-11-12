input_string = input("Введите текст: ")
search_word = input("Введите искомое слово: ")

words = []
word = ""

for char in input_string:
    if char != " ":
        word += char
    elif word:
        words.append(word)
        word = ""

#проверка на последнее слово
if word:
    words.append(word)

count = 0

for i in words:
    if i == search_word:
        count += 1

print(f"Количество: {count}")