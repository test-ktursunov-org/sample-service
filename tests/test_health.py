import json
import threading
import urllib.request
from http.server import HTTPServer

from sample_service.app import Handler


def _running_server():
    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def test_health_reports_ok():
    server = _running_server()
    url = f"http://127.0.0.1:{server.server_port}/health"

    with urllib.request.urlopen(url) as response:
        assert response.status == 200
        assert json.load(response) == {"status": "ok"}

    server.shutdown()
