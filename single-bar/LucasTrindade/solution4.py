import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(5000) #Default = 1000 | RecursionError: maximum recursion depth exceeded in comparison

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
    #print(graph)
        
    memory = {} #dp step1
    def dfs_custom(root:int, target:int, price:int=0)->int:
        nonlocal memory
        if root == target:
            return price
        elif root in memory.keys(): #dp step2
            return memory[root]
        elif len(graph[root]) > 0:
            max_vertice_price = 0
            for edge in graph[root]:#O(e)
                if edge == target:
                    new_price = graph[root][edge]
                elif edge in memory.keys():
                    new_price = memory[edge]
                else:
                    new_price = dfs_custom(root=edge, target=target, price=graph[root][edge])
                max_vertice_price = max(max_vertice_price, new_price)
            memory[root] = max_vertice_price #dp step3
            return price + max_vertice_price     
    
    root = 0
    if bar_size <= 1000:    
        dfs_custom(root, bar_size) #O(v+e) => e = v! => O(v!)
    else:
        end_pointer = bar_size
        while True:
            start_pointer = max((end_pointer-1000), 0)
            dfs_custom(start_pointer, bar_size) #O(v+e) => e = v! => O(v!)
            if start_pointer == 0:
                break
            else:
                end_pointer = start_pointer
    return memory[root]  