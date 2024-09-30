import socket
import threading

# Настройка TCP-сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9090)
server_socket.bind(server_address)
server_socket.listen()

clients = []  # Хранение всех клиентов
usernames = []  # Хранение имен


# Широковещательная рассылка сообщения всем клиентам
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass


# Обработка сообщений от клиентов
def handle_client(client):
    while True:
        try:
            # Получаем сообщение от клиента
            message = client.recv(1024)
            if message:
                broadcast(message)  # Пересылаем сообщение всем клиентам
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                username = usernames[index]
                broadcast(f'{username} покинул чат!'.encode())
                usernames.remove(username)
                break


# Функция для принятия новых подключений
def receive_connections():
    print("Сервер запущен и ожидает подключения пользователей")
    while True:
        client, address = server_socket.accept()
        print(f'Новое подключение: {address}')

        # Получаем и сохраняем имя пользователя
        client.send('USERNAME'.encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)

        print(f'Имя пользователя: {username}')
        # Сообщаем о новом пользователе
        client.send('Вы подключены к чату!\n'.encode())
        broadcast(f'{username} присоединился к чату!'.encode())

        # Запускаем поток для обработки сообщений от клиента
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive_connections()
