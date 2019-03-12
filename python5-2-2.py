from decimal import Decimal

def bozukluk(para,tutar):
    kalan=("%.2f" % (para-tutar))
    bozuk=[0.50,0.25,0.21,0.10,0.05,0.01]
    kalanbozuk={}
    paraustu=[0,0,0,0,0,0]
    if(float("%.2f" % (float(kalan)%float(0.21)))==0.00):
        paraustu[2]=int("%.0f" % (float(kalan)/float(0.21)))
        kalan=0
    for i in range(len(bozuk)):
        while(float(kalan)-bozuk[i]>=0):
            kalan=Decimal(kalan)-Decimal(bozuk[i])
            paraustu[i]+=1
            
    for j in range(len(bozuk)):
        kalanbozuk[bozuk[j]]=paraustu[j]
    return(kalanbozuk)

print(bozukluk(10.00,9.37))