# Namespace Collision Demo

Each of the Python files in this directory can be run as a stand-alone program **and** be imported into another program.

*   [main.py](./main.py)
*   [Beatles.py](./Beatles.py)
*   [Presidents.py](./Presidents.py)


When importing identifiers into the current namespace, you must be aware of collisions between *locally* defined identifiers and those defined in the *imported module*.

Run these programs to see what happens when identifiers are *clobbered* by definitions imported from other modules.  Change the code to try new things.  This is a Git repository; you can't break things permanently.  Run this command to restore the files to their original state:

```bash
$ git restore :/
```
