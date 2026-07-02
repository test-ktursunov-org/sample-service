from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(404)
        self.end_headers()

    def log_message(self, fmt, *args):
        pass


def serve(host: str = "127.0.0.1", port: int = 8080) -> None:
    HTTPServer((host, port), Handler).serve_forever()
