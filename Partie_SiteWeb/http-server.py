import http.server

port = 80
addresse = ("", port)

server = http.server.HTTPServer

gestionnaire = http.server.CGIHTTPRequestHandler
gestionnaire.cgi_directories = ["/"]

httpd = server(addresse, gestionnaire)

httpd.serve_forever()