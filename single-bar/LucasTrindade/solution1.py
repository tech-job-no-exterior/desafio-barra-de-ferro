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
            
    max_price = 0
    
    def dfs_custom(root:int, target:int, price:int=0)->None:
        nonlocal max_price
        if root == target:
            max_price = max(max_price, price) #also could be a maxheap
        elif len(graph[root]) > 0:
            for edge in graph[root]:#O(e)
                new_price = price + graph[root][edge]
                dfs_custom(root=edge, target=target, price=new_price)
        return       

    dfs_custom(0, bar_size)#O(v+e) => e = v! => O(v!)
    return max_price