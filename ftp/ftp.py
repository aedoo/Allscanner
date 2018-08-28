#coding:utf-8

import ftplib
import sys,socket

def ftpburp(ip,port):


    with open('ftp\user.txt','r') as user:
        users = user.readlines()

    with open('ftp\pass.txt','r') as passs:
        pwds = passs.readlines()

    user.close()
    passs.close()

    addr = (ip, int(port))
    sock_21 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock_21.connect(addr)
        # print sock_21.recv(1024)

        for user in users:
            user = user.strip()
            for password in pwds:
                password = password.strip()
                try:
                    ftp = ftplib.FTP()
                    ftp.timeout = 10
                    ftp.connect(host=ip, port=int(port))
                    ftp.login(user=user,passwd=password)
                    sys.stdout.write('%s:%d has FTP WeakPass, %s:%s\n' % (ip, port, user, password))
                    ftp.close()
                    

                except Exception,e:
                    continue
    except:
        sock_21.close()
