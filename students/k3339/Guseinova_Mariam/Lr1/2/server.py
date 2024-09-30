import socket


def calculate_trapezoid_area(a, b, h):
    # Формула площади трапеции (вариант 11)
    return (a + b) * h / 2


# Настройка TCP-сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
server_socket.bind(server_address)
server_socket.listen(1)  # Ожидание подключения клиента

print('Сервер запущен')

while True:
    connection, client_address = server_socket.accept()
    try:
        print(f'Подключен клиент: {client_address}')

        # Получение данных от клиента
        data = connection.recv(1024).decode()
        if data:
            a, b, h = map(float, data.split())
            print(f'Получены параметры трапеции: a = {a}, b = {b}, h = {h}')

            area = calculate_trapezoid_area(a, b, h)

            response = f'Площадь трапеции равна: {area:.2f}'
            connection.sendall(response.encode())
            print(f'Ответ отправлен: {response}')
    finally:
        connection.close()
