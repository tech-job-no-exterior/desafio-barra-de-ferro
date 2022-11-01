import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(3000) #Default = 1000 | RecursionError: maximum recursion depth exceeded in comparison

def max_price(bar_size:int, price_map:list)->int|bool:
    if (bar_size < 1
        or len(price_map) < 1
        or bar_size != len(price_map)
    ):
        return False
    
    graph = {}
    graph[0] = {}
    for vertice in range(1, bar_size+1): #O(v+e)
        graph[0][vertice] = price_map[vertice-1]
        graph[vertice] = {}
        index = 0
        for edge in range(vertice+1, bar_size+1):
            graph[vertice][edge] = price_map[index]
            index += 1   
        
    memory = {}
    def dfs_custom(root:int, target:int, price:int=0)->int:
        nonlocal memory
        if root == target:
            return price
        elif root in memory.keys():
            return memory[root]
        elif len(graph[root]) > 0:
            max_vertice_price = 0
            for edge in graph[root]:#O(e)
                new_price = price + graph[root][edge]
                max_vertice_price = max(max_vertice_price
                                        , dfs_custom(root=edge, target=target, price=graph[root][edge])
                                    )
            memory[root] = max_vertice_price #kadane
            return price + max_vertice_price     

    root = 0
    dfs_custom(root, bar_size) #O(v+e) => e = v! => O(v!)
    return memory[root]  