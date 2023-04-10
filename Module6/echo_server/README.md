# Echo server and client written in C and Python

An **echo server** is a program that takes messages from a **client** program and sends them right back again.  These programs exhibit one approach to Inter-Process Communication (IPC).

I've adapted a simple echo server/client pair written by [Brian "Beej Jorgensen" Hall](https://beej.us/guide/bgipc/html/split/unixsock.html) in C and translated it directly into Python.  These two pairs of programs are identical in every detail, except for how they handle errors.  The C programs necessarily follow the *look before you leap* error handling philosophy while the Python programs employ exception handling and adhere to the *easier to ask forgiveness* school of thought.

Because both pairs of programs do exactly the same things, the Python server will happily converse with the C client, and vice-versa.  Indeed, the server neither knows nor cares which language its counterpart is written in.


## Running the demo on your own computer

The point of this demo is to learn something about different styles of writing code, and it is not actually necessary to build and run the programs to do this.  However, if you would like run these programs on your own, these instructions can help you get started.

*Note: These programs have been tested on Linux and Mac.  Because IPC is facilitated by the operating system of the computer the programs run on, it is difficult to write a program like this that will simultaneously work on Linux, Mac and Windows.  Windows users who install WSL may be able to run this demo.*

0.  Prepare your system to build C programs
    *   On Ubuntu-like Linux systems (Mint, Kubuntu, Xubuntu, etc.) install the **build-essential** package
        *   ```
            $ sudo apt update
            $ sudo apt install build-essential
            ```
    *   Mac users must install Xcode (if you're using Git, you should already have it)
1.  Compile the C source code into binary executables with `make`
    *   ```
        $ make
        cc -std=c11 -Wall -Wextra -ggdb -Wno-misleading-indentation    echoc.c   -o echoc
        cc -std=c11 -Wall -Wextra -ggdb -Wno-misleading-indentation    echos.c   -o echos
        ```
2.  In one terminal run the C server
    *   ```
        $ ./echos
        Waiting for a connection...
        ```
3.  Open another terminal to run the C client
    *   ```
        $ ./echoc
        Trying to connect...
        Connected.
        >
        ```
4.  Type text into the client
5.  Use `Ctrl-D` to make the client exit
    *   The server will await another connection
6.  Now, run the Python client
    *   ```
        $ python3 echoc.py
        Trying to connect...
        Connected.
        >
        ```
    *   Again, `Ctrl-D` exits the client
7.  Use `Ctrl-C` to exit the server
8.  Experiment!
    *   Try the above, but with the Python server
    *   What happens when
        *   ...a client is launched while no server is runnig?
        *   ...the server is killed while a client is connected?
        *   ...another server is started while one is already running?
        *   ...a second client is launched when one is already attached to the server?
        *   ...the `echo_socket` file is deleted while the server is running?
9.  Run `make clean` to remove temporary files created by building and running these programs


## Files

*   `Makefile` - Compiles the C files into native binary executables
*   `echos.c` - Echo server in C
*   `echoc.c` - Echo client in C
*   `echoc.py` - Echo server in Python
*   `echos.py` - Echo client in Python
*   `echo_socket` - A special file to facilitate IPC between server and client
    *   This file is treated specially by the OS.  You may need to delete it before you are allowed to remove or rename this folder.

*Updated Mon Apr 10 12:58:46 MDT 2023*
