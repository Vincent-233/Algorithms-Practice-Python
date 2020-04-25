def binary_search_sub(data,target,low,high):
    """recursion search. 
       return index of target, return -1 if not found
       O(logn) time
    """
    if low > high:
        return -1
    mid = (low + high) // 2
    if target == data[mid]:
        return mid
    if target > data[mid]:
        low = mid + 1
    else:
        high = mid - 1
    return binary_search_sub(data,target,low,high)

def binary_search(data,target):
    return binary_search_sub(data,target,0,len(data) - 1)

if __name__ == "__main__":
    data = [3,5,7,9,11]
    target = (1,2,3,4,5,6,7,8,9,10,11,12)
    for t in target:
        print(t,binary_search(data,t))