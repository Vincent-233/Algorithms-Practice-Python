def binary_search(data,target):
    """the iterative version of binary search"""
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if target > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    data = [3,5,7,9,11]
    target = (1,2,3,4,5,6,7,8,9,10,11,12)
    for t in target:
        print(t,binary_search(data,t))