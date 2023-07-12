from collections import defaultdict,deque
def parallelCourses(n, prerequisites):
    # Write your code here.

    graph = defaultdict(list)
    indgree = [0]*n
    for a,b in prerequisites:
        graph[a].append(b)
        indgree[b-1] += 1

    q = deque()
    visited = set()
    output = [0]*n
    for i in range(len(indgree)):
        if indgree[i] == 0:
            q.append((i+1,1))
            visited.add(i+1)
            output[i] = 1
    
    while q:
        ind, semi= q.popleft() 

        for node in graph[ind]:
            indgree[node-1] -= 1
            if indgree[node-1] == 0:
                output[node-1] = semi + 1 
                visited.add(node)
                q.append((node,semi+1))
    # print(output)
    # print(q)            
    if len(visited) < n:
        return -1

    return max(output)                  



    
