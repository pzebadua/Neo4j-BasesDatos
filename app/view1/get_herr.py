import conf

def get_herr(x): #parametro es el ID de la receta
	x=str(x)
	results=graph.cypher.execute("match (R:Receta)-[:Usa]-(I:Herraminetas)where R.id="+x+" return I")
	#print(results)
	ingredientes=[]
	for i in results:
		ingredientes.append(i[0].properties)
	#print(json.dumps(ingredientes))
	return json.dumps(ingredientes)