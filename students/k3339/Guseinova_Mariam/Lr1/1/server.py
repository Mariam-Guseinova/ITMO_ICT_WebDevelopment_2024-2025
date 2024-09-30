import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)

print('Сервер запущен')

while True:
    # Ожидание данных от клиента
    data, client_address = server_socket.recvfrom(1024)
    print(f'Получено сообщение клиента: "{data.decode()}"')

    # Отправка ответа
    response = 'Hello, client'
    server_socket.sendto(response.encode(), client_address)
    print(f'Ответ "{response}" отправлен клиенту')