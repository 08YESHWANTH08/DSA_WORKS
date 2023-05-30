def BinarySearch(array,start,end,element):
    if(start>end):
        return f"{element} not found in {array}"
    mid=(start+end)//2
    if(array[mid]>element):
        return BinarySearch(array,start,mid-1,element)
    elif(array[mid]==element):
        return f"{element} found in {array} at index {mid}"
    else:
        return BinarySearch(array,mid+1,end,element)
array=list(map(int,input("Enter The Array Elements (With Space): ").split(" ")))
array.sort()
element=int(input("Enter the Element To Search: "))
n=len(array)
start=0
end=n-1
print(BinarySearch(array,start,end,element))