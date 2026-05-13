from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.request import Request, urlopen
import json


ROOT = Path(__file__).resolve().parent
SHEET_CSV_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1i8lRUlj0sW1D-QP5k2vTD-din8PFX-b5jCk6ZL0lG2U/"
    "export?format=csv&gid=0"
)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.startswith("/api/sheet"):
            self.send_sheet()
            return
        super().do_GET()

    def send_sheet(self):
        try:
            request = Request(
                SHEET_CSV_URL,
                headers={"User-Agent": "Codex Sheet Monitor"},
            )
            with urlopen(request, timeout=20) as response:
                body = response.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
        except Exception as exc:
            body = json.dumps({"error": str(exc)}, ensure_ascii=False).encode("utf-8")
            self.send_response(502)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    print("Sheet monitor: http://127.0.0.1:8765", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
