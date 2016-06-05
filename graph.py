""" In this file a graph is a dictionary with {node-name: edge-set} where edge is (destination, length) """

def shortest_path(graph, begin, end, infinity = 1000000000) :
	""" Uses Dijkstra's shortest path algorithm.
		begin is a set of starting nodes.
		end is a set of ending nodes.
		infinity should be larger than any possible path length in graph. """
	
	d = {}
	v = set()

	for x in graph.keys() : d[x] = infinity
	for b in begin : d[b] = 0
	cn = b
	
	while not cn in end and d[cn] != infinity :
		for (n, l) in graph[cn] :
			if d[cn] + l < d[n] :
				d[n] = d[cn] + l
		v.add(cn)
		cn = min([(x, y) for (x, y) in d.items() if not x in v], key = lambda x: x[1])[0]
	
	return d[cn]