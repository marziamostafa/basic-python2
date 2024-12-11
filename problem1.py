""" 
1. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.(don’t use any python built in function)
Example :  pHitrOn.iO presents "Python COuRSe".
Ans : PhITRoN.Io PRENSENTS “pYTHON coUrsE”
 """

word='pHitrOn.iO presents "Python COuRSe"'


for c in word:
  lower=c.lower()
  upper=c.upper()
  if c==lower:
    print(upper,end="")
  else:
    print(lower,end='')


# also possible with built-in function
# new_word=word.swapcase()
# print(new_word)