class Letter {
    char c;
    Letter next;

    Letter(char c) {
        this.c = c;
        this.next = null;
    }

    void setNext(Letter l) {
        this.next = l;
    }
}


class CircularList {
    Letter head = null;

    CircularList(String letters) {
        Letter f = null;

        for (char c : letters.toCharArray()) {
            if (head == null) {
                head = new Letter(c);
                f = head;
            }
            else {
                Letter next = new Letter(c);
                f.setNext(next);
                f = next;
            }
        }

        // Tie the tail to the head to become circular
        f.setNext(head);
    }

    char getchar() {
        return this.head.c;
    }

    CircularList next() {
        this.head = this.head.next;
        return this;
    }
};



public class song {
    private static final int DELAY_MS = 1;

    private static String lyrics =  "This is the song that never ends\n"
        + "It just goes on and on my friends\n"
        + "Some people started singing it, not knowing what it was\n"
        + "And they'll continue singing it forever just because\n";


    static void iterative(CircularList cl) throws InterruptedException {
        while (true) {
            System.out.print(cl.getchar());
            cl.next();
            Thread.sleep(DELAY_MS);
        }
    }

    static void recursive(CircularList cl) throws InterruptedException {
            Thread.sleep(DELAY_MS);
            System.out.print(cl.getchar());
            recursive(cl.next());
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("This is the Java version");
        CircularList song = new CircularList(lyrics);

        if (args.length == 0) {
            System.out.println("Singing recursively\n");
            Thread.sleep(1500);
            recursive(song);
        }
        else {
            System.out.println("Singing iteratively\n");
            Thread.sleep(1500);
            iterative(song);
        }
    }
}
