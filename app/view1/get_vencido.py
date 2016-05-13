#import conf
import json
from py2neo import Graph
import requests
import socketserver
import http.server
import http
from http.server import BaseHTTPRequestHandler, HTTPServer
graph = Graph("http://neo4j:1234@localhost:7474/db/data/")

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

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		#print(self.path[-1:])
		r=get_vencido(self.path[-1:])
		print(r)
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.wfile.write(r.encode())

httpd = socketserver.TCPServer(("localhost", 8086), MyHandler)
httpd.serve_forever()