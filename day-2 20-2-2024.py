#R-sugarcane juice business
'''
def cal_profit(n):
    ti=n*50
    spends=ti*0.7
    return int((ti-spends))

for i in range(int(input())):
    n=int(input())
    print(cal_profit(n))''' 

#R-sugarcane juice business(recursive)
'''
def cal_profit(n):
    return int(n*50-n*35)

def test(t):
    if(t==0):
        return
    else:
        n=int(input())
        print(cal_profit(n))
        test(t-1)
t=int(input())
test(t)'''

#S-watching movies at 2x speed 
'''
def time(x,y):
    print(x-y//2)  
x,y=map(int,input().split())
time(x,y)
#y//2+(x-y) == x-y//2'''

#W- lucky four 2 rec fun
'''
def no_of_fours(n,count=0):
    if n==0:
        print(count)
    else:
        if(n%10 == 4):
            count=count+1
        n=n//10
        no_of_fours(n,count)

def test(t):
    if t==0:
        return 
    else:
        n=int(input())
        no_of_fours(n)
        test(t-1)

t=int(input())
test(t)'''

#W- lucky four 1 rec fun
'''
def fours(n,c=0):
    if(n==0):
        print(c)
    else:
        d=n%10
        if(d==4):
           c=c+1
        n=n//10
        fours(n,c)
for i in range(int(input())):
    n=int(input())
    print(fours(n))'''

#compute n factorial-for loop
'''
n=int(input())
r=1
for i in range(1,n+1): 
    r=r*i
print(r)'''

'''#compute n factorial-while loop
n=int(input())
r=1
while(n):
    r=r*n
    n=n-1
print(r)'''

#compute n factorial-rec fun
'''
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*fact(n-1))
n=int(input())
print(fact(n))'''

#append three for 3 digit no
'''
def three(n):
    r1=(((n/1000)+3)*1000)*10+3
    print(int(r1))
n=int(input())
three(n)'''

#append three for n digit no
'''
def rev(n):
    r=0
    while(n!=0):
        r=r*10+(n%10)
        n=n//10
    return r

def three(n):
    n=n*10+3
    k=rev(n)
    k=k*10+3
    print(rev(k))

n=int(input())
three(n)'''

