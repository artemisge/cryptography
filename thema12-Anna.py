import math

def continuousfraction(N,e):
    a=[-1 for i in range(0,1000)]
    a[0]=0
    i=1
    while N/e>0:
        temp=N
        N=e
        e=temp
        x=e/N
        a[i]=math.floor(x)
        e=e-(N*a[i])
        i=i+1
        if (e==0):
            break
    a=[a[i] for i in range(0,i)]
    return a_



def kd(a):

    kd=[[0 for x in range(0,2)] for y in range(0,len(a))]
    kd[1][0]=1
    kd[1][1]=a[1]
    for i in range(2,len(a)):
        ar=1
        par=1
        temp1=a[i]
        for j in range(i,1,-1):
            par=a[j-1]*temp1+ar
            ar=temp1
            temp1=par
        kd[i][0]=ar
        kd[i][1]=par
    return kd

def f(e,k,d):

    return int((ed - 1)/k)

def eq(N,f):
    temp=-N+f-1
    D=int(temp**2-4*N)
    if (D<0):
        return False
    if (D==0):
        if (temp==N):
            return True

    x1=int(temp-math.sqrt(D))
    x1=int(x1/2)
    x2=int(temp+math.sqrt(D))
    x2=int(x2/2)
   # print(x1,"   ",x2)
   # print(x1x2)
    return x1x2==N

def check_effectiveness(N,d):
    return N**(1/4)/3>d



N=194749497518847283
e=50736902528669041

#N=5697733
#e=3105251

a=continuousfraction(N, e)

kd=kd(a)
#print(kd)

d=0
for i in range(1,len(a)):
    f=f(e,kd[i][0],kd[i][1])
    #print(f)
    if(eq(N,f)):
        d=kd[i][1]
        print(d)
        break

if (check_effectiveness(N,d)):
    print("All good")
else:
    print("Not good bro")
