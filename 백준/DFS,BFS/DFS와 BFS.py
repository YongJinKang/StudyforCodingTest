def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n,m,v = map(int,input().split())
print(n,m,v)
graph = []
print(graph)
for i in range(m):
    a,b= map(int,input().split())
    graph.append([a,b])
    
    
visited = [False] * int(m+1)
print("graph:",graph)
print("visited:",visited)

dfs(graph, v, visited)




# print(n,m,v, sep = '\t')
# print(line)

# def dcf(graph,v, visited):


