"""
输入s[n]，输出a[n]，a[j] = avg(s[1..n])
"""

import sys 
sys.path.append(r'E:\WeiYun\CodeVersion\CodeSample\Practice-Python\JupyterNoteBook\Temp & Test')
import decorators

@decorators.timer
def prefix_average_1(s):
    a = [0] * len(s)
    for i in range(len(s)):
        total = 0
        for j in range(i + 1):
            total += s[j]
        a[i] = total/(i + 1)
    return a

@decorators.timer
def prefix_average_2(s):
    a = [0] * len(s)
    total = 0
    for i in range(len(s)):
        total += s[i]
        a[i] = total/(i + 1)
    return a


if __name__ == "__main__":
    nums = [i for i in range(1000)]
    # print(prefix_average_1(nums))
    # print(prefix_average_2(nums))
    
    prefix_average_1(nums)
    prefix_average_2(nums)