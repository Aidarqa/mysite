from http.server import BaseHTTPRequestHandler, HTTPServer

import os



class Handler(BaseHTTPRequestHandler):

    def do_POST(self):

        if self.path == '/deploy':

            os.system('cd /home/devops/mysite && git pull && ./deploy.sh')

            self.send_response(200)

            self.end_headers()

            self.wfile.write(b'Deployed')

        else:

            self.send_response(404)

            self.end_headers()



server = HTTPServer(('0.0.0.0', 5000), Handler)

print("Webhook server started on port 5000...")

server.serve_forever()
