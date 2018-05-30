import os

from socketIO_client import SocketIO


def on_connect():
    print('connect')


def on_disconnect():
    print('disconnect')


def on_reconnect():
    print('reconnect')


def on_message(message):
    print(message)


socket_ = SocketIO(os.environ['SOCKET_URL'], verify=False)
socket_.emit('data', {
    'type': 'subscribe',
    'channel': 'order_book',
    'payload': {
        'baseTokenAddress': '0x6ff6c0ff1d68b964901f986d4c9fa3ac68346570',
        'quoteTokenAddress': '0xd0a1e359811322d97991e03f863a0c30c2cf029c',
        'snapshot': 'true',
        'depth': '100'
    }
})
socket_.on('message', on_message)
socket_.on('connect', on_connect)
socket_.wait()
