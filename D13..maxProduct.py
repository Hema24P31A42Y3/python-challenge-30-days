nums = list(map(int, input().split()))

nums.sort()
print((nums[-1]-1) * (nums[-2]-1))
