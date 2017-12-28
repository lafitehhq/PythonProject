# -*- coding:utf-8 -*-

"""
浏览器作为客户端，jingdong.py作为服务端。
运行后显示字体，浏览器输入：http://127.0.0.1:8089/ 
"""

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8089))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        print(buf.decode('utf8'))

        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n", "utf8"))
        # 方式一：
        # connection.sendall(bytes("<h1 style = 'color:red'>Hello,Vito</h1>", "utf8"))
        # 方式二：
        with open('hello.html', 'rb') as f:
            data = f.read()
        connection.sendall(data)

        connection.close()

if __name__ == '__main__':
    main()