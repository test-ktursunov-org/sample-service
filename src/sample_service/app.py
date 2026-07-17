from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from sample_service import routes
from sample_service.config import Settings


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self._json(*routes.health())
            return
        if self.path == "/items":
            self._json(*routes.list_items())
            return
        self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/items":
            self._json(404, {"error": "not found"})
            return
        length = int(self.headers.get("content-length", 0))
        payload = json.loads(self.rfile.read(length) or b"{}")
        self._json(*routes.create_item(payload))

    def _json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


def serve(settings: Settings | None = None) -> None:
    settings = settings or Settings.from_env()
    HTTPServer((settings.host, settings.port), Handler).serve_forever()
