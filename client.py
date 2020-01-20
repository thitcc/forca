import socket
import time

address = ('localhost', 20001)
name = ""

# Create sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

while not name:
    print("Digite seu nome para outros jogadores o reconhecerem: ")
    name = input()
    if name:
        client_socket.send(name.encode())
        print(client_socket.recv(4096).decode())

# Echo
while True:
    your_turn = client_socket.recv(4096)
    time.sleep(0.5)
    if your_turn == b"true":
        print(client_socket.recv(4096).decode())    # Mostra a forca
        print("Digite a letra ou tente adivinhar a palavra\nDigite sair para desconectar\n> ", end="")
        answer = input()
        client_socket.send(bytes(answer, "utf-8"))  # Envia a resposta
    elif your_turn == b"Vic":
        print("O jogo acabou, você venceu!")
        client_socket.close()
    elif your_turn == b"End":
        print("O jogo acabou, você perdeu")
        client_socket.close()
    else:
        print(client_socket.recv(4096).decode())
        print(client_socket.recv(4096).decode())
        print("Espere seu turno\n")
