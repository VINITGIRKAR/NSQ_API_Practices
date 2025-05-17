# consumer.py
import nsq
import tornado.ioloop

def handler(message):
    print(f"[✓] Received message: {message.body.decode()}")
    message.finish()  # acknowledge processing success

reader = nsq.Reader(
    message_handler=handler,
    lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic='my_topic',
    channel='test_channel',
    lookupd_poll_interval=15,
)

nsq.run()
