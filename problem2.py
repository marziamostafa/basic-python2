""" 
2. Write a program to print the following number pattern using a loop.
Input : 5
Output : 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

 """

n=6

number=1
while number<n:
    for i in range(1,number+1):
         print(i,end=' ')
    print('\n')
    number+=1