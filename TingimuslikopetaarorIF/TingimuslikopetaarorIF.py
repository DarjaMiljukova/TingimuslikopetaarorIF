from math import *
from pickle import TRUE
from random import *
from time import *


#Ülesanne 1
#try:
#    nimi=input("Sisestage oma nimi ")

#    if nimi.upper()=="JUKU":
#        print("Lähme kinno")
#        vanus=int(input("Kui vana sa oled? "))
#        if vanus<=0 or vanus>=100:
#            print("Viga andmetega")
#        elif vanus<6:
#            print("Tasuta")
#        elif vanus>=6 and vanus<=14:
#            print("Lapse pilet")
#        elif vanus>=15 and vanus<=65:
#            print("Täispilet")
#        elif vanus>=65:
#            print("Sooduspilet")
#        elif vanus<=0 or vanus>=100:
#            print("Viga andmetega")

#    else:
#        print("Otsime Juku")
#except:
#    print("Vale Andmetüüp")

##Ülesanne 2
#nimi1=input("Mis sinu nimi on? ")
#nimi2=input("Mis sinu nimi on? ")
#if nimi1.isalpha()==True and nimi2.isalpha():
#    if nimi1.lower()==("Liri") and nimi2.lower()==("Kiri"):
#        print(f"{nimi1} ja {nimi2} olete täna naabrid")
#    else:
#        print()
#else:
#    print("Vale Andmetüüp")

##Ülesanne 3
#try:
#    a=float(input("määrake ristkülikukujulise ruumi pikkus ->"))
#    b=float(input("määrake ristkülikukujulise ruumi laius ->"))
#    if a>=0 and b>=0:
#        S=a*b
#        print(f"ristküliku pindala on {S}")
#        c=int(input("Kas te soovite remonti teha? kui 1=ja või 0=ei: "))
#        if c==1:
#            print("Kui palju ta maksab ruutmeeter ja mitu põranda vahetamise hind?")
#        else:
#            print("Hüvasti")
#    else:
#        print("Vale Andmetüüp")
#except:
#    print("Vale Andmetüüp")

##Ülesanne 4
#try:
#    hind=float(input("Mis hind?"))
#    if hind>0:
#        if hind>700:
#                print(f"Sul on soodus 30%, {hind-hind*0.3}")

#        else:
#            print(f"{hind}")
#except:
#    print("Vale Andmetüüp")


#Ülesanne 5
#n=int(input("Mitu toa korteris?"))
#for i in range(1,n+1,1): #range(n) i=1,2,3,.....,n
#    t=float(input(f"{i}. toa temperatuur: "))
#    if t>18:
#        print("Soe")
#    else:
#        print("Külm")


#Ülesanne 6
#p=k=l=0
#kogus=randint(1,20)
#print("Kokku on",kogus,"inimest")
#while kogus>0:
#    kogus-=1
#    pikkus=randint(56,256)
#    if pikkus>178:
#        print("Pikk")
#        p+=1
#    elif pikkus>155 and pikkus<=178:
#        print("Keskmine")
#        k+=1
#    else:
#        print("Lühike")
#        l+=1
#print(f"Pikka kasvu {p} inimest")    
#print(f"Keskmine kasvu {k} inimest")
#print(f"Lühike kasvu {l} inimest")

#Ülesanne 7
a=0
b=1
while a!=b:
    while True:
        try:
            a=float(input("Sisesta 1. külg: "))
            break
        except:
            print("Sisesta veel kord")
    while True:
        try:
            b=float(input("Sisesta 2. külg: "))
            break
        except:
            print("Sisesta veel kord")
    if a!=b: print("Andmetüüb on ok, vaid see ei ole ruud!")
print(f"See on ruud. Ruudu külg võrdub {a}")

#Ülesanne 8
#try:
#    a=int(input("Kas soovite piima osta?(jah-1 või ei-0): "))
#    b=int(input("Kas soovite saia osta?(jah-1 või ei-0): "))
#    c=int(input("Kas soovite leiba osta?(jah-1 või ei-0): "))
#    if a<0 and b<0 and c<0:
#        print("Error")
#    if a==1 and b==0 and c==0:
#        piim=0.79
#        sai=0
#        leib=0
#        S=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",S)
#    elif a==0 and b==1 and c==0:
#        piim=0
#        sai=0.8
#        leib=0
#        P=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",P)
#    elif a==0 and b==0 and c==1:
#        piim=0
#        sai=0
#        leib=0.8
#        F=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",F)
#    elif a==1 and b==1 and c==0:
#        piim=0.79
#        sai=0.8
#        leib=0
#        L=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",L)
#    elif a==0 and b==1 and c==1:
#        piim=0
#        sai=0.8
#        leib=0.8
#        O=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",O)
#    elif a==1 and b==0 and c==1:
#        piim=0.79
#        sai=0
#        leib=0.8
#        U=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",U)
#    elif a==1 and b==1 and c==1:
#        piim=0.79
#        sai=0.8
#        leib=0.8
#        A=piim+sai+leib
#        print("Kõik ostetud asjad maksavad",A)
#except:
#    print("Vale Andmetüüp")


#Ülesanne 9
#try:
#    a=float(input("Utle pool a "))
#    b=float(input("Utle pool b "))
#    if a==b:
#        print("See on ruut")
#    else:
#        print("See ei ole ruut")
#except:
#    print("Value Error")


#Ülesanne 10
#try:
#    a=float(input("1 number "))
#    b=float(input("1 number "))
#    c=input("mis märk sa oled +-*/ \n ")
#    if c==("+"):
#        print(a+b)
#    elif c==("-"):
#        print(a-b)
#    elif c==("*"):
#        print(a*b)
#    elif c==("/"):
#        if b==0:
#            print("Väiksem kui 0")
#        else:
#            print(a/b)
#except:
#    print("Value Error")

#Ülesanne 11
#now = datetime.datetime.now()
#try:
#    a=int(input("Sisesta sünniaasta. "))
#except:
#    print("Value Error")
#b=int(now.year)
#c=int(b-a)
#print(c)
#f=c%5
#if f==0:
#    print("teil on juubel")
#else:
#    print("Kui kaju")

#Ülesanne 12
#try:
#    a=float(input("sisesta toote hind "))
#    if a<=10:
#        print("sul on soodus 10%",a-a*0.1)
#    elif a>10:
#        print("sul on soodus 20%",a-a*0.2)
#except:
#    print("Value Error")

#Ülesanne 13
#try:
#    a=int(input("Kas sa oled mees?(jah-1 või ei-0) \n"))
#    if a==1:
#        b=int(input("Kui vana sa oled? "))
#        if b>=16 and b<=18:
#            print("sa sobid")
#    else:
#        print("sa oled naine sest, et sa ei sobi")
#except:
#    print("Value Error")