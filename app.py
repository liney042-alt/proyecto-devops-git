from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HOST = "0.0.0.0"
PORT = 8080
DATA_DIR = Path("/data")
SECRET_FILE = Path("/run/secrets/banner_msg")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Endpoint para el Healthcheck de Docker
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
            return
        
        # 2. Filtro para omitir el Favicon y evitar que cuente doble por recarga
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        
        # 3. Lógica del contador de visitas persistente (Aumenta de 1 en 1)
        visits = "sin contador"
        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            visits_file = DATA_DIR / "visits.txt"
            count = int(visits_file.read_text().strip()) if visits_file.exists() else 0
            count += 1
            visits_file.write_text(str(count))
            visits = str(count)
        except Exception:
            pass
            
        # 4. Lógica para leer el secreto de Docker
        secret_msg = ""
        if SECRET_FILE.exists():
            secret_msg = SECRET_FILE.read_text(encoding="utf-8").strip()
            
        # 5. Interfaz HTML que se muestra en el navegador
        html = f"""
        <html>
        <head><title>Portal EcoVerde</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px; background-color: #f4f9f4;">
            <h1 style="color: #2e7d32;">Portal EcoVerde Antioquia</h1>
            <p>Servicio web listo para Docker en producción y con seguridad aplicada.</p>
            <hr>
            <h3>Métricas de Operación:</h3>
            <p><strong>Visitas registradas (en volumen):</strong> {visits}</p>
            <p><strong>Mensaje secreto inyectado:</strong> <span style="color: #c62828;">{secret_msg or "no definido"}</span></p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    print(f"Servidor web de producción corriendo en http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()