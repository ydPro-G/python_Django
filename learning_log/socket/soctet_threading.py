# 监听端口，接受外部请求
import errno
import socket
import threading
import time
 
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''<h1> Hello World!<h1> - form {thread_name}'''  # 响应体数据，thread_name 代表的是当前线程
response_params = [ # 响应参数
    'HTTP/1.0 200 OK',
    'Date: Sun, 27 may 2019 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {length}\r\n',
    body,
]
response = '\r\n'.join(response_params) # 响应内容
 
 
def handle_connection(conn, addr): #句柄连接
    print(conn, addr) # 打印连接客户端，打印ip
    time.sleep(10)  # 可以自行尝试打开注释，设置睡眠时间
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)  # 注意在设置为非阻塞模式时这里会有报错，将 serversocket.setblocking(0)，设置为1即可解决
 
    print(request)
    current_thread = threading.currentThread() # 当前线程
    content_length = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name) #thread-1
    #以http格式回复数据，format:print('网站名：{name}.format(name='线程数量')'  返回数据是response.format(获取到的线程名字)
    conn.send(response.format(thread_name=current_thread.name, length=content_length).encode())  # 发送回应
    conn.close()
 
 
def main(): # sock运行函数
    # socket.AF_INET    用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM    基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #实例化socket，创建服务器连接
    # 设置端口可复用，保证我们每次Ctrl C之后，快速再次重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000)) # 绑定ip
    # 可参考：https://stackoverflow.com/questions/2444459/python-sock-listen
    serversocket.listen(10) #监听该端口，最大请求数
    print('http://127.0.0.1:8000')
    serversocket.setblocking(1)  # 设置socket为非阻塞模式，改为1即可运行  

 
    try:
        i = 0
        while True:
            try:
                conn, address = serversocket.accept() # 调用accept允许请求连接，建立新的socket
            except socket.error as e:
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1 # 数量+就代表了开启了新线程
            print(i) #1
            t = threading.Thread(target=handle_connection, args=(conn, address), name='thread-%s' % i)
            t.start()
    finally:
        serversocket.close()
 
 
if __name__ == '__main__':
    main()  


#serversocket.setblocking(0）：设置为非阻塞模式：当前socket不会再accept或者recv时处于阻塞状态（必须有连接或者数据过来时才执行下一步）
#通过accept接受连接后，开启一个新的线程来处理这个连接，而主程序可以继续在 while true循环中处理其他连接



#serversocket.setblocking(0):参数为0时为非阻塞状态，书上提及这个（47行）设为非阻塞状态的时（24行）request += conn.recv(1024)会报错。我的报错内容是：[WinError 10035] 无法立即完成一个非阻止性套接字操作。
# 通过搜索大约解答为：设置了non-block模式后, recv如果无法接受到数据。



#socket.socket.setblocking(flag)如果flag为0, 则将套接字设置为非阻塞模式。
#否则, 套接字将设置为阻塞模式（默认值）。在非阻塞模式下, 如果recv()调用没有发现任何数据或者send()调用无法立即发送数据, 那么将引发socket.error异常。在阻塞模式下, 这些调用在处理之前都将被阻塞。


#所产生的结果都是使I/O变成非阻塞模式(non-blocking)，在读取不到数据或是写入缓冲区已满会马上return，而不会阻塞等待。


#serversocket.listen()方法. 参数是监听等待队列的大小. 它告诉了操作系统, 在python代码accept前, 缓存多少TCP/IP连接在队列中.
#  每次python代码调用accept()的时候, 一个连接从队列中移除, 为新的连接进来空出一个位置. 如果队列满了, 新的连接自动放弃, 给客户端带来不必要的网络延迟