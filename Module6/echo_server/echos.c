/*
** echos.c -- the echo server for echoc.c; demonstrates unix sockets
 * https://beej.us/guide/bgipc/html/split/unixsock.html
 */

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>

#define error(ex, er, msg) \
{ \
    fflush(stdout); \
    fprintf(stderr, msg ": %s\n", strerror(er)); \
    if (ex) exit(ex); \
}

#define SOCK_PATH "echo_socket"


int main(void) {
    int s, s2, len;
    unsigned t;
    struct sockaddr_un local, remote;
    char dat[100];

    if ((s = socket(AF_UNIX, SOCK_STREAM, 0)) == -1) {
        error(1, errno, "socket");
    }

    if (access(SOCK_PATH, F_OK) == 0) {
        puts("Stale socket found; attempting to remove...");
        if (unlink(SOCK_PATH) == -1) {
            error(1, errno, "unlink");
        }
        else {
            puts("  socket successfully removed");
        }
    }

    local.sun_family = AF_UNIX;
    strcpy(local.sun_path, SOCK_PATH);
    len = strlen(SOCK_PATH) + sizeof(remote.sun_family);
#ifdef __APPLE__
    // There are only two hard things in computer science:
    // cache invalidation, naming things, and off-by-one errors.
    len += 1;
#endif

    if (bind(s, (struct sockaddr *)&local, len) == -1) {
        error(1, errno, "bind");
    }

    if (listen(s, 5) == -1) {
        error(1, errno, "listen");
    }

    for (;;) {
        int done, n;
        puts("Waiting for a connection...");
        t = sizeof(remote);
        if ((s2 = accept(s, (struct sockaddr *)&remote, &t)) == -1) {
            error(1, errno, "accept");
        }

        puts("Connected.");

        done = 0;
        do {
            n = recv(s2, dat, 100, 0);
            if (n <= 0) {
                if (n < 0) {
                    error(0, errno, "recv");
                }
                done = 1;
            }
            else
                dat[n] = '\0';

            if (!done) {
                printf("Sending: %s", dat);
                if (send(s2, dat, n, 0) < 0) {
                    error(0, errno, "send");
                    done = 1;
                }
            }
        } while (!done);

        if (close(s2) != 0) {
            error(1, errno, "close");
        }
    }

    return 0;
}
