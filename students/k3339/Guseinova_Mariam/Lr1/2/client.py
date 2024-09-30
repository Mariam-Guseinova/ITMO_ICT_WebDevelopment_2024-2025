import socket

# Настройка TCP-клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)

client_socket.connect(server_address)

print("Для расчета площади трапеции введите несколько параметров:")

try:
    a = input('Длина первого основания (a): ')
    b = input('Длина второго основания (b): ')
    h = input('Высота (h): ')

    # Отправление данных на сервер
    message = f'{a} {b} {h}'
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024).decode()
    print(f'Ответ сервера: {data}')

finally:
    client_socket.close()
