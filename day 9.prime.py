>>> n = int(input('Enter a number: '))
... if n <= 1:
...     print('Not Prime')
... else:
...     for i in range(2,n):
...         if n % i == 0:
...             print('Not Prime')
...             break
...     else:
...         print('Prime')
...
Enter a number: 7
Prime
>>> 10
>>> start = int(input('Enter the number :'))
... end =int(input('Enter the number :'))
... for num in range(start,end+1):
...     if num > 1:
...        for i in range(2,num):
...           if num % i == 0:
...             break
...        else:
...            print(num)
...
Enter the number :10
Enter the number :20
11
13
17
19
>>> a=int(input('Enter the number a : '))
... b=int(input('Enter the number b : '))
... a,b=b,a
... print('a : ',a)
... print('b : ',b)
...
Enter the number a : 5
Enter the number b : 8
a :  8
b :  5
