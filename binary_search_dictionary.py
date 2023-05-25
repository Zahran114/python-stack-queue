def binary_search_dictionary(word, dictionary):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2

        if dictionary[mid][0] == word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < word:
            left = mid + 1
        else:
            right = mid - 1

    return "Definisi tidak ditemukan."

dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

word = "Duck"
definition = binary_search_dictionary(word, dictionary)
print("Definisi dari kata", word, "adalah:", definition)
