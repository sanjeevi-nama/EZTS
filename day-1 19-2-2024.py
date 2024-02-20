#A-print many hello worlds
'''
i=1000
while(i):
    print("Hello World")
    i=i-1'''

#B-small, large, or equal
'''
a,b=map(int,input().split())
if(a>b):
    print("a > b")
elif(a<b):
    print("a < b")
else:
    print("a == b")'''

#D-Triangle validator
'''
a,b,c=map(int,input().split())
#logic-sum of two sides greater than third side
if a<b+c or b<a+c or c<a+b:
    print("Yes")
else:
    print("No")'''

#equal distribution - APPROACH-1(operator)
'''
n,k=map(int,input().split())
print(k%n)'''

#equal distribution - APPROACH-2 (Brute force method)
'''
n=int(input())
k=int(input())
while(k>=n):
    k=k-n
print(k)'''

#Largest amoung 3 nos
'''a=int(input())
b=int(input())
c=int(input())
if(a>=b and a>=c):
    print(b if(b>c) else c)
elif(b>=a and b>=c):
    print(a if(a>c) else c )
else:
    print(a if(a>b) else b)'''

#second largest amoung 3 nos
'''
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>c and b>a:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)'''

#reversing number
'''n=int(input())
r=0
e=0
if(n<0):
    e=n
    n=-n
while(n!=0):
    k=n%10
    r=10*r+k
    n=n//10
print(-r if(e<0) else r)'''

#fever
'''
for i in range(int(input())):
    t=int(input())
    print("Yes" if t>98 else "No")'''
'''#fever-while
n=int(input())
while(n>0):
    t=int(input())
    if(t>98):
        print("Yes")
    else:
        print("No")'''

#Discount
'''
for i in range(int(input())):
    print(100-int(input()))'''
    
#TV-Discount
'''
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(a-c<b-d):
        print("First")
    elif(a-c>b-d):
        print("Second")
    else:
        print("Any")'''
        
#minimum-packets
'''
for i in range(int(input())):
    n,x=map(int,input().split())
    if(x>=n):
        print(0)
    else:
       r=n-x
       if(r%4==0):
          print(r//4)
       else:
          print(r//4+1)'''

#pizza slice
'''
for i in range(int(input())):
    n,s=map(int,input().split())
    r=n*s
    if(r%4==0):
        print(r//4)
    else:
        print(r//4+1)'''

#pizza-while
'''
for i in range(int(input())):
    n,s=map(int,input().split())
    r=n*s
    p=0
    while(r>=4):
            r=r-4
            p=p+1  
    print(p if r==0 else p+1) '''     