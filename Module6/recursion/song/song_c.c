#define _XOPEN_SOURCE 500
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>

# define DELAY_uS 1000


struct Letter {
    char c;
    struct Letter* next;
};
typedef struct Letter Letter;


Letter* circular_list(char *s) {
    Letter *head = NULL;
    Letter *f = NULL;

    size_t len = strlen(s);
    for (int i = 0; i < len; ++i) {
        if (!head) {
            head = malloc(sizeof(Letter));
            f = head;
        }
        else {
            f->next = malloc(sizeof(Letter));
            f = f->next;
        }
        f->c = s[i];
        f->next = NULL;
    }

    f->next = head;
    return head;
}


void iterative(Letter *cl) {
    while (cl) {
        printf("%c", cl->c);
        fflush(stdout);
        usleep(DELAY_uS);
        cl = cl->next;
    }
}


void recursive(Letter *cl) {
    printf("%c", cl->c);
    fflush(stdout);
    usleep(DELAY_uS);
    return recursive(cl->next);
}


char* lyrics =  "This is the song that never ends\n"
        "It just goes on and on my friends\n"
        "Some people started singing it, not knowing what it was\n"
        "And they'll continue singing it forever just because\n";


int main(int argc, __attribute__((unused))char* argv[]) {
    Letter *cl = circular_list(lyrics);

    puts("This is the C version");

    if (argc == 1) {
        puts("Singing recursively\n");
        usleep(1500000);
        recursive(cl);
    }
    else {
        puts("Singing iteratively\n");
        usleep(1500000);
        iterative(cl);
    }

    return 0;
}
