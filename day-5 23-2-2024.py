#odd string + even string
'''
s=input()
print(s[1::2]+s[::2])''' 

#Occurance of a character-for loop
'''
s=input()
s=s.lower()
ch=input()
c=0
for i in s:
    if(i==ch):
        c+=1
print(c)'''

#Occurance of a character-methods
'''
s=input()
s=s.lower()
ch=input()
print(s.count(ch))'''

#occurance of a letter in even index-loop
'''
s=input()
s=s.lower()
ch=input()
c=0
for i in range(len(s)):
    if(s[i]==ch and i%2==0):
        c+=1
print(c)'''

#occurance of a letter in even index-slicing
'''
s=input()
ch=input()
r=s[::2]
print(r.count(ch))'''

#vowels in a string-with vowels count
'''
s=input()
v="aeiouAEIOU"
c=0
for i in s:
    if i in v:
        c+=1
print("Yes" if(c==len(s)) else "No")'''

#vowels in a string-with consonants count
'''
s=input()
v="aeiouAEIOU"
c=0
for i in s:
    if i not in v:
        c+=1
print("Yes" if(c==0) else "No")'''

#vowels in a string-with out count
'''
s=input()
v="aeiouAEIOU"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")'''

#digits in a string-with out count
'''
s=input()
d="0123456789"
for i in s:
    if i not in d:
        print("No")
        break
else:
    print("Yes")'''

#digits in a string-with count
'''
s=input()
d="0123456789"
c=0
for i in s:
    if i in d:
        c+=1
print("Yes" if(c==len(s)) else "No")'''

#digits in a string-with alphabet count
'''
s=input()
d="0123456789"
c=0
for i in s:
    if i not in d:
        c+=1
print("Yes" if(c==0) else "No")'''

#digits in a string-with method
'''
s=input()
print("Yes" if(s.isdigit()) else "No")'''

#count of vowels and consonants 
'''
s=input()
s=s.lower()
v="aeiou"
c="qwrtypsdfghjklmnbvcxz"
o_c=0
c_c=0
for i in s:
    if i in v:
        o_c+=1
    elif i in c:
        c_c+=1
print(o_c,c_c)'''

#count of vowels and consonants -method
'''
s=input()
s=s.lower()
v="aeiou"
o_c=0
c_c=0
for i in s:
    if i in v:
        o_c+=1
    elif(i.isalpha()):
        c_c+=1
print(o_c,c_c)'''

#compress a string
'''
s=input()
r=""
c=0
for i in range(len(s)-1): #no need to check last element
    if s[i]==s[i+1]:
        c+=1
    else:
        r=r+s[i]+str(c+1)
        c=0
print(r)'''

#words,vowels and consonants-double for loop
'''
for i in range(int(input())):
    s=list(input().split())
    v="aeiouAEIOU"
    vc=0
    cc=0
    for i in s:
        for j in i:
            if j in v:
                vc+=1
            elif(j.isalpha()):
                cc+=1
    print(len(s),vc,cc)'''

#words,vowels and consonants-single for loop
'''
for i in range(int(input())):
    s=input()
    v="aeiouAEIOU"
    vc=0
    cc=0
    for i in s:
        if i in v:
            vc+=1
        elif(i.isalpha()):
            cc+=1
    print(len(s.split()),vc,cc)''' 

#Guess the problem-1
'''
for i in range(int(input())):
    a,b=input().split()
    r=""
    for i in b:
        if(i not in a):
            r=r+i
    print(r)
'''

#guess the problem-2

for i in range(int(input())):
    a,b=input().split()
    b=int(b)
    r=""
    for i in a:
        k = ord(i)+b
        if k > 122:
            k = 96 + (k-122)
            r = r + chr(k)
        else:
            r = r + chr(k)
    print(r)

#oops
'''
class classa:
    def factorial(self,n):
        r=1
        for i in range(1,n+1):
            r=r*i
        print(r)
ob=classa()
ob.factorial(5)'''

#opps -2
'''
class classa:
    def __init__(self,n):
        self.n=n
        print(n) #no need to use self
    def factorial(self):
        r=1
        for i in range(1,self.n+1): # we have to use self as __init__ is private
            r=r*i
        print(r)
ob=classa(5)
ob.factorial()'''

#recursive in classes
'''
class classa:
    def __init__(self,n):
        self.n=n 
    def factorial(self):
        print(self.fact(self.n))
    def fact(self,n):
        if n==1 or n==0:
            return 1
        else:
            return (n*self.fact(n-1))
ob=classa(5)
ob.factorial()'''
