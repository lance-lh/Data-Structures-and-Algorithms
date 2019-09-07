# matrix is fixed as below:
# matrix = [[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45]]

# solution 2: Union Find
'''
并查集思想：查找一点是否与它之后的所有点相连（条件判断）
matrix事实上不太需要，提炼出abs(x-y) == 1 or abs(x-y) == 10即可
pre 记录前导点,pre分配有6个位置的-1，根据两两相邻连接的条件，最终pre中只有1个-1
双指针遍历，后指针起点为前指针+1
find 退出条件，,最终pre[x]处为-1
'''
def find(x):
    # itself as root
    if pre[x] == -1:
        return x
    root = find(pre[x])
    pre[x] = root
    return root

while True:
    try:
        path = list(map(int,input().split()))
        pre = [-1] * 6
        for i in range(6):
            for j in range(i+1,6):
                x,y = path[i],path[j]
                if abs(x-y) == 1 or abs(x-y) == 10:
                    a,b = find(i),find(j)
                    if a != b:
                        pre[a] = b
        res = 1 if pre.count(-1) == 1 else 0
        print(res)
    except:
        break



# solution 1:back tracking
# first find head node, then set visited to not go back
# exist is pathlen, if pathlen = 6, then quit
# I tried but failed, if more time ...
'''
def haspath(matrix,path):
    visited = [False] * (5 * 5)
    pathlen = 0

    for r in range(5):
        for c in range(5):
            # find a start point to connect all points
            if matrix[r][c] in path:
                cnt = dfs(matrix, r, c, path)
                
                return True
            else:
                continue
    return False

def dfs(matrix,r,c,path,pathlen,visited):
    if pathlen == len(path):
        return True

    # flag = False
    if r>=0 and r<5 and c>=0 and c<5 and \
        matrix[r][c] == path[pathlen] and not visited[r*5+c]:
        visited[r*5+c] = True
        pathlen += 1

        dfs(matrix,r+1,c,path,pathlen,visited) \
               or dfs(matrix,r-1,c,path,pathlen,visited) \
               or dfs(matrix,r,c+1,path,pathlen,visited) \
               or dfs(matrix,r,c-1,path,pathlen,visited)

    return flag


while True:
    try:
        path = list(map(int,input().split()))
        res = haspath(matrix,path)
        print(int(res))
    except:
        break   
'''