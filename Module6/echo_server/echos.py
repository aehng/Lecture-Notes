# echos.c -- the echo server for echoc.c; demonstrates unix sockets
# http://beej.us/guide/bgipc/html/multi/unixsock.html

import os
import socket
import sys


SOCK_PATH = "echo_socket"

def main():
    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        if os.access(SOCK_PATH, os.F_OK):
            print("Stale socket found; attempting to remove...")
            os.unlink(SOCK_PATH)

        s.bind(SOCK_PATH)
        s.listen(5)

        while True:
            print("Waiting for a connection...")
            s2, addr = s.accept()
            print("Connected.")

            done = False
            while not done:
                dat = s2.recv(100)
                n = len(dat)
                if n <= 0:
                    if n < 0:
                        print("Something went wrong with s2.recv()")
                    done = True

                if not done:
                    print(f"Sending: {dat.decode('utf-8')}", end="")
                    s2.send(dat)

            s2.close()

    except KeyboardInterrupt:
        # This happens when the user hits Ctrl-C to quit the program
        print()
        sys.exit(130)

    except Exception as e:
        print("Something unexpected went wrong...", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
