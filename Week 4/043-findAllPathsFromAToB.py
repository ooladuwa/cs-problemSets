def csFindAllPathsFromAToB(graph):
    output = []
    path = [0]
    final_index = len(graph) - 1

    def dft(path):
        current_node = path[-1]
        if current_node == final_index:
            output.append(path)
            return
        for neighbor in graph[current_node]:
            dft(path + [neighbor])
            
    dft(path)
    return sorted(output)
    
    
    
  
    # final_node = len(graph) - 1
    # output = []   
    # stack = [[0]]
    
    # while len(stack) > 0:
    #     path = stack.pop()
        
    #     current_node == path[-1]
        
    #     if current_node == final_node:
    #         output.append(path)
    #         continue
            
    #     for neighbor in graph[current_node]:
    #         stack.append(path + [neighbor])
            
    # return sorted(output)


"""
You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1.

graph[a] is a list of all nodes b for which the edge a -> b exists.

Example:
Graph illustration

Input: graph = [[1, 2],[3],[3],[4],[]]
Output: [[0,1,3,4], [0,2,3,4]]
Note: The results must be returned in sorted order. You can use any built-in sort method on the results array at the end of your function before returning.

[execution time limit] 4 seconds (py3)

[input] array.array.integer graph

[output] array.array.integer
"""