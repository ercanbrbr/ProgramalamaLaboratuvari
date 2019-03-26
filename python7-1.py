import random
import pylab
import numpy

# def ZarAt():
#     """Return a random int between 1-6"""
#     return random.choice([1,2,3,4,5,6])

# def Tane(n):
#     result=''
#     for i in range(n):
#         result= result+str(ZarAt())+" "
#     print(result)

# Tane(10)

# def at(atmaSayısı):
#     heads=0
#     for i in range(atmaSayısı):
#         if random.choice(('H','T')) == 'H':
#             heads+=1
#     return heads/atmaSayısı
# def atSim(numFlipsPerTrial, denemeSayısı):
#     fracHeads=[]
#     for i in range(denemeSayısı):
#         fracHeads.append(at(numFlipsPerTrial))
#         mean=sum(fracHeads)/len(fracHeads)
#     return mean

# print(atSim(10,10000))
def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
                numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'k')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'k')
random.seed(0)
flipPlot(4, 20)