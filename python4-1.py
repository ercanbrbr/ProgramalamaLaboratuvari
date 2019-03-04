matrix_1=[[1,2,3],[4,5,6]]
matrix_2=[[7,8,9],[10,11,12]]

matrix_3=[[1,2],[3,4]]
matrix_4=[[5,6,7],[8,9,10]]
alpha=10

def my_vector_inner_product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    
    for i in range(size):
        my_result[i]=v[i]*w[i]

    t=0
    for i in range(size):
        t=t+my_result[i]

    return t

def mat_topla(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]+m2[row][column])
    return result        

def mat_cikar(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]-m2[row][column])
    return result      

def mat_skaler_carp(m1,alpha):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]*alpha)
    return result     

def f1(m1,i):
    return m1[i]
def f2(m1,j):
    my_j_th_col=[]
    for row in m1:
        for indis in range(len(row)):
            if(indis==j):
                my_j_th_col.append(row[indis])
    return my_j_th_col

def mat_carp(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m2[0])):
            a=f1(m1,row)
            b=f2(m2,column)
            c=my_vector_inner_product(a,b)
            result[row].append(c)
    return result     


print(mat_topla(matrix_1,matrix_2))
print(mat_cikar(matrix_1,matrix_2))
r=mat_skaler_carp(matrix_1,alpha)
print(f1(matrix_1,1))
print(f2(matrix_2,2))
print(mat_carp(matrix_3,matrix_4))
