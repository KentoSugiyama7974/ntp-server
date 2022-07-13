import socket
import threading as th
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 60002))
# sock.setblocking(False)


def socket_start():
    # f = "%Y-%m-%d %H:%M:%S.%f"
    try:
        print("wait...")
        t0, addr = sock.recvfrom(1024)
        t0 = t0.decode('utf-8')
        t0 = float(t0)
        t1 = time.time()
        print(t0, t1)
        print(str(t1-t0))
        t2 = time.time()
        print(t2)
        sock.sendto(bytes(f"{str(t1-t0)},{str(t2)}",'utf-8'), addr)

    except KeyboardInterrupt:
        sock.close()

def while_thread():
    while True:
        socket_start()

# thread = th.Thread(target=while_thread)
# thread.setDaemon(True)
# thread.start()

while_thread()

