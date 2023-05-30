array=list(map(int,input("Enter the Elements Of The Array (With Space): ").split(" ")))
n=len(array)
for i in range(n-1):
    for j in range(n-i-1):
        if(array[j]>array[j+1]):
            array[j],array[j+1]=array[j+1],array[j]
    print(f"After {i+1} Iteration, Given Array : {array}")