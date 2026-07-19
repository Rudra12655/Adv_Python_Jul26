def count_characters(text):
    result = {}

    for char in text.lower():
        if char.isalpha():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1

    sorted_result = {}
    for key in sorted(result):
        sorted_result[key] = result[key]

    return sorted_result


text = "Hello World 123!!"
print(count_characters(text))