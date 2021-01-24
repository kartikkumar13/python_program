n = int(input("Enter the term for series:"))
t1 = 0
t2 = 1
print(t1, end=",")
print(t2, end=",")
for i in range(n):
    fab = t1+t2
    print(fab, end=",")
    t1 = t2
    t2 = fab
