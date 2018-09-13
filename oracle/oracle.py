#coding:utf-8

import socket,sys
import cx_Oracle

def oracleburp(ip,port):

    addr = (ip,int(port))

    with open('oracle\user.txt') as user:
        users = user.readlines()
    user.close()

    with open('oracle\pass.txt') as passs:
        passwords = passs.readlines()
    passs.close()

    sock_1521 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock_1521.settimeout(0.5)
        sock_1521.connect(addr)


        for un in users:
            un = un.strip()
            for pwd in passwords:
                pwd = pwd.strip()
                try:
                    conn = cx_Oracle.connect(un, pwd, ip + ':1521/orcl')
                    sys.stdout.write('%s:%d has Oracle SQL WeakPass, %s:%s\n' % (ip, port, un, pwd))
                except Exception,e:
                    continue
    except:
        sock_1521.close()
