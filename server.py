import socket
def tcp(host:str,port:int,back_log:int):
    tcpSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpSocket.bind((host,port))
    #能连接多少个客户端
    tcpSocket.listen(back_log)
    buffer_size=1024
    print("---------starting server---------")
    print("server socket:",tcpSocket)
    #阻塞等待

    while True:
        conn, address = tcpSocket.accept()  # 在这个位置进行等待，监听端口号,返回一个新的client的socket
        print(conn)
        print('client address:', address)
        print('------ready to read msg-------')
        while 1:
            try:
                # 接受套接字的大小，怎么发就怎么收
                msg = conn.recv(buffer_size)
                conn.send("收到消息".encode('utf-8'))
                if msg.decode('utf-8') == "close":
                    # 断开连接
                    conn.close()
                    break
                print('server received:', msg.decode('utf-8'))
            except Exception as e:
                conn.close()
                break
        break
    print("----------stop the server------------")
    tcpSocket.close()

def udp():
    udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



if __name__ == '__main__':
    tcp('127.0.0.1',8000,8)
