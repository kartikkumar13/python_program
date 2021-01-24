# scorelist=[]
# score = []

# for i in range (int(input())):
#     x = input()
#     y = float(input())
#     scorelist.append([x, y])
#     score.append(y)
 
# sorted_score = sorted(set(score))
# output = sorted_score[1]

# result= []
# for i in scorelist:
#     if output == i[1]:
#         result.append(i[0])

#  result.sort()

# for nm in name:
#     print(nm)


marksheet = [[input(), float(input())] for _ in range(int(input()))]
sec_highest = sorted(list(set(marks for name, marks in marksheet)))[1]

print('\n'.join([a for a,b in sorted(marksheet) if b == sec_highest]))