import socket

def check():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.google.com', 80))
        s.close()
        print('You are Online')
    except Exception:
        print('You are Offline')
        exit(0)

check()