fruit = ["apple", "banana", "guava", "graphes", "watermelon", "pineapple"]
# print(fruit[0])
number = [2, 46, 7, 6, 45, 63]
number.append(3)  # add element in last
number.insert(1, 56)  # insert element by giving index and integer


# remove element by giving exact integer that you want to remove
number.remove(46)
number.pop(4)  # remove element by giving its index
number.sort()  # arrange number in accending order
number.reverse()  # arrange number in deccending order


print(number)          # accessing element in list
# print(number[first index:last index :slice/differance])


# tuple
# it is created by {} sign although list is created by [] sign
# it is immutable that means it not changeable
fruit = {"apple", "banana", "guava", "graphes", "watermelon", "pineapple"}
fruit{6} = "barry"
print(fruit)
