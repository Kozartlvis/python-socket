# Python Socket编程
## Socket(套接字)
套接字（socket）是一个抽象层，应用程序可以通过它发送或接收数据，可对其进行像对文件一样的打开、读写和关闭等操作。套接字允许应用程序将I/O插入到网络中，并与网络中的其他应用程序进行通信。网络套接字是IP地址与端口的组合。
## 创建Socket及源码分析
```python
import socket
tcpSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

```
python创建tcp/udp socket对象
对socket.socket()源码分析：
```python
def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
    # For user code address family and type values are IntEnum members, but
    # for the underlying _socket.socket they're just integers. The
    # constructor of _socket.socket converts the given argument to an
    # integer automatically.
    if fileno is None:
        if family == -1:
            family = AF_INET
        if type == -1:
            type = SOCK_STREAM
        if proto == -1:
            proto = 0
    _socket.socket.__init__(self, family, type, proto, fileno)
    self._io_refs = 0
    self._closed = False
```
代码解析：  
Socket的构造函数参数有`family`：套接字地址簇,`type`：套接字类型,`proto`：协议号,`fileno`：文件号
可以看到默认的构造函数是`family = AF_INET,type = SOCK_STREAM,proto = 0`。而且这些套接字都是在`_sokcet.py`枚举类中，将字符转换成Int类型
**socket families(地址簇)：**
AF_UNIX：unix本机之间进行通信  
AF_INET：使用IPv4  
AF_INET6：使用IPv6  
**socket types：**
SOCK_STREAM：TCP套接字类型  
SOCK_DGRAM：UDP套接字类型  
SOCK_RAW：原始套接字类型，这个套接字比较强大,创建这种套接字可以监听网卡上的所有数据帧  
SOCK_RDM：是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。  
**协议号**：通常为零，可以省略，或者在地址族为AF_CAN的情况下，协议应为CAN_RAW或CAN_BCM 。
**指定fileno**：则忽略其他参数，从而导致具有指定文件描述器的套接字返回。
## TCP



 