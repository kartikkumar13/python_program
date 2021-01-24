numbers = input(">")


def digit_to_word(numbers):
    words = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero"
    }
    output = ""
    for number in numbers:
        output += words.get(number)+" "
    return output


result = digit_to_word(numbers)
print(result)
