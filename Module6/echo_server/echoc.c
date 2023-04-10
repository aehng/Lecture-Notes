/*
** echoc.c -- the echo client for echos.c; demonstrates unix sockets
 * http://beej.us/guide/bgipc/html/multi/unixsock.html
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
    int s, t, len;
    struct sockaddr_un remote;
    char dat[100];

    if ((s = socket(AF_UNIX, SOCK_STREAM, 0)) == -1)
        error(1, errno, "socket");

    puts("Trying to connect...");

    remote.sun_family = AF_UNIX;
    strcpy(remote.sun_path, SOCK_PATH);
    len = strlen(SOCK_PATH) + sizeof(remote.sun_family);

#ifdef __APPLE__
    // There are only two hard things in computer science:
    // cache invalidation, naming things, and off-by-one errors.
    len += 1;
#endif

    if (connect(s, (struct sockaddr *)&remote, len) == -1)
        error(1, errno, "connect");

    puts("Connected.");

    while(printf("> "), fgets(dat, 100, stdin), !feof(stdin)) {
        if (send(s, dat, strlen(dat), 0) == -1)
            error(1, errno, "send");

        if ((t = recv(s, dat, 100, 0)) > 0) {
            dat[t] = '\0';
            printf("echo> %s", dat);
        } else {
            if (t < 0) {
                error(0, errno, "recv");
            }
            else {
                puts("Server closed connection");
            }

            exit(1);
        }
    }

    if (close(s) != 0)
        error(1, errno, "close");

    return 0;
}
