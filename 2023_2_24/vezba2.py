import http.server as srv
import datetime

class Handler(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        "/index.html?tralala"
        delovi_putanje = self.path.split("?")
        fajl = delovi_putanje[0].lstrip("/")
        upit = delovi_putanje[1]
        sadrzaj_fajla = open(fajl,"r").read()
        sadrzaj_fajla = sadrzaj_fajla.replace("[BOJA]",upit)
        self.wfile.write(f"HTTP/1.1 200 Ok\r\n\r\n{sadrzaj_fajla}".encode())
        # ime = "dovla"
        # ime_unazad = ime[::-1]
        # self.wfile.write(f"HTTP/1.1 200 Ok\r\n\r\n{ime_unazad}".encode())

server = srv.HTTPServer(("0.0.0.0",8000),Handler)

server.serve_forever()
