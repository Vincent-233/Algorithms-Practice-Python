def liner_sum(ls,n):
    """return the sum of first n numbers of list ls"""
    if n == 0:  # if only one left,return it
        return ls[n]
    return ls[n] + liner_sum(ls, n - 1)

if __name__ == "__main__":
    ls = [1,1,2,2,3,3]
    print(liner_sum(ls,len(ls) - 1 ), sum(ls))