input_string = input("Введите текст: ")

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

output_string = ""

for current_word in words:
    output_string += current_word + " "

output_string = output_string[:-1]

print(f"Начальная строка: {input_string}")
print(f"Конечная строка: {output_string}")