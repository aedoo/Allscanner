#coding:utf-8
import psycopg2
import sys,socket

def postgreburp(ip,port):
    with open('postgresql\user.txt') as user:
        users = user.readlines()
    user.close()

    with open('postgresql\pass.txt') as passs:
        pwds = passs.readlines()
    user.close()

    addr = (ip, int(port))
    sock_5432 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        sock_5432.settimeout(1)
        sock_5432.connect(addr)
    except:
        sock_5432.close()

    for un in users:
        un = un.strip()
        for pwd in pwds:
            pwd = pwd.strip()
            try:

                pgscon = psycopg2.connect(host=ip, port=port, user=un, password=pwd)
                sys.stdout.write('%s:%d has PostgreSQL WeakPass, %s:%s\n' % (ip, port, un, pwd))
            except Exception,e:
                continue







