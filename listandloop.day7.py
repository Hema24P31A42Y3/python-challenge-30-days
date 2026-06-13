                         
>>> for i in range(1,len(arr)):
...     if arr[i] > arr[max_index]:
...         max_index = i
... print("index num:",max_index)
...
index num: 7
>>> largest = max(arr)
>>> count = arr.count(largest)
>>> print(count)
1
>>>
>>> n = len(arr)
>>> for i in range(n):
...     for j in range(0,n-i-1):
...         if arr[j]>arr[j+1]:
...             arr[j],arr[j+1]=arr[j+1],arr[j]
... print(arr)
...
[1, 2, 3, 4, 5, 6, 9, 11, 12, 15]
>>> k=9
>>> key = 9
>>> if key in arr:
...     print("key exit")
... else:
...     print("key does not exit")
...
key exit
>>> even_sum = 0
... odd_sum = 0
...
... for i in arr:
...     if i % 2 == 0:
...         even_sum += i
...     else:
...         odd_sum += i
... difference = even_sum - odd_sum
... print("Even Sum:", even_sum)
... print("Odd Sum:", odd_sum)
... print("Difference:",difference)
...
Even Sum: 24
Odd Sum: 44
Difference: -20
>>> while 2 in arr:
...     arr.remove(2)
... print(arr)
...
[1, 3, 4, 5, 6, 9, 11, 12, 15]

