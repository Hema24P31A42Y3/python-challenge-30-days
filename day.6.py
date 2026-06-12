arr=[2,12,3,13,4,15,6,7,8,9,10]
>>> print(arr)
[2, 12, 3, 13, 4, 15, 6, 7, 8, 9, 10]
>>> print(max(arr))
15
>>> print(min(arr))
2
>>> print(sum(arr))
89
>>> count=0
>>> for i in arr:
...     if i % 2 == 0:
...         count = count + i
... print(count)
...
42
>>> count=0
>>> for i in arr:
...     if i % 2 == 0:
...         count += 1
... print(count)
...
...
6
>>> for i in arr:
...     if i % 2 != 0:
...         print(i)
...
3
13
15
7
9
>>> for i in arr:
...     if i>10:
...         print(i)
...
12
13
15
>>> print(i*i)
100
>>> for i in arr:
...     print(i*i)
...
4
144
9
169
16
225
36
49
64
81
100
>>> print(arr[::-1])
[10, 9, 8, 7, 6, 15, 4, 13, 3, 12, 2]
>>> print(arr[::-1])
[10, 9, 8, 7, 6, 15, 4, 13, 3, 12, 2]
>>>
>>> sum = 0
>>> for i in arr:
...     sum = sum+i
... avg=sum/len(arr)
... print(avg)
...
8.090909090909092
>>>
