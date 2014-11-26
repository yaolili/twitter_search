import random
import copy 
import time

segma = 0.5

def create_graph(graph,document_number,score):
	for i in range(0, document_number):
		for j  in range(i+1, document_number):
			#score[(i,j)] = random.random()
	       		if (score[(i,j)] > segma):
				if i in graph : 
					graph[i].append(j)
					if j in graph :	graph[j].append(i)
					else: graph[j] = [i]
				
				else:
					graph[i] = [j]
					if j in graph : graph[j].append(i)
					else: graph[j] = [i]
	# create the vertex without any edge
	for i in range(0, document_number):
		if (i not in graph): graph[i] = []
	return graph

def max_degree(graph):	
	max_degree_id = -1
	max_degree_number = 0
	#to find the last id with max degree
	for i in graph:
		if(len(graph[i]) >= max_degree_number):
			max_degree_number = len(graph[i])
			max_degree_id = i

	return max_degree_id

"""
Clustering the max degree doucument which's id is document_id
This function will change graph and clustering_array
"""
def clustering(graph, document_id, clustering_array):
	graph[document_id].append(document_id)
	want_clustered_list = copy.deepcopy (graph[document_id])
	#print graph[document_id]
	#print document_id
	for i in graph:
		for j in graph[document_id]:
			if ( ( j in graph[i]) and (i != document_id )):
				#print  i ,j 
				graph[i].remove(j)
				#print graph 
        # to make the first element is star center
        graph[document_id].reverse()
        clustering_array.append(graph[document_id])
	for i in want_clustered_list: del graph[i]
	return 1 

def is_all_marked(clustering_array, graph_length):
	marked_number = 0
	for i in range(0, len(clustering_array)):
		marked_number += len(clustering_array[i])
	#print marked_number
	if (marked_number == graph_length): return True
	else: return False

def star_clustering_result(document_number,score):
	graph = dict ()
	clustering_result = list()
	create_graph(graph,document_number,score)
	original_graph = copy.deepcopy(graph)
	#print 'create original graph'
	#print graph
  	
	while (not is_all_marked(clustering_result, len(original_graph))):
		Id = max_degree(graph)
		clustering(graph,Id,clustering_result)
		#print '----after clustering-----'
		#print 'clustering_result'
		#print clustering_result
		#print 'clustered_graph'
		#print graph
	return clustering_result

"""
number = 1000
score = dict()
for i in range(0, number):
	for j in range(i+1, number):
		score[(i,j)] = random.random()
result = star_clustering_result(number,score)
print "star_clustering_result"
print result
print time.clock()
"""

