import BaseHTTPServer
import CGIHTTPServer

port = 8000

httpd = BaseHTTPServer.HTTPServer(('', port), CGIHTTPServer.CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

