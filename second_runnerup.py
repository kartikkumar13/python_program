
def get_data():
    number = []
    n = int(input('Enter the number term:'))
    for i in range(n):
        output = input(f'Enter the {i+1} number: ')
        number.append(output)
    return number


def second_runnerup(output):
    output.remove(max(output))
    return print(f'The runnerup is: {max(output)}')


output = get_data()
print(output)
second_runnerup(output)
