#!/bin/env python3


EXCEPTIONS = {}

def tally(exn):
    print(f"\n{exn}, that's exceptional!")
    if exn in EXCEPTIONS:
        EXCEPTIONS[exn] += 1
    else:
        EXCEPTIONS[exn] = 1

def report():
    print("Altogether you experienced the following symptoms")
    for exn in EXCEPTIONS:
        if EXCEPTIONS[exn] == 1:
            print(f"  {EXCEPTIONS[exn]:<3} instance of {exn}")
        else:
            print(f"  {EXCEPTIONS[exn]:<3} instances of {exn}")
    print("Ask your doctor if Exception Handling is right for you")


def main():
    """
    It would be nice if this REPL counted exceptions instead of crashing.
    The approved ways to quit are by running `exit()`, `sys.exit()` or
    pressing Ctrl-C.

    Design an exception handling scheme to fulfill these requirements, and
    which looks for these errors in particular:


    Refer to this document:
    https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    Hint: `exit()` closes STDIN.
    Hint: The open/closed state of a file is visible in its `.closed` attribute.
    """
    line = 1
    try:
        while True:
            try:
                # Here be Dragons
                exec(input(f"\n(one line only pls) [{line:<2}] >>> "))
            except ZeroDivisionError:
                tally(ZeroDivisionError)
            except ArithmeticError:
                tally(ArithmeticError)
            except SyntaxError:
                tally(SyntaxError)
            except ModuleNotFoundError:
                tally(ModuleNotFoundError)
            except EOFError:
                tally(EOFError)
            except FileExistsError:
                tally(FileExistsError)
            except FileNotFoundError:
                tally(FileNotFoundError)
            except IndexError:
                tally(IndexError)
            except LookupError:
                tally(LookupError)
            except OSError:
                tally(OSError)
            except RuntimeError:
                tally(RuntimeError)
            except TypeError:
                tally(TypeError)
            except ValueError:
                tally(ValueError)
            finally:
                print("finally, let's increment the line count")
                line += 1

    except KeyboardInterrupt:
        print("\nYou pressed ^C, goodbye")
    finally:
        report()


if __name__ == '__main__':
    main()
    print("we're done with main now")
