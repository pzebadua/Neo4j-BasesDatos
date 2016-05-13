#import conf
import json
from py2neo import Graph
import requests
import socketserver
import http.server
import http
from http.server import BaseHTTPRequestHandler, HTTPServer
graph = Graph("http://neo4j:1234@localhost:7474/db/data/")

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

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		#print(self.path[-1:])
		r=get_vendido(self.path[-1:])
		print(r)
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.wfile.write(r.encode())

httpd = socketserver.TCPServer(("localhost", 8084), MyHandler)
httpd.serve_forever()