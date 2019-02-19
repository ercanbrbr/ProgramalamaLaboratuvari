#selection sort
def mySearchSelection(my_array):
    for i in range(len(my_array)-1,0,-1):
        maxIndex=0
        for j in range (1,i+1):
            if(my_array[j]>my_array[maxIndex]):
                maxIndex=j
        temp=my_array[j]
        my_array[j]=my_array[maxIndex]
        my_array[maxIndex]=temp
    return
#binary search
def binarySearch(sortedarray,item):
    first=0
    last=len(sortedarray)-1
    found=False
    s=0
    while first<=last and not found:
        midpoint=(first+last)//2
        print("first - last",first,last)
        if(sortedarray[midpoint]==item):
            found=True
        else:
            if(item<sortedarray[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
                s=s+1
    return found,midpoint,s

my_arr=[11,27,7,98,55,9,8,31,69,77,34]
mySearchSelection(my_arr)
print(my_arr)
print(binarySearch(my_arr,27))