#coding:utf-8
import socket
import ldap,sys

def ldapburp(ip, port):
    try:
        HOST = ip
        PORT = 389
        addr = (HOST, PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.settimeout(1)
            s.connect(addr)
        except:
            s.close()

        uri = "ldap://%s:389/" % HOST

        try:
            s.close()
            obj = ldap.initialize(uri)
            try:
                dn = obj.read_rootdse_s()['namingContexts']
                sys.stdout.write('%s:%d is Ldap Unauthorized, INFO:%s\n' % (HOST, PORT, dn))

            except:
                pass
        except:
            s.close()
    except:
        pass