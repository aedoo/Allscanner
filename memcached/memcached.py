#coding:utf-8

import socket,sys

def memcachedburp(ip,port):
    addr = (ip,int(port))

    sock_11211 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        sock_11211.settimeout(1)
        sock_11211.connect(addr)

        try:
            sock_11211.send("stats\r\n")
            result = sock_11211.recv(1024)

            if "version" in result:
                sys.stdout.write('%s:%d is Memcached Unauthorized\n' % (ip, port))
        except Exception:
            pass

    except:
        sock_11211.close()