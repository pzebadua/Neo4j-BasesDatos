import conf

def get_vencido(x): #parametro es el ID del ingrediente 
	x=str(x)
	results=graph.cypher.execute("match (P:Product)-[r:ESTA]-(F:Fechas) where r.estado=\"vencido\" and P.id="+x+"  return F")
	#print(results)
	vence=[]
	for v in results:
		#print(v[0].properties)
		vence.append(v[0].properties)
	#print(json.dumps(vence))
	return json.dumps(vence)