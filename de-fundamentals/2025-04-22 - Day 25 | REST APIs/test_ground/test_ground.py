from http.server import BaseHTTPRequestHandler, HTTPServer


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            print("handling GET")
            # The order matters
            self.send_response(200)  # Set status code
            self.headers.add_header("Content-Type", "text/html")  # add any headers
            self.end_headers()  # add the blank line
            self.wfile.write(
                "<H1>Hello World!</H1>".encode("utf-8")
            )  # add body with a byte string (has to be encoded)

    def do_POST(self):
        pass


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run(handler_class=MyRequestHandler)
#
