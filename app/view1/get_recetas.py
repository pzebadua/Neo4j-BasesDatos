import conf

def get_recetas():
	results = graph.cypher.execute("MATCH (n:Receta) RETURN n")
	nodes = []
	#print(results[0][0].properties)
	#print(json.dumps(results[0][0].properties))
	for r in results:
		#print(r[0].properties)
		nodes.append(r[0].properties)
	#print(nodes)
	#print( json.dumps(nodes))
	return json.dumps(nodes)