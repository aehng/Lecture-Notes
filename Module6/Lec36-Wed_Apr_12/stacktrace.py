import time
import traceback


# Run this program in your shell with this long command:
# while python3 except.py; do echo "restarting except.py"; sleep 1; done
#
# Use `exit(1)` to break the loop and return to your shell

print("\033[1;32mReloaded except.py...\033[0m\n")

def one():
    two()

def two():
    three()

def three():
    four()

def four():
    five()

def five():
    my_repl()

def my_repl():
    while True:
        try:
            print(eval(input("Hit me with your best shot\n>>> ")))  # This is risky business right here
        except KeyboardInterrupt:
            print(" Interrupted")
            exit(0)
        except Exception as e:
            print(f"You got an error! {e}")
            traceback.print_stack()
        finally:
            print("finally: Just hang on half a sec...\n")
            time.sleep(.5)


# my_repl()
# How does the stack trace change if we don't directly invoke my_repl()?
one()
