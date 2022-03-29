# networking/nonblocking/tcp_multithreaded_server.py
import socket
import threading


def main():
    host = "127.0.0.1"
    port = 5001
    s = socket.socket()
    network_host = (host, port)
    s.bind(network_host)
    s.listen(10)

    while True:
        conn, addr = s.accept()
        # If there is no response in 5 minutes, close connection
        conn.settimeout(60)
        print(f"Connection from {addr}")
        # Create a new thread
        #   target = function/method that will be called when the thread starts
        #   arge = arguments to pass to target function
        thread = threading.Thread(target=listen_to_client, args=(conn, addr))
        thread.start()


def listen_to_client(conn: socket.socket, addr):
    print(type(addr))
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            prompt = (f"Received from {addr}: ").ljust(40)
            print(f"{prompt}: {addr}")

        except socket.timeout as err:
            print(f"socket from {addr} timed out")
            print(err)
        except IOError as err:
            print(f"IOError from socket at {addr}")
            print(err)
            break
    conn.close()


if __name__ == "__main__":
    main()
