import socket
import sys
import _thread
from view import *
from player import *
import time

palavra = ["rola"]

host = "localhost"
port = 20014
# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket criada")

# Connect sockets
try:
    server_socket.bind((host, port))
except socket.error:
    print("Falha na vinculação de endereço", (host, port))
    sys.exit()

print("Socket vinculada ao endereço", (host, port))

server_socket.listen(4)

players = []
hangman = True
errors = 0
prints = [zero(), one(), two(), lambda: three, lambda: four, lambda: five, lambda: six]

def game(palavra_escolhida):
    copy = palavra_escolhida
    while True:
        if len(players) >= 3:
            break
    while hangman:
        for p in players:
            # print("Enviando autorizacao")
            p[0].sendto(b"true", p[1])

            time.sleep(0.5)
            # current_hangman_print = prints[errors]
            # print(current_hangman_print)
            # print("Enviando forca")
            p[0].sendto(prints[errors], p[1])
            time.sleep(0.5)
            # print("Esperando resposta de ", p[2])
            data = p[0].recv(4096).decode()
            # print("Resposta recebida de ", p[2])
            print(data)
            if data == palavra_escolhida:
                print("ACERTO TUDO")
            elif len(data) == 1 and data in copy:
                copy = copy.replace(data, "")
                print("ACERTO")
                print(copy)
            else:
                print("ERRO")



def clientthread(conn, player_address):
    name = conn.recv(4096).decode()
    players.append((conn, player_address, name))
    print("Jogador", player_address, "nomeou-se como " + name)

    if len(players) >= 3:
        conn.sendto(("\nBem vindo ao jogo da forca, " + name +
                      "\nA sala está cheia, vamos começar!\n").encode(), player_address)
    else:
        conn.sendto(("\nBem vindo ao jogo da forca, " + name +
                     "\nAtualmente temos " + str(len(players)) + " jogadores na sessão, é preciso 3 jogadores para iniciar\n").encode(), player_address)


_thread.start_new_thread(game, (palavra[0],))

while True:
    connection, address = server_socket.accept()
    print("Nova conexão recebida de", address)
    _thread.start_new_thread(clientthread, (connection, address))
