def frekans(list):
    say=0
    liste=[]
    for i in range(len(list)):
        for j in range(len(list)):
            if(list[i]==list[j]):
                say=say+1
        str = list[i], say
        liste.append(str)
        say=0
    return liste


list = [5,7,3,2,3,7,8]
print(frekans(list))

print(list)