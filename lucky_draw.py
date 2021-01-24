import random


def members():
    people_count = int(input("Enter the Number of people:"))
    member = []
    for i in range(people_count):
        output = input(f'Enter the {i+1} number: ')
        member.append(output)
    return member


def lucky_draw(output):
    lucky = random.choice(output)
    return print(f'Congrats :) {lucky} are salected for 1000$, hip hip hureeee!')


output = members()
print(output)
lucky_draw(output)
