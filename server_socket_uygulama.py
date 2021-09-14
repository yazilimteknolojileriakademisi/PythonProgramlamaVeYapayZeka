# -*- coding: utf-8 -*-
"""
 TCP SERVER SOCKET
"""

import socket

# Socket oluşturma
server_socket = socket.socket()


""""
Ports 0-1024 are forbidden for programs..
Ports 1024-49151- Registered Port -These can be registered for services with the IANA and should be 
treated as semi-reserved. User written programs should not use these ports.
Ports 49152-65535– These are used by client programs and you are free to use these in client programs.
"""
server_socket.bind(("127.0.0.1", 50000))


# Socketimiz dinlemeye başlıyor..
server_socket.listen(5)
print("Soket oluşturuldu bağlantı bekleniyor...")

while True:
    client_socket, adres = server_socket.accept()
    print(adres, " isimli bilgisayar ile bağlantı kuruldu..")    

    # Client sistemden gelen mesajı ekrana yazıyoruz..
    gelen_mesaj = client_socket.recv(1024).decode()
    print(gelen_mesaj)

    client_socket.close()
    
    # While döngüsünde programımızın takılıp kalmaması için client'den 'exit' mesajı geldiğinde
    # while döngüsünden çıkıyoruz ve server artık 50000. porttan dinlemeyi bitiyiryor, program sonlanıyor..
    # Burası önemli çünkü bu kısmı yapmazsak 50000.port bind edilmiş bir şekilde kalır ve hata alırız..
    if (gelen_mesaj == 'exit'):
        break
    
print("Hoşçakalın..")
server_socket.close()

    

