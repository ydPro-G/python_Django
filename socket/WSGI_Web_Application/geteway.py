import os
import sys
# from app import simple_app


def simple_app(environ,start_response):
    """简单的Web Application，拿到数据后设置对应的状态和header"""
    status = '200 OK' # 状态码，标志
    response_headers = [('Content-type','text/html')]# 响应头
    start_response(status,response_headers)
    return [b'Hello World! -by G \n']


def wsgi_to_bytes(s):
    return s.encode()

def run_with_cgi(application):
    environ = dict(os.environ.items()) # 获得系统的各种信息，以字典形式返回
    # 向字典中添加元素
    environ['wsgi.input'] = sys.stdin.buffer
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True

    # 判断使用的是https协议还是http协议
    if environ.get('HTTPS','off') in ('on','1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'
    
    headers_set = []
    headers_sent = []

    def write(data):
        out = sys.stdout.buffer # 输出流缓存

        # 如果没有发送hedder，则抛出AssertionError异常
        if not headers_set:
            raise AssertionError("write() before start_response()") # 写在开始响应之前
        
        elif not headers_sent:
            # 在输出第一行数据之前，先发送响应头
            status,response_headers = headers_sent[:] = headers_set
            out.write(wsgi_to_bytes('Status: %s\r\n' % status)) # 写状态码
            for header in response_headers:
                out.write(wsgi_to_bytes('%s:%s\r\n' % header)) # 写状态码
            out.write(wsgi_to_bytes('\r\n'))
        
        out.write(data)
        out.flush()
   
   # 通过回调函数↓，设置response状态和header,最后返回body
    def start_response(status,response_headers,exc_info=None):# 开始响应
        if exc_info:
            try:
                if headers_sent:
                    # 如果已经发送了header，则重新抛出原始异常信息
                    raise (exc_info[0], exc_info[1], exc_info[2])
            finally: # finally 不管有没有异常都可以执行的代码
                exc_info = None  # 避免循环引用
        elif headers_set:
            raise AssertionError('Headers already set!')

        headers_set[:] = [status,response_headers]
        return write

    result = application(environ,start_response) # 接收环境变量，回调函数

    try:
        for data in result:
            if data:    # 如果没有body数据，则不发送header
                write(data)
        if not headers_sent:
            write('') # 如果body为空，就发送数据header
    finally:
        if hasattr(result,'close'):
            result.close()

if __name__ == '__main__':
    run_with_cgi(simple_app) # 获得系统消息，返回Web application




# raise:抛出一个指定的有x = 10 if x > 5: raise Exception('x值不能大于5，x值为：{}'.format(x))

