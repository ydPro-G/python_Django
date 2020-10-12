# coding:utf-8 
# 服务器socket并没有用来做数据处理, 而是接受服务器过来的连接, 然后建立一个新的socket, 用来和客户端通讯.
import socket

EOL1 = b'\n\n' #分割http头部和body
EOL2 = b'\n\r\n' 



body = '''<h2>Hello World!</h2><h1> 我们接下来学习django开发</h1>'''
response_params = [  # 响应参数
    'HTTP/1.0 200 OK',   # 状态行，响应时的状态行
    'Date:Sat,18 apr 2020 01:01:01 GMT', #消息报头-时间
    'Content-Type:text/html; charset=utf-8', # 消息报头-内容类型
    'Content-Length: {}\r\n', format(len(body.encode())), # 消息报头-内容长度
    body #body也响应
]
response = '\r\n'.join(response_params) # 响应数据，body内容长度+内容



# conn 连接客户端，addr ip地址，端口
def handle_connection(conn,addr):   # 接受请求数据，直到一个完整的http请求被接收完毕
    request = b"" 
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)  # 循环处理客户端请求
    print(request)
    conn.send(response.encode())  #response转为bytes后传输,发送回应
    conn.close() #关闭



def main(): # 运行函数
    #socket.AF_INET用于服务器与服务器之间网络通信
    #socket.SOCK_STREAM用于基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 创建服务器的连接
    #设置端口可复用，保证我们每次按ctrl+c组合键后，快速重启，即使其他程序也在监听同样的端口
    serversocket.setsockopt(socket.SOL_SOCKET,socket.SOCK_STREAM, 1)
    serversocket.bind(('127.0.0.1',8000)) # 绑定端口号
    serversocket.listen(5) #监听该端口号，响应从客户端过来的连接请求
    print('http://127.0.0.1:8000')

    try:
        while True:
            conn,address = serversocket.accept() # 允许客户端连接请求 
            handle_connection(conn, address) # 调用句柄连接函数
    finally:
        serversocket.close() # 关闭

if __name__ == '__main__':
    main() # 运行socket链接



# 1.serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)[创建服务器连接]
# 2.serversocket.setsockopt(socket.SOL_SOCKET,socket.SOCK_STREAM, 1) [设置端口可复用，即使其他程序也在监听同样的端口]
# 3.serversocket.bind(('127.0.0.1',8000)) 绑定使用的端口号
# 4.serversocket.listen(5) [监听该端口，响应从客户端过来的连接请求，连接最大排队数5]
# 5.conn,address = serversocket.accept() [程序一直停在这。直到建立了一个连接，这个时候服务器socket建立一个新的socket，用来和客户端通讯 这个新的socket是accept()的返回值, address对象标示了客户端的IP地址和端口. ]
# 6.request = b"" 
#    while EOL1 not in request and EOL2 not in request:
#       request += conn.recv(1024)  [接收数据，直到一个完整的http请求接收完毕，这是一个简单的http服务器实现]