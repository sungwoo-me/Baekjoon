N,M = map(int,input().split())

s =[]

def dfs(num):
    if len(s) == M :
        print(*s)
        return 

    for i in range(num,N+1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)