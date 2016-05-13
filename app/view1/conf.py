import json
import urllib.request
import requests
import socketserver
import http.server


from bottle import get, run, request, response, static_file
from py2neo import Graph


graph = Graph("http://neo4j:1234@localhost:7474/db/data/") #http://NEOUSR:PASS@localhost:PUERTO/db/data