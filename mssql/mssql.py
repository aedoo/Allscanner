#coding:utf-8

import socket,sys
import pymssql

def mssqlburp(ip,port):

    addr = (ip,int(port))

    with open('mssql\user.txt') as user:
        users = user.readlines()
    user.close()

    with open('mssql\pass.txt') as passs:
        passwords = passs.readlines()
    passs.close()

    sock_1433 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock_1433.settimeout(1)
        sock_1433.connect(addr)
        host = ip + ':' + str(port)

        for un in users:
            un = un.strip()
            for pwd in passwords:
                pwd = pwd.strip()
                try:
                    conn = pymssql.connect(host=host,user=un,password=pwd)
                    sys.stdout.write('%s:%d has MicroSoft SQL WeakPass, %s:%s\n' % (ip, port, un, pwd))
                except Exception,e:
                    continue
    except:
        sock_1433.close()
