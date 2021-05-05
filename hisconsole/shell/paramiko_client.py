# coding: utf-8
import time
import paramiko
import re

batchcmd = """pwd
cd /home
pwd
echo 'start'
df -h
cd abc
ls"""

def ssh(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
    ssh.connect('192.168.31.85',22,'root','982128')    #SSH端口默认22，可改
    stdin,stdout,stderr = ssh.exec_command(cmd)    #这三个得到的都是类文件对象
    outmsg,errmsg = stdout.read(),stderr.read()    #读一次之后，stdout和stderr里就没有内容了，所以一定要用变量把它们带的信息给保存下来，否则read一次之后就没有了
    #outmsg = str(outmsg)
    #print(outmsg.replace("\\n","\\r\\n"))
    print(outmsg.decode())
    print(errmsg)
    if errmsg == "":
        print(outmsg)
    ssh.close()

# 定义一个类，表示一台远端linux主机
class Linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3

    # 调用该方法连接远程主机
    def connect(self):
        while True:
            # 连接过程中可能会抛出异常，比如网络不通、链接超时
            try:
                self.t = paramiko.Transport(sock=(self.ip, 22))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                # 如果没有抛出异常说明连接成功，直接返回
                print(u'连接%s成功' % self.ip)
                # 接收到的网络数据解码为str
                print(self.chan.recv(65535).decode('utf-8'))
                return
            # 这里不对可能的异常如socket.error, socket.timeout细化，直接一网打尽
            except Exception as e1:
                if self.try_times != 0:
                    print(u'连接%s失败，进行重试' % self.ip)
                    self.try_times -= 1
                else:
                    print(u'重试3次失败，结束程序')
                    exit(1)

    # 断开连接
    def close(self):
        self.chan.close()
        self.t.close()

    # 发送要执行的命令
    def send(self, cmd):
        cmd += '\r'
        # 通过命令执行提示符来判断命令是否执行完成
        p = re.compile(r']$')

        result = ''
        # 发送要执行的命令
        self.chan.send(cmd)
        # 回显很长的命令可能执行较久，通过循环分批次取回回显
        while True:
            time.sleep(2)
            ret = self.chan.recv(65535)
            ret = ret.decode('utf-8')
            result += ret
            if p.search(ret):
                print(result)
                return (result)

# if __name__ == '__main__':
#     host = Linux('192.168.31.85', 'root', '982128')
#     host.connect()
#     host.send('ll')
#     host.close()

def sshBatch(ip,batchcmd=batchcmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
    ssh.connect(ip,22,'root','982128')    #SSH端口默认22，可改
    command = ssh.invoke_shell()
    message=""
    for line in batchcmd.split('\n'):
        command.send(line + "\n")
        time.sleep(1)
        output = command.recv(65535)
        output = output.decode("ascii")
        print(output)
        message += output
    ssh.close()
    return message



if __name__ == '__main__':
    # ssh("df -h")
    ip_list =['192.168.31.85']
    for ip in ip_list:
        sshBatch(ip,batchcmd)
