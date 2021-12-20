import os

def release_port(port):
    """释放指定的端口"""

    #查找对应端口的pid
    cmd_find='netstat -aon | findstr %s' %port
    print(cmd_find)

    #返回命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)

    if  str(port) and 'LISTENING' in result:
        #获取端口对应的pid进程
        i=result.index('LISTENING')
        start=i+len('LISTENING')+7
        end=result.index('\n')
        pid=result[start:end]

        # 关闭被占用端口的pid
        cmd_kill='taskkill -f -pid %s' %pid
        print(cmd_kill)
        os.popen(cmd_kill)

    else:
        print('port %s is available !' %port)


if __name__ == '__main__':
    host='127.0.0.1'
    port=4723
    # check_port(host,port)
    release_port(port)