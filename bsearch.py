def binary_search(arr,low,high,key):
    mid=(low+high)//2
    if low<=high:
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binary_search(arr,mid+1,high,key)
        else:
             return binary_search(arr,low,mid-1,key)