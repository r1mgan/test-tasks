from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.do_GET()
    def do_GET(self):
        if self.path == "/healthcheck":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("X-Custom-Header", "healthcheck")
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("X-Custom-Header", "Check")
            self.end_headers()
            value = self.headers.get('X-Forwarded-For', 'Empty')
            self.wfile.write(f'X-Forwarded-For: {value}\r\n'.encode())

SERVER_PORT = 80
httpd = HTTPServer(('0.0.0.0', SERVER_PORT), SimpleHTTPRequestHandler)
print('Listening on port %s ...' % SERVER_PORT)
httpd.serve_forever()
