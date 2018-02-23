import  codecs as cod
import sys

def fibo(n):
    a=1
    b=1
    if n==1:
        print(a, end=" ")
    elif n==2:
        print(a,b,end=" ")
    else:
        c=a+b
        print(a,b,c, end=" ")
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c,end=" ")
            k+=1

def fibo2(n):
    a=1
    b=1
    k=1
    fajl=open("ki1.txt",mode="w")
    while k<n:
        fajl.write("%.4f " % (a/b))
        a=a+b
        b=a-b
        k=k+1
    fajl.close()

def feladat1(fajl_nev):
    fajl = cod.open(fajl_nev,encoding='utf-8', mode="r")
    max=0
    max_sor=""
    for sor in fajl:
        sor=sor.strip()
        if(sor[0].isupper() and len(sor)>max):
            max= len(sor)
            max_sor=sor
    print(max, max_sor)
    fajl.close()

def feladat2():
    fajl=open("be1.txt",mode="r")
    for sor in fajl:
        if("   " in sor):
            fajl=open("ki1.txt",mode="w")
            fajl.write(sor)
            fajl.close()
            break
def fel7(lista,betu):
    li=[]
    fajl= open("ki2.txt", mode="w")
    for i in lista:
        if i[0]==betu:
            li.append(i)

    fajl.write(str(li))
    fajl.close()

def kivetel():
    s="alma"
    try:
        # print(1 / 0)
        # print(s[10])
        print("try-ban benn")
    except ZeroDivisionError as e:
        print("Zéróval osztottunk, vigyázz")
    except Exception as e:
        print("legáltalánosabb kivétel dobódott",e)
    finally:
        print("Az itt lévő utasítás miden esetben végre hajtódik!")

    print("vége a try-nak")

def fel3():
    try:
        fajl=cod.open(sys.argv[1],encoding="utf-8",mode="r")
        nagy=True
        for sor in fajl:
            li=sor.split(" ")
            for szo in li:
                if(not szo[0].isupper()):
                    nagy=False
                    break
            if nagy :
                print(sor)
                break
            else:
                nagy=True
    except FileExistsError:
        print("Nem létezik a fajl")
    except Exception as e:
        print("valamlyen kivétel dobódott:",e)

def fel4():
    try:
        fajl=open(sys.argv[2],mode="r")
        scoreA=0
        scoreB=0
        for sor in fajl:
            sor=sor.strip()
            a,b=sor.split("-")
            if a=="ko" and b=="ollo":
                scoreA=scoreA+1
            elif a=="ko" and b=="papir":
                scoreB=scoreB+1
            elif a=="papir" and b=="ko":
                scoreA = scoreA + 1
            elif a=="papir" and b=="ollo":
                scoreB=scoreB+1
            elif a=="ollo" and b=="papir":
                scoreA=scoreA+1
            elif a=="ollo" and b=="ko":
                scoreB=scoreB+1
            else:
                scoreA=scoreA+1
                scoreB=scoreB+1

        if scoreB>scoreA:
            print("A második nyert")
        elif scoreA>scoreB:
            print("Az első nyert")
        else:
            print("dontetle")
    except OSError:
        print("hiba a fájl megnyitása közben")
    except Exception:
        pass

def fel5():
    try:
        fajl=open("hallgato.txt",mode="r")
        fajl2= open("ki_hallgato.txt",mode="w")
        for sor in fajl:
            sor=sor.strip()
            h=sor.split(";")
            sum=0
            for i in h[2:]:
                sum=sum+int(i)
            fajl2.write("%s %d\n" % (h[1],sum))
    except OSError as e:
        print(e)
    except Exception:
        pass
    finally:
        fajl.close()
        fajl2.close()








def main():
   #feladat1("be1.txt")
   #feladat2()
   #fel7(["alma", "ananasz","naracs"],'a')
   #kivetel()
   fel5()
if __name__ == '__main__':
    main()







