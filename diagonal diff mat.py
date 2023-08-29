n = int(input().strip())
arr = []
s = 0
s1 = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if (i == j):
            s += arr[i][j]
    for k in range(0, len(arr), -1):
        s1 += arr[i][j]
t = s - s1