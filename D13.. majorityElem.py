nums = list(map(int, input().split()))

count = {}

for i in nums:
    count[i] = count.get(i, 0) + 1

print(max(count, key=count.get))
