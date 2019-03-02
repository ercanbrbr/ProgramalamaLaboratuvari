import random

def generate_an_array(n):
    my_arr=[]
    for i in range(n):
        s=random.randint(0,100)
        my_arr.append(s)#--- s elemanını diziye ekler
    return my_arr

my_arr_list=generate_an_array(5)
print(my_arr_list)
print("\n")

for i in range(len(my_arr_list)):
    print(i+1,".index :",my_arr_list[i])
print("\n")

def print_array(dizi):
    for item in my_arr_list:
        print(item, end=" ")
    print("\n")
print("FONKSIYON ile YAZDIRMA-------------")
print_array(my_arr_list)

def my_bubble_sort(my_array):
    for i in range(len(my_array)-1,0,-1):
        for j in range(i):
            if(my_array[j]>my_array[j+1]):
                temp=my_array[j]
                my_array[j]=my_array[j+1]
                my_array[j+1]=temp

print("SIRALI LISTE")            
print_array(my_bubble_sort(my_arr_list))   


def eleman_ara(dizi,n):
    found=False
    step=0
    for i in range(len(dizi)):
        if(dizi[i]==n):
            found=True
            step=i
    print(found,"bulunan elemanın sırası : ",step+1)

print(eleman_ara(my_arr_list,5))            