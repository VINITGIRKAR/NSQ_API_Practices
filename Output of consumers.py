# Output of consumers.py
Microsoft Windows [Version 10.0.22631.5335]
(c) Microsoft Corporation. All rights reserved.

(C:\NSQ_API\venv1) C:\NSQ_API>python consumers.py
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[my_topic:test_channel] lookupd http://127.0.0.1:4161/lookup?topic=my_topic query error: HTTP 404: Not Found
[✓] Received message: Hello from Python!
[VINIT:4150:my_topic:test_channel] connection is stale (310.61s), closing
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
[VINIT:4150:my_topic:test_channel] ERROR: ConnectionClosedError('Stream is closed')
[VINIT:4150:my_topic:test_channel] ERROR: ConnectionClosedError('Stream is closed')
[VINIT:4150:my_topic:test_channel] connection closed
