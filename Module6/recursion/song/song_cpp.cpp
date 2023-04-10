#include <unistd.h>
#include <iostream>
#include <string>
#include <sys/types.h>

# define DELAY_uS 1000


struct Letter {
    char c;
    Letter* next;

    Letter(char i) : c(i), next(nullptr) {};
};


Letter* circular_list(std::string s) {
    Letter *head = nullptr;
    Letter *f = nullptr;

    for (char c : s) {
        if (!head) {
            head = new Letter(c);
            f = head;
        }
        else {
            f->next = new Letter(c);
            f = f->next;
        }
    }

    f->next = head;
    return head;
}


void iterative(Letter *cl) {
    while (cl) {
        std::cout << cl->c << std::flush;
        usleep(DELAY_uS);
        cl = cl->next;
    }
}



void printer(char c) {
    (void)(std::cout << c << std::flush);
}


void recursive(Letter * cl) {
    usleep(DELAY_uS);

    /*********************************************************************
     * Spring 2021 UPDATE - This appears to be fixed in g++ (GCC) 10.3.0 *
     *********************************************************************/

    // using cout in this function causes a stack allocation
    // casting cout's return type to void didn't have an effect
    //     (void)(cout << cl->c << flush);
    // neither did putting the call to cout into its own scope.

    // To make this function tail-call optimized, comment out this line...
    std::cout << cl->c << std::flush;

    // And uncomment this line:
    // printer(cl->c);

    return recursive(cl->next);
}


std::string lyrics = "This is the song that never ends\n"
        "It just goes on and on my friends\n"
        "Some people started singing it, not knowing what it was\n"
        "And they'll continue singing it forever just because\n";


int main(int argc, __attribute__((unused))char* argv[]) {
    Letter *cl = circular_list(lyrics.c_str());

    std::cout << "This is the C++ version\n";

    if (argc == 1) {
        std::cout << "Singing recursively\n\n";
        usleep(1500000);
        recursive(cl);
    }
    else {
        std::cout << "Singing iteratively\n\n";
        usleep(1500000);
        iterative(cl);
    }

    return 0;
}
