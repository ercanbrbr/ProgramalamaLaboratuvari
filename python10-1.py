import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(denemesayısı):
    numWins = 0
    for i in range(denemesayısı):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print('Kazanma İhtimali =', numWins/denemesayısı)

checkPascal(100)


def passline(denemesay):
    winSay=0
    eskizar=0
    for i in range(denemesay):
        d1= rollDie()
        d2= rollDie()
        if(d1+d2==7 or d1+d2==11):
            winSay+=1
        elif(d1+d2==2 or d1+d2==3 or d1+d2==12):
            continue
        else:
            while(1):
                eskizar=d1+d2
                d1= rollDie()
                d2= rollDie()
                if d1+d2==7:
                    break
                if d1+d2==eskizar:
                    winSay+=1
                    break
    print("Kazanma Olasılığı..:",winSay/denemesay)


passline(100)