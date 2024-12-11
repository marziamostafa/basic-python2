""" 
Display Fibonacci series up to 10 terms

0  1  1  2  3  5  8  13  21  34

 """

n=10
x=0
y=1
print(x,y,end=' ')
for i in range(0,n-2):
    number=x+y
    x=y
    y=number
    print(number,end=' ')
    