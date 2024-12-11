""" 
Count all uppercase, lowercase, digits, and special symbols from a given
"P@#yn26at^&i5ve"
Total counts of chars, digits, and symbols 

 """

word="P@#yn26at^&i5ve"
lower_chars=0
upper_chars=0
digits=0
symbols=0

for c in word:
     if c.isupper():
          upper_chars+=1
          #print(upper, end=' ')
     elif c.islower():
          lower_chars+=1
     elif c.isdigit():
          digits+=1
     else:
          symbols+=1
          
          

print('Lower Characters: ',lower_chars)
print('Upper Characters: ',upper_chars)
print('Digits: ',digits)
print('Symbols: ',symbols)