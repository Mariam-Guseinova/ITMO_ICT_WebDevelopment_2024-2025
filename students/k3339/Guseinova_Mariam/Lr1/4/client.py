import socket
import threading

# Настройка TCP-клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9090)
client_socket.connect(server_address)


# Функция для получения сообщений от сервера
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == 'USERNAME':
                client_socket.send(username.encode())
            else:
                print(message)
        except:
            print('Ошибка при подключении к серверу.')
            client_socket.close()
            break


# Функция для отправки сообщений серверу
def send_messages():
    while True:
        message = f'{username}: {input("")}'
        client_socket.send(message.encode())


username = input('Введите ваше имя: ')

# Запуск потоков для отправки и получения сообщений
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
