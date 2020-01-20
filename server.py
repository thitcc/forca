import socket
import sys
import _thread
import time
import random
from view import *

host = "localhost"
port = 20001

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

players = []    # Lista de jogadores
prints = [zero(), one(), two(), three(), four(), five(), six()] # Arrays com prints dos estados da forca
pool = ["batata"] #, "caminhar", "mesa", "limao", "cascalho", "perna", "brazil", "goiaba"]   # Lista de palavras

def game(chosen_word):
    global players
    errors = 0
    hangman = True
    copy = chosen_word
    while True:
        if len(players) >= 3:
            break
    while hangman:
        for p in players:
            p[0].sendto(b"true", p[1])
            print("Agora é o turno do jogador: ", p[2])
            time.sleep(0.5)
            p[0].sendall(prints[errors])
            print("Enviando a forca para o jogador ", p[2])
            time.sleep(0.5)
            data = p[0].recv(4096).decode()
            print("Resposta recebida de ", p[2], ": ", data)
            if data == chosen_word:
                print(p[2], " acertou a palavra")
                for i in players:
                    i[0].sendto(prints[errors], i[1])
                    i[0].sendto(bytes("\n\nO jogo acabou, o jogador" + i[2] + "acertou a palavra!: " + chosen_word, "utf-8"), i[1])
                    i[0].close()
                    print(len(players))
                    hangman = False
                break
            elif len(data) == 1 and data in copy:
                copy = copy.replace(data, "")
                if not copy:
                    print("Ninguém acertou a palavra: ", chosen_word)
                    for i in players:
                        i[0].sendto(prints[errors], i[1])
                        i[0].sendto(bytes("\n\nO jogo acabou, ninguém acertou a palavra: " + chosen_word, "utf-8"), i[1])
                        i[0].close()
                        hangman = False
                    break
                print(p[2], " acertou uma letra")
            else:
                errors += 1
                if errors >= 6:
                    for i in players:
                        i[0].sendto(prints[errors], i[1])
                        i[0].sendto(bytes("\n\nO jogo acabou, número máximo de erros excedido", "utf-8"), i[1])
                        i[0].close()
                        hangman = False
                    break
                print(p[2], " errou")

        players = []
        print("Jogo acabou, iniciando outro")
        _thread.start_new_thread(game, (random.choice(pool),))

def client_thread(conn, player_address):
    name = conn.recv(4096).decode()
    players.append((conn, player_address, name))
    print("Jogador", player_address, "nomeou-se como " + name)

    if len(players) >= 3:
        conn.sendto(("\nBem vindo ao jogo da forca, " + name +
                      "\nA sala está cheia, vamos começar!\n").encode(), player_address)
    else:
        conn.sendto(("\nBem vindo ao jogo da forca, " + name +
                     "\nAtualmente temos " + str(len(players)) + " jogadores na sessão, é preciso 3 jogadores para iniciar\n").encode(), player_address)

_thread.start_new_thread(game, (random.choice(pool),))

while True:
    if len(players) < 2:
        connection, address = server_socket.accept()
        print("Nova conexão recebida de", address)
        _thread.start_new_thread(client_thread, (connection, address))
