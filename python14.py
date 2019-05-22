a=[[1,2,3],[4,5,6],[7,8,9]]
def copy(a=[]):
    b=[]
    m=len(a)
    n=len(a[0])
    for i in range(m):
        b.append([])
        for j in range(n):
            b[i].append(a[i][j])
    return b
def birim(n):
    b=[]
    for i in range(n):
        b.append([])
        for j in range(n):
            b[i].append(0)
    for i in range(n):
        b[i][i]=1
    return b
def tersi(a):
    n=len(a)
    BM=copy(a)
    I=birim(n)
    IM=copy(I)
    indices=list(range(n))
    for fd in range(n):
        fdscaler=1.0/BM[fd][fd]
        for j in range(n):
            BM[fd][j]*=fdscaler
            IM[fd][j]*=fdscaler
        for i in indices[0:fd]+[fd+1:]:
            crscaler=BM[i][fd]
            for j in range(n):
                BM[i][j]=BM[i][j]-crscaler*BM[fd][j]
                IM[i][j]=IM[i][j]-crscaler*IM[fd][j]
    return IM
print(tersi(a))