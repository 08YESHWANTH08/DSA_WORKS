array=list(map(int,input("Enter the Elements Of The Array (With Space): ").split(" ")))
n=len(array)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if(array[min]>array[j]):
            min=j
    if(min!=i):
        array[min],array[i]=array[i],array[min]
    print(f"After {i+1} Iteration, Given Array : {array}")