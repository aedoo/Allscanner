import socket,sys
import pymongo

def mongoburp(ip,port):

    addr = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(1)
        s.connect(addr)
        client = pymongo.MongoClient(ip, 27017)
        db = client.mongotest
        db.my_collection.insert_one({"x": 1}).inserted_id
        client.drop_database('mongotest')
        sys.stdout.write('%s:%d is MongoDB Unauthorized\n' % (ip, port))

    except:
        s.close()
