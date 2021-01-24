
# marksheet ={input : list(map(int, input().split())) for _ in range(int((input())))}
n = int(input())
student_marks = {}
for _ in range(n):
    name , *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores



query_name = input()
x = query_name in student_marks
if x == True:
    for a,b in student_marks.items():
        while query_name == a:
            marks = b
            break
else:
    print("not found")

sum = 0.0
for m in marks:
    sum = sum+m;

item = len(marks)

avg = sum/item
rounded_avg= format(avg,".2f")
print(rounded_avg)

