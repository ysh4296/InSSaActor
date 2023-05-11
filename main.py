import requests
from api import getMovieList,getGraph

actorList = getMovieList()
print(actorList)
graph = getGraph(actorList)
print(graph)

max_actor_conn = 0
max_actor_node = ''

for key,value in graph.items():
    conn_sum = sum([len(graph[conn]) for conn in value])
    if key[:2] == "배우": #배우 노드
        if conn_sum > max_actor_conn:
            max_actor_conn = conn_sum
            max_actor_node = key

print("The actor with the maximum connections: ", max_actor_node)