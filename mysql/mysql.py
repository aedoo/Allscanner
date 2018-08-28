import socket
import MySQLdb
import sys

def mysqlburp(ip,port):

    with open('mysql\user.txt','r') as user_file:
        users = user_file.readlines()

    with open('mysql\password.txt','r') as pass_file:
        passs = pass_file.readlines()

    addr = (ip,int(port))
    sock_3306 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock_3306.settimeout(1)
        sock_3306.connect(addr)

        for user in users:
            user = user.strip()
            for password in passs:
                password = password.strip()
                try:
                    MySQLdb.connect(ip, user, password)
                    sys.stdout.write('%s:%d has MySQL WeakPass, %s:%s\n' % (ip, port, user, password))

                except:
                    continue

    except:
        sock_3306.close()
