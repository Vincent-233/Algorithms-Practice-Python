import os
def disk_usage(path):
    """return then number of bytes used by a path
    O(n) time
    """
    size = os.path.getsize(path) # return the direct uasage
    if os.path.isdir(path):      # if a folder recursive dive into it
        for dir in os.listdir(path):
            size = size + disk_usage(os.path.join(path,dir))
    print('{0:<10}'.format(size),path) # optional to print the path and current total size
    return size

if __name__ == "__main__":
    # the same result as commond `du -ab`
    # it's like a tree traversal
    path = r'D:\02-Work'
    print(disk_usage(path))