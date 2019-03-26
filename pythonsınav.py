class oku():
    def __init__(self, dosya=""):
        f=open("C:\\Users\\asus\\Desktop\\file.txt","r")
        myContent=f.read()
        cümle = myContent.split(".")
        self.myWords=[]
        for sentence in cümle:
            WordsInTheSentence=sentence.split(" ")
            for word_1 in WordsInTheSentence:
                self.myWords.append(word_1)
        self.frek1()
        # self.frek2(self.words)
        self.wfrek1()
        # self.wfrek2(self.words)
        
    def frek1(self):
        self.freklist1={}
        for word in self.myWords:
            if(word in self.freklist1):
                self.freklist1[word]+=1
            else:
                self.freklist1[word]=1
        
    # def frek2():
    def wfrek1(self):
        for word1 in self.freklist1:
            print(word1+" "+str(self.freklist1[word1]))
    # def wfrek2():

myclass1=oku()
print(myclass1.freklist1['all'])