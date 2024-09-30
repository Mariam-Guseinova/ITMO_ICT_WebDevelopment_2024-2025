import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)

# Отправка сообщения серверу
message = 'Hello, server'
client_socket.sendto(message.encode(), server_address)
print(f'Сообщение "{message}" отправлено серверу')

data, _ = client_socket.recvfrom(1024)
print(f'Ответ сервера: "{data.decode()}"')

client_socket.close()