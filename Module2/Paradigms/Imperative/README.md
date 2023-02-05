# Imperative programming

*   [Imperative.py](./Imperative.py)
    FizzBuzz sequence in a simulated assembly language
*   [Asm/](./Asm)
    A Python module that mimics assembly language, including `goto`
    instructions.  For novelty purposes only.


This style is characterized through the step-by-step execution of instructions.

In its purest form, the fundamental unit of imperative code is the instruction.
The flow of the program ordinarily proceeds one instruction at a time from
top-to-bottom.  Computation occurs by executing instructions with
"side-effects" which change the state of CPU registers and memory locations.
However, some instructions (e.g. `goto` and `jump`) can change which
instruction will be executed next.  Syntactic loops and if/then/else are not
present in this paradigm.

Neither are named functions present; blocks of code called "subroutines" may be
`jump`ed into or out of, but there is no notion of passing arguments or
returning values.  Further, code may freely jump into the middle of a
subroutine without first executing any initialization code that may have been
present at the top of the subroutine.

Examples: Machine code, Assembly language, IBM's FORTRAN and FORTRAN II
