import socket

# Наша HTML страничка
HTML_FILE = 'index.html'

# Настройка TCP-сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)
server_socket.listen(1)  # Ожидание одного клиента

print(f'Сервер запущен')

while True:
    connection, client_address = server_socket.accept()
    try:
        print(f'Подключен клиент: {client_address}')

        request = connection.recv(1024).decode()
        print(f'Запрос клиента:\n{request}')

        # Чтение HTML-файла
        try:
            with open(HTML_FILE, 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Формирование HTTP-ответа
            response = (
                (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        f"Content-Length: {len(html_content)}\r\n"
                        "\r\n"
                        + html_content
                )
            )

        except FileNotFoundError:
            # Если файл не найден отправляем 404 ошикбу
            response = (
                'HTTP/1.1 404 Not Found\r\n\r\n'
                '<h1>404 Not Found</h1>'
            )

        connection.sendall(response.encode())

    finally:
        connection.close()