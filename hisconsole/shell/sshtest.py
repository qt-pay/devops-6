from socket import socket

from hisconsole.shell.ssh import SSH

batchcmd = """pwd
cd /home
pwd
echo 'start'
df -h
cd abc
ls"""

if __name__ == '__main__':
    client = SSH(hostname="192.168.31.85",password="982128")
    # message = client.exec_command(batchcmd)
    # print(message)

    for code, out in client.exec_command_with_stream(batchcmd):
        print(out)
