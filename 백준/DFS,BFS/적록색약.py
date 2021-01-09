n = int(input())
graph = []
visited=[]
visited2=[]
for i in range(n):
    graph.append(str(input()))
    
for i in range(n):
    visited.append([])
    visited2.append([])
    for j in range(n):
        visited[i].append("False")
        visited2[i].append("False")
print(visited)
print(visited2)

def rdfs(x, y):
    
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "R" and visited[x][y] == "False":
        visited[x][y] = "True"
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        rdfs(x - 1, y)
        rdfs(x, y - 1)
        rdfs(x + 1, y)
        rdfs(x, y + 1)

        return True
    else:

        return False

def gdfs(x, y):
    
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "G" and visited[x][y] == "False":
        visited[x][y] = "True"
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        gdfs(x - 1, y)
        gdfs(x, y - 1)
        gdfs(x + 1, y)
        gdfs(x, y + 1)

        return True
    else:

        return False

def bdfs(x, y):
    
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "B" and visited[x][y] == "False":
        visited[x][y] = "True"
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        bdfs(x - 1, y)
        bdfs(x, y - 1)
        bdfs(x + 1, y)
        bdfs(x, y + 1)

        return True
    else:

        return False




result = 0
for i in range(n):
    for j in range(n):
        #현재 위치에서 DFS 수행
        if rdfs(i,j) == True:
            result += 1
        elif gdfs(i,j) == True:
            result += 1
        elif bdfs(i,j) == True:
            result += 1
print(f"적록색약이 아닌 사람이 봤을 때의 결과 : {result}")


# print(graph2)
##적록색약인 사람이 봤을 때의 구역의 수 구하기

def rgdfs(x, y):
    
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if (graph[x][y] == "R" or graph[x][y]=="G") and visited2[x][y] == "False":
        visited2[x][y] = "True"
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        rgdfs(x - 1, y)
        rgdfs(x, y - 1)
        rgdfs(x + 1, y)
        rgdfs(x, y + 1)

        return True
    else:

        return False


def bdfs2(x, y):
    
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "B" and visited2[x][y] == "False":
        visited2[x][y] = "True"
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        bdfs2(x - 1, y)
        bdfs2(x, y - 1)
        bdfs2(x + 1, y)
        bdfs2(x, y + 1)

        return True
    else:

        return False


result2 = 0
for i in range(n):
    for j in range(n):
        #현재 위치에서 DFS 수행
        if rgdfs(i,j) == True:
            result2 += 1
        elif bdfs2(i,j) == True:
            result2 += 1
print(f"적록색약이 아닌 사람이 봤을 때의 결과 : {result2}")
