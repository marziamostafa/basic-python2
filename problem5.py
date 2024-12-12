""" 
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"

Output : AzbycX

 """
s1="Abc"
s2="Xyz"
s3=""
new_s2=""

for k in range(len(s2)-1,-1,-1):
    new_s2=new_s2+s2[k]
count=0

for i in range(len(s1)):
    s3=s3+s1[i]
    for j in range(len(new_s2)):
        if i==j:
            s3=s3+new_s2[j]
            count+=1
            continue
        elif (len(new_s2)<len(s3)) and (len(s1)<len(s2)):
            s3=s3+new_s2[j]
print(s3)   