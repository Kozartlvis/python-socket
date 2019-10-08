import socket
def tcpClient(host:str,port:int):
    tcpSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpSocket.connect((host,port))
    #能连接多少个客户端
    buffer_size=1024
    print("---------starting client---------")
    print("client socket:",tcpSocket)
    while True:
        msg = input('please input\n')
        # 防止输入空消息
        if not msg:
            continue
        tcpSocket.send(msg.encode('utf-8'))  # 收发消息一定要二进制，记得编码
        back_msg=tcpSocket.recv(buffer_size)
        print("client received:"+back_msg.decode('utf-8'))
        if msg == "close":
            break
    print("--------stop the client----------")
    tcpSocket.close()
if __name__ == '__main__':
    tcpClient('127.0.0.1',8000)