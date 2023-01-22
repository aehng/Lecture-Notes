# Namespace Collision Quiz

0.  Clone the lecture notes repository onto your computer
1.  Open a shell and navigate into the repository
2.  Open the quiz in Canvas and use your shell to find the answers
    *   Some questions are answered with the `grep` tool
    *   The rest can be answered by running the programs with Python, and editing the files

Each of the Python files in this directory can be run as a stand-alone program **and** be imported into another program.

*   [main.py](./main.py)
*   [Beatles.py](./Beatles.py)
*   [Presidents.py](./Presidents.py)


When importing identifiers into the current namespace, you must be aware of collisions between *locally* defined identifiers and those defined in the *imported module*.  This quiz teaches you the consequences of carelessly importing things into your programs.

Run these files to see what happens when identifiers are *clobbered* by definitions imported from other modules.  Change the code to fix bugs and to try new things.  Don't be scared.  This is a Git repository; it is hard to break!

When you are done, run this command to restore the files to their original state:

```bash
$ git restore :/
```
