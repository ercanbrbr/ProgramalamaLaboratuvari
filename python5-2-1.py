from decimal import Decimal

def bozukluk(para,tutar):
    kalan=("%.2f" % (para-tutar))
    bozuk=[0.50,0.25,0.10,0.05,0.01]
    kalanbozuk={}
    paraustu=[0,0,0,0,0]
    for i in range(len(bozuk)):
        while(float(kalan)-bozuk[i]>=0):
            kalan=Decimal(kalan)-Decimal(bozuk[i])
            paraustu[i]+=1
            
    for j in range(len(bozuk)):
        kalanbozuk[bozuk[j]]=paraustu[j]
    print(kalanbozuk)

bozukluk(10.00,9.23)