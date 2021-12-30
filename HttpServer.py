import http.server
import signal
import socketserver
import multiprocessing

DIRECTORY = "./root/"


def httpServer(port, directory=DIRECTORY):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def log_message(self, format, *args) -> None:
            return None

    with socketserver.TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    server = multiprocessing.Process(target=httpServer, args=(8888,))
    server.start()
    print("Running")
