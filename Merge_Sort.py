def mergesort(l):
    n=len(l)
    if n>1:
        r=n//2
        sub1=l[:r]
        sub2=l[r:]
        n1=len(sub1)
        n2=len(sub2)
        mergesort(sub1)
        mergesort(sub2)
        i=j=k=0
        while(i<n1 and j<n2):
            if(sub1[i]<sub2[j]):
                l[k]=sub1[i]
                i+=1
            else:
                l[k]=sub2[j]
                j+=1
            k+=1
        while(i<n1):
            l[k]=sub1[i]
            i+=1
            k+=1
        while(j<n2):
            l[k]=sub1[j]
            j+=1
            k+=1

l=[21,13,12]
mergesort(l)
print(l)