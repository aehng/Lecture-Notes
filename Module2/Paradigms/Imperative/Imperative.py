#!/usr/bin/python3

# FizzBuzz in the Imperative style w/ goto.py
#
# This Python program goes to great lengths to emulate Assembly Language.
# It is *not* to be taken seriously!

from Asm.Asm import *


# Integer Registers
#   rax, rbx, rcx, rdx
#
# The String Register
#   rsx
#
# 
# Labels
# ======
# label .NAME - Name this point in the program NAME
# goto .NAME - Set instruction pointer to NAME
# 
# 
# Instructions
# ============
# storstr l, s | Store string `s` to memory at l
# loadstr l    | Point RSX to the string stored at l
# printstr     | Print the string stored in register RSX
# printi       | Print value in RAX as an integer
# printc       | Print value in RAX as a character
# loadi r, i   | Load into register r immediate value i
# movr a, b    | Move register B into A
# addi r, i    | add immediate value i to register r, store into r
# subi r, i    | subtract immediate value i from register r, store into r
# modi r, i    | compute the modulus r  % i, stores into r
# zeroflg      | check whether the last operation resulted in 0
# cmpi r, i    | compare value in register r with immediate i, sets zeroflg if equal


@with_goto
def __start():

    label .data

    # store string data in static area
    storstr('f', "Fizz")
    storstr('b', "Buzz")

    # The register RBX is used as our N value
    # Set N to 1
    loadi(rbx, 0x1)

    label .text

    goto .fizzBuzzLoop

    # The FIZZ subroutine
    # Input:  RBX = N
    # Output: RDX == 0 means that this number divides by 3
    label .fizz
    movr(rcx, rbx)
    modi(rcx, 0x3)
    if zeroflg():
        loadi(rdx, 0x1)
        loadstr('f')
        printstr()
    goto .fizzR

    # The BUZZ subroutine
    # Input:  RBX = N
    # Output: RDX == 1 means that this number divides by 5
    label .buzz
    movr(rcx, rbx)
    modi(rcx, 0x5)
    if zeroflg():
        loadi(rdx, 0x1)
        loadstr('b')
        printstr()
    goto .buzzR

    # Loop from 1 to 100, printing the FizzBuzz sequence line-by-line
    label .fizzBuzzLoop

    # RDX keeps track of whether a number has fizzed or buzzed
    # Reset it to Zero at the top of the main loop
    loadi(rdx, 0x0)

    # Call the Fizz routine and return
    goto .fizz
    label .fizzR

    # Call the Buzz routine and return
    goto .buzz
    label .buzzR

    # If N is neither Fizz nor Buzz, print it
    cmpi(rdx, 0x0)
    if zeroflg():
        movr(rax, rbx)
        printi()

    # Print a newline (ASCII char #10)
    loadi(rax, 0x0a)
    printc()

    # When N == 100 quit
    movr(rcx, rbx)
    subi(rcx, 0x64)
    if zeroflg():
        goto .end
    else:
        # Increment N
        addi(rbx, 0x1)
        goto .fizzBuzzLoop

    label .end


# Program Main Entry Point
__start()
