class oku():
    def __init__(self,dosyam=""):
        f=open("C:\\Users\\asus\\Desktop\\file.txt","r")
        kitap=f.read()
        cumleler=kitap.split(".")#cümlelere ayır,listeye at
        self.kelime=[]
        for i in cumleler:
            kelimeler=i.split(" ")
            for k in kelimeler:
                self.kelime.append(k)
        self.kelimefrekans()
        self.kelimefrekyaz()
        self.kelimefrek2li()
        self.kelimefrek2yaz()
    def kelimefrekans(self):
        self.freklist1={}
        for k in self.kelime:
            if(k in self.freklist1):
                self.freklist1[k]+=1
            else:
                self.freklist1[k]=1
    def kelimefrekyaz(self):
        for k in self.freklist1:
            print(k+" "+str(self.freklist1[k]))
    def kelimefrek2li(self):
        self.freklist2={}
        for k in range(len(self.kelime)-1):
            w1,w2=self.kelime[k],self.kelime[k+1]
            if((w1,w2) in self.freklist2):
                self.freklist2[(w1,w2)]+=1
            else:
                self.freklist2[(w1,w2)]=1
            
    def kelimefrek2yaz(self):
        for k in self.freklist2:
            print(str(k)+" "+str(self.freklist2[k]))

oku1=oku()