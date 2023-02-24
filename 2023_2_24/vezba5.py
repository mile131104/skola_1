import http.server as srv
import urllib.parse as parse

podaci = {"python":[
    "python web", "python fundamentals", "python database"
],"java":[
    "java_core", "java advanced", "java web"
]}

class Handler(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        upit = self.path.split("?")[1]
        parametri = dict(parse.parse_qsl(upit[1]))
        smer = parametri["smer"]

        odgovori = ""
        for predmet in podaci[smer]:
            odgovori += f"{predmet}"

        self.wfile.write(f"HTPP/1.1 200 Ok\r\n\r\n{odgovori}".encode())

srv.HTTPServer(("0.0.0.0", 8000),Handler).serve_forever()
