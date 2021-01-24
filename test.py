# x = int(input())
# y = int(input())
# z = int(input())
# # n = int(input())cls

# for i in range(x):
#     for j in range(y):
#         for k in range(z):
#             print([i, j, k])

# X = int(input())
# Y = int(input())
# Z = int(input())
# N = int(input())
# lis = [[x, y, z]
#        for x in range(X+1)
#        for y in range(Y+1)
#        for z in range(Z+1)
#        if x + y + z != N
#        ]
# print(lis)


# num = {5, 7, 34, 45, 46, 1}
# # num.remove(max(num))
# print(f'second last number is:  {max(num)}')

# arr = map(int, input().split())
# print(sorted(set(list(arr)))[-2])


# a = (map(int, input().split()))
# print(a)

# score_list = [[input(), float(input())] for _ in range(int(input()))]
# second_highest = sorted(list(set([marks for name, marks in score_list])))[1]
# print('\n'.join([a for a, b in sorted(score_list) if b == second_highest]))

# import argparse
# import sys


# def test(args):
#     if args.x == '1':
#         return "like "
#     if args.y == '2':
#         return "comment "
#     if args.z == '3':
#         return "share "


# parser = argparse.ArgumentParser()
# parser.add_argument('--x', type=str, default='9')

# parser.add_argument('--y', type=str, default='9')

# parser.add_argument('--z', type=str, default='9')

# args = parser.parse_args()

# sys.stdout.write(str(test(args)))

def f(x):
    d = 0
    y = 1
    while y <= x:
        d += 1
        y *= 3
    return (d)


print(f(846))
