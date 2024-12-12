""" 
Write a program to check if one string contains another. For example, the result will be True if all the characters in the s1 are present in s2, otherwise False. The character’s position doesn’t matter. Take inputs from the user.

s1 = "Phi"
s2 = "Phitron"

Output : True

 """
s1 = "Phi"
s2 = "Phitron"
count=0

for i in s2:
    for j in s1:
        if i==j:
            count+=1
        else:
            continue
if count==len(s1):
    print(True)
else:
    print(False)