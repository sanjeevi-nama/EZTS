#panagram -all english alphabets:sets
'''
s=input()
r=set(s.lower()) 
print(r)
print("Panagram" if(len(r)>=26) else "Not a Panagram")'''

#panagram -all english alphabets:dictionaries
'''
s=input()
d={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
d=dict.fromkeys(d,0)
for i in s:
    if i in d:
        d[i]=s.count(i)
print("Panagram" if(0 not in d.values()) else "Not a Panagram")'''

#first repeating character
'''
t=int(input())
for i in range(t):
    s=input()
    l=set(s)
    d=dict.fromkeys(l,0)
    r="."
    for j in s:
        if(s.count(j)>1):
            r=j
            break
    print(r)'''

#dict an map
'''
n=int(input())
d={}
for i in range(n):
    f,p=input().split()
    d[f]=p
while(1):
    k=input()
    if k in d:
        print(f"{k}={d[k]}")
    else:
        print("Not found")''' 

#term frequency-inverse document frequency
'''
n=int(input())
d={}
while(n):
    k=input()
    if k not in d:
        d[k]=1
    else:
        d[k]+=1
    n-=1
i=max(d.values())
l=[]
for j in d:
    if(d.get(j)==i):
        l.append(j)
print(max(l),i)'''

#database
'''
t=int(input())
for j in range(t):
    n,r=map(int,input().split())
    d={}
    for k in range(r):
        i,c=map(int,input().split())
        if c not in d:
            d[c]=[i]
        else:
            d[c].append(i)

    for i in d:
        if len(set(d[i]))!=len(d[i]) or (len(d[i])>n):
                print(f"Scenario #{j+1} : Impossible")
                break
    else:
        print(f"Scenario #{j+1} : possible")'''

            
#graph paths using dict(directed graph)
'''
n=int(input())
d={}
for i in range(n):
    x,y=input().split()
    if x not in d:
        d[x]=[y]
    else:
        d[x].append(y)
t=input()
if t in d:
    print(*d[t])
else:
    print("No routes")'''

#graph paths using dict(directed weighted graph)
'''
n=int(input())
d={}
for i in range(n):
    x,y,c=input().split()
    if x not in d:
        d[x]=[(c,y)]
    else:
        d[x].append((c,y))
t=input()
if t in d:
    r=min(d[t])
    print(r[1])
else:
    print("No routes")'''