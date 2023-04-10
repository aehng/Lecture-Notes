# Using watcher.sh

    Usage: watcher.sh PROGRAM_NAME [iteratively]


`watcher.sh` will run a program in the background and launch a new instance of
the Terminology terminal which runs the script `proc_vm_watcher.sh` to watch
memory use of the background process.  If you don't have the Terminology
terminal you can edit `watcher.sh` to make it spawn a different terminal
instead.

Once you've seen enough press ENTER in `watcher.sh`'s window to terminate the
backgrounded process.


# Expected program behaviors:

*   **song.py**
    *   Not Tail-Call Optimized (TCO)
    *   Crashes very quickly, though this can be overcome by running
        `sys.setrecursionlimit(20000)`
    *   VmStk grows *very* rapidly
*   **song.class**
    *   Not TCO
    *   Crashes after a while, but takes longer than Python
    *   Curiously, VmStk doesn't grow at all in Java8; this JVM must manage its
        call stack on the heap
*   **song_c**
    *   TCO
    *   Very low memory requirements overall
*   **song_cpp**
    *   Not TCO in its present form with g++ (GCC) 9.3.0
    *   Not TCO in its present form with clang version 10.0.0 
    *   But if you rewrite one small part it *IS* TCO
*   **song_scm**
    *   TCO; Scheme requires implementations to be TCO since iteration doesn't
        exist in this language
*   **song_scm.scm**
    *   TCO, even when run as an interpreted script
