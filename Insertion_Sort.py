array=[3,2,1]
n=len(array)
for i in range(1,n):
    temp=array[i]
    j=i-1
    while(j>=0 and array[j]>temp):
        array[j+1]=array[j]
        j-=1
    array[j+1]=temp
print(array)