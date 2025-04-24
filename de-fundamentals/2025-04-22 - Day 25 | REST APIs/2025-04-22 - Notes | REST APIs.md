# 2025-04-22 - Notes
## REST API
- Representational State Transfer
- Stateless (no data held in memory, no varriables holding data)
- anything we store must persist outside the server (tipically in a database)
- combination of METHOD + url endpoint to interpret request
- GET /api/doughnuts - gives back doughnuts from a database

## Servers
The term can be applied for physical servers but can also be used to describe certain programs that receive requests and return responses
###
```python
from http.server import BaseHTTPRequestHandler, HTTPServer

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
run()
```
## Parametric endpoints
Endpoints where there is user input that we need to take into account
