#coding:utf-8
import urllib2
import sys,socket


def elasticburp(ip,port):


    addr = (ip,int(port))
    url = "http://" + ip + ":" + str(port) + "/_cat"

    sock_9200 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        sock_9200.settimeout(1)
        sock_9200.connect(addr)

        #print '%s 9200 open!'

        try:
            data = urllib2.urlopen(url).read()
            if '/_cat/master' in data:
                sys.stdout.write('%s:%d is ElasticSearch Unauthorized\n' % (ip, port))

        except:
            pass
    except:
        sock_9200.close()