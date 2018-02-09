import math as mt

def is_prim(n):
    prim=True

    if n==1:
        prim=False

    for i in range(3,int(mt.sqrt(n))+1):
        print(i)
        if n%i==0:
            prim=False

    return prim


def lnko(a,b):

    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break

    return a

def palindrom(szam):
    masolat=szam
    uj_szam=0
    while szam!=0:
        szj=szam%10
        szam=szam//10
        uj_szam=uj_szam*10+szj

    return uj_szam==masolat

def fibo(n):
    a=1
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b, end=" ")
    else:
        c=a+b
        print(a,b,c,end=" ")
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c,end=" ")
            k=k+1

def fibo_arany(n):
    a=1
    b=1

    for i in range(1,n+1):
        print("%.4f" % (a/b),end=" ")
        a=a+b
        b=a-b


def haromszog():


    while True:
        a = float(input("Kérem a háromszög oldalait:"))
        b = float(input("Kérem a háromszög oldalait:"))
        c = float(input("Kérem a háromszög oldalait:"))
        if a<=0 or b<=0 or c<=0:
            print ("Hibás adatok")
        else:
            break

    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        T=mt.sqrt(p*(p-a)*(p-b)*(p-c))
        R=(a*b*c)/(4*T)
        r=T/p
        print("A háromszogbe írt kor sugatar %.2f, a köré írt kör sugara=%.2f" % (r,R))
    else:
        print("Nem")


def fg(x):

    if x>-2 and x<0:
        f=2*x
    elif x>=0 and x<2:
        f=x*x
    elif x>2:
        f=10
    else:
        print("Nem definiált")
        return
    return f


def main():
    print(is_prim(1))
    print(palindrom(11311))
    fibo(10)
    print()
    fibo_arany(20)
    print()
    # haromszog()
    print(fg(-10))
    print("Javitott sor")



if __name__=="__main__":
    main()
