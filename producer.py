# producer.py
import nsq
import tornado.ioloop
import time

def pub_callback(conn, data):
    print(f"[+] Published: {data}")

def publish_message():
    writer.pub(b'my_topic', b'Hello from Python!', pub_callback)

writer = nsq.Writer(['127.0.0.1:4150'])  # 4150 is the TCP port for nsqd

ioloop = tornado.ioloop.IOLoop.instance()
ioloop.add_timeout(time.time() + 1, publish_message)
nsq.run()
