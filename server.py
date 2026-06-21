import http.server
import socketserver
import webbrowser


PORT = 8001


def start_server():
    """
    Start a local web server to display the generated index.html file.
    """
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Healthcare Technology Watch CMS website is running!")
        print(f"Open this link in your browser: http://localhost:{PORT}/index.html")

        webbrowser.open(f"http://localhost:{PORT}/index.html")

        httpd.serve_forever()


if __name__ == "__main__":
    start_server()