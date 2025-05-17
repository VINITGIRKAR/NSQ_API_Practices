# output of producers.py
Microsoft Windows [Version 10.0.22631.5335]
(c) Microsoft Corporation. All rights reserved.

(C:\NSQ_API\venv1) C:\NSQ_API>python producers.py
[+] Published: b'OK'
[127.0.0.1:4150:127.0.0.1:4150] connection is stale (318.75s), closing
uncaught exception in data event
Traceback (most recent call last):
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\nsq\conn.py", line 289, in _read_body
    self.trigger(event.DATA, conn=self, data=data)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\nsq\event.py", line 84, in trigger
    ev(*args, **kwargs)
    ~~^^^^^^^^^^^^^^^^^
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\nsq\conn.py", line 504, in _on_data
    self.send(protocol.nop())
    ~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\nsq\conn.py", line 295, in send
    return self.stream.write(self.encoder.encode(data))
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\nsq\conn.py", line 295, in send
    return self.stream.write(self.encoder.encode(data))
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
    return self.stream.write(self.encoder.encode(data))
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\tornado\iostream.py", line 523, in write
    self._check_closed()
    self._check_closed()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\tornado\iostream.py", line 998, in _check_closed      
    raise StreamClosedError(real_error=self.error)
  File "C:\Users\vinit\AppData\Roaming\Python\Python313\site-packages\tornado\iostream.py", line 998, in _check_closed      
    raise StreamClosedError(real_error=self.error)
    raise StreamClosedError(real_error=self.error)
tornado.iostream.StreamClosedError: Stream is closed
tornado.iostream.StreamClosedError: Stream is closed
[127.0.0.1:4150:127.0.0.1:4150] ERROR: ConnectionClosedError('Stream is closed')
[127.0.0.1:4150:127.0.0.1:4150] ERROR: ConnectionClosedError('Stream is closed')
[127.0.0.1:4150] connection closed
