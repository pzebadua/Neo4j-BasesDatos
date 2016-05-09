import json

from bottle import get, run, request, response, static_file
from py2neo import Graph


graph = Graph("http://neo4j:1234@localhost:7474/db/data/") #http://NEOUSR:PASS@localhost:PUERTO/db/data

"""
def get_graph():
	results = graph.cypher.execute("match (H:Herraminetas)-[r3:Usa]-(R:Receta)-[r1:NECESITA]-(P:Product)-[r2:ESTA]-(F:Fechas) where r2.estado=\"vencido\"  return *")
	#print(results[0])
	rec=[]
	props=[]
	modishnes=0
	allahuakbar=0
	for tutzke in results:
		for kuz in results[modishnes]:
			#print(kuz.properties)
			props.append(kuz.properties)
		rec.append(props)
		modishnes+=1
	print(json.dumps(rec,indent=4))
	#return json.dumps(rec)
"""
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

def get_ings(x): #parametro es el ID de la receta
	x=str(x)
	results=graph.cypher.execute("match (R:Receta)-[:NECESITA]-(I:Product)where R.id="+x+" return I")
	#print(results)
	ingredientes=[]
	for i in results:
		ingredientes.append(i[0].properties)
	#print(json.dumps(ingredientes))
	return json.dumps(ingredientes)

def get_herr(x): #parametro es el ID de la receta
	x=str(x)
	results=graph.cypher.execute("match (R:Receta)-[:Usa]-(I:Herraminetas)where R.id="+x+" return I")
	#print(results)
	ingredientes=[]
	for i in results:
		ingredientes.append(i[0].properties)
	#print(json.dumps(ingredientes))
	return json.dumps(ingredientes)

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

def get_vendido(x):
	x=str(x)
	results=graph.cypher.execute("match (P:Product)-[r:ESTA]-(F:Fechas) where r.estado=\"vendido\" and P.id="+x+"  return F")
	#print(results)
	sold=[]
	for v in results:
		#print(v[0].properties)
		sold.append(v[0].properties)
	#print(json.dumps(sold))
	return json.dumps(sold)


"""
print(
get_recetas(),"\n",
get_ings(1), '\n',
get_herr(1),"\n",
get_vencido(1),"\n",
get_vendido(1)
)
"""
get_graph()
