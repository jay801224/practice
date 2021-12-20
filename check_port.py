import socket

def check_port(host, port):
    """检测指定的端口是否被占用"""

    #创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError as msg:
        print('port %s is available! ' %port)
        print(msg)
        return True
    else:
        print('port %s already be in use !' % port)
        return False


if __name__ == '__main__':
    host='127.0.0.1'
    port=4723
    check_port(host,port)