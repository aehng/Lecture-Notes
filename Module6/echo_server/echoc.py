# echoc.py -- the echo client for echos.c; demonstrates unix sockets
# https://beej.us/guide/bgipc/html/split/unixsock.html

import socket
import sys


SOCK_PATH = "echo_socket"

def main():
    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        print("Trying to connect...")

        s.connect(SOCK_PATH)
        print("Connected.")

        while True:
            dat = input("> ")
            s.send(bytes(dat + "\n", "utf-8"))
            dat = s.recv(100).decode("utf-8")
            print(f"echo> {dat}", end="")

        print("Server closed connection")
        s.close()

    except EOFError:
        # This happens when the user hits Ctrl-D to quit the program
        s.close()

    except KeyboardInterrupt:
        # This happens when the user hits Ctrl-C to quit the program
        print()
        sys.exit(130)

    except Exception as e:
        print("Something unexpected went wrong...", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
