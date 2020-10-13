# coding:utf-8
# 简单的应用程序

def simple_app(environ,start_response):
    """简单的Web Application，拿到数据后设置对应的状态和header"""
    status = '200 OK' # 状态码，标志
    response_headers = [('Content-type','text/plain')]# 响应头
    start_response(status,response_headers)
    return [b'Hello World! -by G \n']


# WSGI协议规定，application必须是一个可调用的对象
class AppClass(object):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
 
    def __call__(self, environ, start_response):
        print(environ, start_response)
        start_response(self.status, self.response_headers)
        return ['Hello AppClass.__call__\n']
 
application = AppClass()


# WSGI Server 调用WSGI Application 大致流程

def start response(status , headers):
    ＃ 伪代码
    set_status(status)
    for k , v in headers :
        set_header (k , v )
 
def handle conn(conn):
    ＃调用我们定义的application （也就是上面的simple_app ，或者是AppClass 的实例，或者是AppClassiter 本身）
    app = application(environ, start_response)
    ＃边历返回的结果， 生成response
    for data in app :
        response += data
 
    conn.sendall (response)