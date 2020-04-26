- typical default max recursive depth of python is 1000. use below code to change it:
    ``` python
    import sys
    old = sys.getrecursionlimt()
    sys.setrecursionlimt(100000) 
    ```
- We organize our presentation by considering the maximum number of recursive calls that may be started from within the body of a single activation
    - If a recursive call starts at most one other, we call this a linear recursion.
    - If a recursive call may start two others, we call this a binary recursion.
    - If a recursive call may start three or more others, this is multiple recursion.

- designing recursive algorithms 
    - test for base cases
    - if not a base case, perform one or more recursive calss. 
    -  redefine the original problem to facilitate similar-looking subproblems, usually involve reparameterizing the function

- 关于尾递归
    - 尾递归优化后（若支持）可以减少过多调用堆栈的开销
    - [递归和尾递归的区别和原理](https://blog.csdn.net/zcyzsy/article/details/77151709)
    - [尾调用优化](https://www.ruanyifeng.com/blog/2015/04/tail-call.html)
    - python语言本身不支持尾递归，但可用装饰器实现，参考[Python尾递归优化方法](https://www.cnblogs.com/zhuminghui/p/9145549.html)