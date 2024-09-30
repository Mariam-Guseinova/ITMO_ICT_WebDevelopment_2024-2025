from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999

grade_list = []


class GradeHandler(BaseHTTPRequestHandler):
    def send_html_response(self, html_content):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

    def do_GET(self):
        html = self.generate_html_page()
        self.send_html_response(html)

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8')
        data = parse_qs(post_body)

        discipline = data.get('subject', [''])[0]
        grade = data.get('score', [''])[0]

        if discipline and grade:
            self.record_grade(discipline, grade)

        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def record_grade(self, discipline, grade):
        entry = next((rec for rec in grade_list if rec['subject'] == discipline), None)
        if entry:
            entry['score'] += f", {grade}"
        else:
            grade_list.append({'subject': discipline, 'score': grade})

    def generate_html_page(self):
        page = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Grade Tracker</title>
</head>
<body>
    <h1>Grades List</h1>
    <table border="1">
        <tr><th>Subject</th><th>Grades</th></tr>"""

        for rec in grade_list:
            page += f"<tr><td>{rec['subject']}</td><td>{rec['score']}</td></tr>"

        page += """
    </table>
    <h2>Add a Grade</h2>
    <form method="POST" action="/">
        <label for="subject">Subject:</label><br>
        <input type="text" id="subject" name="subject" required><br>
        <label for="score">Grade:</label><br>
        <input type="text" id="score" name="score" required><br><br>
        <input type="submit" value="Add">
    </form>
</body>
</html>"""
        return page


def start_server():
    address = (SERVER_HOST, SERVER_PORT)
    http_server = HTTPServer(address, GradeHandler)
    print(f"Server running at http://{SERVER_HOST}:{SERVER_PORT}")
    http_server.serve_forever()


if __name__ == '__main__':
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShutting down server.")
