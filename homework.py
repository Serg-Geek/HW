array = "кот дом мяч собака яблоко апельсин".split()

# Формируем новый массив из строк, длина которых меньше или равна 3
new_array = [word for word in array if len(word) <= 3]