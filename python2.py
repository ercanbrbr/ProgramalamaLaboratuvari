def fibo_loop(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a

def fibo_rec(n):
    if(n<2):
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)

def fibo_rec2(n,memo):
    if(memo[n]!=None):
        return memo[n]
    if(n<2):
        result=1
    else:
        result=fibo_rec(n-1)+fibo_rec(n-2)
    memo[n]=result
    return result

def fib_memo(n):
    memo=[None]*(n+1)
    return fibo_rec2(n,memo)

def fibo_bottomup(n):
    if (n==1 or n==2):
        return 1
    bottomup=[None]*(n+1)
    bottomup[1]=1
    bottomup[2]=1
    for i in range(3,n+1):
        bottomup[i]=bottomup[i-1]+bottomup[i-2]
    return bottomup[n]

def fakt(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

def fakt_rec(n):
    if(n==1):
        return n
    else:
        return n*fakt_rec(n-1)

def power(m,n):
    s=m
    for i in range(1,n):
        s=s*m
    return s

def power_rec(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    elif(n%2==0):
        return power_rec(m*m,int(n/2))
    elif(n%2!=0):
        return power_rec(m*m,int(n/2))*m
    return m

print(fibo_loop(15))
print(fibo_rec(15))
print(fib_memo(15))
print(fibo_bottomup(15))
print(fakt(5))
print(fakt_rec(5))
print(power(5,7))
print(power_rec(5,7))