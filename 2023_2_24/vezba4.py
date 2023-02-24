import http.server as srv
import urllib.parse as parse

class Handler(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        upit = self.path.split("?")[1]
        parametri = dict(parse.parse_qsl(upit))
        a = int(parametri["a"])
        b = int(parametri["b"])
        rezultat = a + b
        self.wfile.write(f"HTPP/1.1 200 Ok\r\n\r\n{rezultat}".encode())

srv.HTTPServer(("0.0.0.0", 8000),Handler).serve_forever()