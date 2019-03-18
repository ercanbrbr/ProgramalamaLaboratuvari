def dynamicbozuk(bozuklukList,paraüstü,minKurus,kullanılanKurus):
   for kurus in range(paraüstü+1):
      kurusSayısı = kurus
      yeniKurus = 1
      for j in [c for c in bozuklukList if c <= kurus]:
            if minKurus[kurus-j] + 1 < kurusSayısı:
               kurusSayısı = minKurus[kurus-j]+1
               yeniKurus = j
      minKurus[kurus] = kurusSayısı
      kullanılanKurus[kurus] = yeniKurus
   return minKurus[paraüstü]

def printKurusları(kullanılanKurus,paraüstü):
   coin = paraüstü
   while coin > 0:
      thisCoin = kullanılanKurus[coin]
      print(thisCoin)
      coin = coin - thisCoin

deger = 21
clist = [1,5,10,21,25]
kullanılanKurus = [0]*(deger+1)
kurusSayısı = [0]*(deger+1)

print("Making paraüstü for",deger,"requires")
print(dynamicbozuk(clist,deger,kurusSayısı,kullanılanKurus),"coins")
print("They are:")
printKurusları(kullanılanKurus,deger)
print("The used list is as follows:")
print(kullanılanKurus)