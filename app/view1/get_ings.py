#import conf
import json
from py2neo import Graph
import requests
import socketserver
import http.server
import http
from http.server import BaseHTTPRequestHandler, HTTPServer
graph = Graph("http://neo4j:1234@localhost:7474/db/data/")

def get_ings(x): #parametro es el ID de la receta
	x=str(x)
	results=graph.cypher.execute("match (R:Receta)-[:NECESITA]-(I:Product)where R.id="+x+" return I")
	#print(results)
	ingredientes=[]
	for i in results:
		ingredientes.append(i[0].properties)
	#print(json.dumps(ingredientes))
	return json.dumps(ingredientes)

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		#print(self.path[-1:])
		r=get_ings(self.path[-1:])
		print(r)
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.wfile.write(r.encode())

httpd = socketserver.TCPServer(("localhost", 8085), MyHandler)
httpd.serve_forever()