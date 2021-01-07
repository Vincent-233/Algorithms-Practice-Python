def permutation_sub(ls,start,n,result):
    if start == n: # 已选完n个元素，输出
        result.append(ls[:start])
        return
    for i in range(start,len(ls)):
        ls[i],ls[start] = ls[start],ls[i]  # 后续元素依次与start交换，作为领导元素
        permutation_sub(ls,start + 1,n,result)
        ls[i],ls[start] = ls[start],ls[i]  # 再次交换，复原上次结构，方便进行下个元素的交换 

def permutation(ls, n):
    if n > len(ls) or n <= 0:
        raise ValueError('n must between 1 and length of ls')
    perm = []
    permutation_sub(ls,0,n,perm)
    return perm

if __name__ == "__main__":
    ls = [1,2,3,4]
    for x in permutation(ls,2):
        print(x)
