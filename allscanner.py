#coding:utf-8

#author:aedoo
#github:https://github.com/aedoo

import threading,Queue
import base64,ipaddr
import argparse
import time

from redis.redis import redisburp
from mysql.mysql import mysqlburp
from mongodb.mongodb import mongoburp
from ftp.ftp import ftpburp
from postgresql.postgresql import postgreburp
from mssql.mssql import mssqlburp
from memcached.memcached import memcachedburp
from elasticsearch.elasticsearch import elasticburp
from oracle.oracle import oracleburp
from ldapc.ldap import ldapburp


class AllScanner(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):

        while True:
            if self.queue.empty():
                break

            else:
                try:
                    ip = self.queue.get(timeout=0.5)

                    redisburp(ip,6379)
                    mysqlburp(ip,3306)
                    mongoburp(ip,27017)
                    ftpburp(ip,21)
                    postgreburp(ip,5432)
                    mssqlburp(ip,1433)
                    memcachedburp(ip,11211)
                    elasticburp(ip,9200)
                    ldapburp(ip,389)
                    oracleburp(ip,1521)

                except Exception:
                    continue

def main():

    print ''
    logo_encode = 'ICAgIF9fXyAgICBfX19fX19fX18gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgLyAgIHwgIC8gLyAvIF9fXy9fX19fX19fX19fX19fX18gIF9fX18gIF9fXyAgX19fX18KICAvIC98IHwgLyAvIC9cX18gXC8gX19fLyBfXyAgLyBfXyBcLyBfXyBcLyBfIFwvIF9fXy8KIC8gX19fIHwvIC8gL19fXy8gLyAvX18vIC9fLyAvIC8gLyAvIC8gLyAvICBfXy8gLyAgICAKL18vICB8Xy9fL18vL19fX18vXF9fXy9cX19fXy9fLyAvXy9fLyAvXy9cX19fL18v='
    logo = base64.b64decode(logo_encode)
    print logo + '\n\n'
    print 'github:https://github.com/aedoo/' + '\n\n'

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='cidr_ip', help='IP segment like 192.168.1.1/16 contains 65536 IP.')
    parser.add_argument('-t', dest='thread_number', type=int, default=100, help='Setting the number of threads')
    args = parser.parse_args()

    print ''

    IP_Duan = str(args.cidr_ip)

    try:
        IPs = ipaddr.IPNetwork(IP_Duan)
        thread_number = args.thread_number

        threads = []
        queue = Queue.Queue()

        for ip in IPs:
            queue.put(str(ip))

        for i in xrange(thread_number):
            threads.append(AllScanner(queue))

        for t in threads:
            t.start()
        for t in threads:
            t.join()

    except Exception:
        parser.print_help()


if __name__ == '__main__':

    time_start = time.time()
    main()
    time_all = time.time()-time_start
    print 'All Finish. Use %ss' % time_all