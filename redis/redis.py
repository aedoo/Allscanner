import socket,sys

def redisburp(ip,port):

    addr = (ip,port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(1)
        s.connect(addr)
    except:
        s.close()

    data = "ping\n"

    try:
        s.send(data)
        response = s.recv(1024)
        if "+PONG" in response:
            sys.stdout.write('%s:%d is Redis Unauthorized\n' % (ip,port))
    except:
        s.close()
    s.close()