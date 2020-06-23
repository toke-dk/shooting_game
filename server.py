from _thread import *
import socket
from player import Player
import pickle

screen_width = 1600
screen_height = 1200
# skole: MKS
#server = '10.120.0.238'
# freenet
server = '192.168.1.185'
port = 5050


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))
    raise e

s.listen(2)
print('Waiting for connection, Server started')
players = [Player(0, 0, 100, 100, 'space-invaders.png', 180), Player(0, screen_height - 100, 100, 100, 'space-invaders.png', 0)]


def thread_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print('Recieved', data)
                print('Sending', data)
                conn.sendall(pickle.dumps(reply))
        except:
            break
    print('Lost connection')
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print('Connection to:', addr)
    start_new_thread(thread_client, (conn, current_player))
    current_player += 1
