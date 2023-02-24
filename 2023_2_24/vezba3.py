import http.server as srv

class Handler(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        parametri = dict((p.split("=")[0],p.split("=")[1]) for p in self.path.split("?")[1].split(("&")))
        ime = parametri["ime"]
        imerev = ime[::-1]
        self.wfile.write(f"HTTP/1.1 200 Ok\r\n\r\n{imerev}".encode())
        

srv.HTTPServer(("0.0.0.0",8000),Handler).serve_forever()
