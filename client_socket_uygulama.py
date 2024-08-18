# -*- coding: utf-8 -*-
"""
 TCP CLIENT SOCKET
"""

import socket

# Soketi oluşturuyoruz...
client_socket = socket.socket()

# server sokete bağlantı sağlıyoruz...
client_socket.connect(("127.0.0.1", 50000))

mesaj = "Client-111 sistemden selamlar..."
cikis_mesaji  = "exit"
# Server sisteme mesaj gönderiyoruz..
client_socket.send(bytes(cikis_mesaji, 'utf-8'))

client_socket.close()


