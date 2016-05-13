#import conf
import json
from py2neo import Graph
import requests
import socketserver
import http.server
import http
from http.server import BaseHTTPRequestHandler, HTTPServer
#from BaseHTTPServer import BaseHTTPRequestHandler 

graph = Graph("http://neo4j:1234@localhost:7474/db/data/")

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


class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		r=get_recetas()
		print(r)
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		self.wfile.write(r.encode())

httpd = socketserver.TCPServer(("localhost", 8083), MyHandler)
httpd.serve_forever()
"""
get_recetas()
"""