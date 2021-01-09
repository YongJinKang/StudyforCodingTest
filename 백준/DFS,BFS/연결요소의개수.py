index_number=[]
def dfs(graph, v, visited):
    
    visited[v] = True
    print(v, end= ' ')
    index_number.append(v)
    print(index_number)

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            return True
    return False


n, m = map(int,input().split())
print(n,m)
graph = [[]]
for i in range(m):
    graph.append(list(map(int,input().split())))

graph.sort()

print(graph)

visited = [False] * n

print(dfs(graph,1,visited))

# def dfs():




