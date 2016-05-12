import conf

def get_graph():
	results = graph.cypher.execute("match (H:Herraminetas)-[r3:Usa]-(R:Receta)-[r1:NECESITA]-(P:Product)-[r2:ESTA]-(F:Fechas) where r2.estado=\"vencido\"  return *")
	#print(results)
	rec=[]
	props=[]
	modishnes=0
	allahuakbar=0
	
	for kuz in results[modishnes]:
		#print(kuz.properties)
		props.append(kuz.properties)
		modishnes+=1
		
	print(props)
	#print(json.dumps(props,indent=4))
	return json.dumps(props)