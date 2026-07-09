nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

nums1.extend(nums2)
nums1.sort()

print(*nums1)
