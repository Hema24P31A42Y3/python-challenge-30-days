n = int(input())
m = int(input())

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

key = int(input())

for i in range(n):
    for j in range(m):
        if arr[i][j] == key:
            print(i, j)
