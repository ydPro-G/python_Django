# coding:utf-8 

import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''<h2>Hello World!</h2><h1> 我们接下来学习django开发</h1>'''
response_params = [  # 响应参数
    'HTTP/1.0 200 OK',   # 状态行，响应时的状态行
    'Date:Sat,18 apr 2020 01:01:01 GMT', #消息报头-时间
    'Content-Type:text/html; charset=utf-8', # 消息报头-内容类型
    'Content-Length: {}\r\n', format(len(body.encode())), # 消息报头-内容长度
    body # 相应正文
]
response = '\r\n'.join(response_params) # 响应数据，body内容长度+内容

def handle_connection(conn,addr):
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024) #从socket中读取字符
    print(request)
    conn.send(response.encode())  #response转为bytes后传输
    conn.close()

def main():
    #socket.AF_INET用于服务器与服务器之间网络通信
    #socket.SOCK_STREAM用于基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 创建socket
    #设置端口可复用，保证我们每次按ctrl+c组合键后，快速重启
    serversocket.setsockopt(socket.SOL_SOCKET,socket.SOCK_STREAM, 1)
    serversocket.bind(('127.0.0.1',8000)) # 绑定端口号
    serversocket.listen(5) #监听该端口号，最大排队数5
    print('http://127.0.0.1:8000')

    try:
        while True:
            conn,address = serversocket.accept() # 允许客户端连接请求 
            handle_connection(conn, address) # 调用句柄连接函数
    finally:
        serversocket.close() # 关闭

if __name__ == '__main__':
    main() # 运行socket链接