# Python3 GOTO from https://github.com/snoack/python-goto
from Asm.goto import with_goto

registers = {
        'rax': 0,
        'rbx': 0,
        'rcx': 0,
        'rdx': 0,
        'rsx': "",
        }

flags = {
        'zero': False,
        }

strings = {}

rax, rbx, rcx, rdx = 'rax', 'rbx', 'rcx', 'rdx'
rsx = 'rsx'


def storstr(label, string):
    """Store the string data `string` at memory labeled `label`"""
    strings[label] = string


def loadstr(label):
    """Point RSX to the string stored at `label`"""
    registers[rsx] = strings[label]


def printstr():
    """Print the string stored in register RSX"""
    global registers
    print(registers['rsx'], end='')


def printi():
    """print value in RAX as an integer"""
    global registers
    print(registers['rax'], end='')


def printc():
    """print value in RAX as a character"""
    global registers
    print(chr(registers['rax']), end='')


def loadi(r, i):
    """loadi(r, i): Load into register r immediate value i"""
    global registers
    if isinstance(i, int):
        registers[r] = i
    else:
        raise TypeError(f"{__name__} expects an integer immediate")
    # Set the zero flag
    flags['zero'] = registers[r] == 0


def movr(a, b):
    """movr(a, b): Move register B into A"""
    global registers
    registers[a] = registers[b]
    flags['zero'] = registers[a] == 0


def add(r, i):
    """One instruction to deal with both immediates and registers
    add(r, i): add immediate value i to register r, store into r
    """
    global registers
    if isinstance(i, int):
        registers[r] += i
    elif __intregister(i):
        registers[r] += registers[i]
    else:
        raise TypeError(f"{__name__} expects two integer operands")
    flags['zero'] = registers[r] == 0


def addi(r, i):
    """addi(r, i): add immediate value i to register r, store into r"""
    global registers
    if isinstance(i, int):
        registers[r] += i
    else:
        raise TypeError(f"{__name__} expects an integer immediate")
    flags['zero'] = registers[r] == 0


def subi(r, i):
    """subi(r, i): subtract immediate value i from register r, store into r"""
    global registers
    if isinstance(i, int):
        registers[r] -= i
    else:
        raise TypeError(f"{__name__} expects an integer immediate")
    flags['zero'] = registers[r] == 0


def muli(r, i):
    """muli(r, i): multiply immediate value i to register r, store into r"""
    global registers
    if isinstance(i, int):
        registers[r] *= i
    else:
        raise TypeError(f"{__name__} expects an integer immediate")
    flags['zero'] = registers[r] == 0


# integer operations between int registers
def __intregister(r):
    return r in ('rax', 'rbx', 'rcx', 'rdx')


def addr(a, b):
    global registers
    if __intregister(a) and __intregister(b):
        registers[a] += registers[b]
    else:
        raise TypeError(f"{__name__} expects two integer registers")
    flags['zero'] = registers[a] == 0


def subr(a, b):
    global registers
    if __intregister(a) and __intregister(b):
        registers[a] -= registers[b]
    else:
        raise TypeError(f"{__name__} expects two integer registers")
    flags['zero'] = registers[a] == 0


def mulr(a, b):
    global registers
    if __intregister(a) and __intregister(b):
        registers[a] *= registers[b]
    else:
        raise TypeError(f"{__name__} expects two integer registers")
    flags['zero'] = registers[a] == 0


def modi(r, i):
    """modi(r, i): divide register r by immediate value i, store remainder into r"""
    registers[r] %= i
    flags['zero'] = registers[r] == 0


def modr(a, b):
    """modi(a, b): divide register a by register b, store remainder into a"""
    registers[a] %= registers[b]
    flags['zero'] = registers[a] == 0


def cmpi(r, i):
    global registers
    if __intregister(r):
        registers[r] -= i
        flags['zero'] = registers[r] == 0
    else:
        raise TypeError(f"{__name__} expects two integer registers")


def cmpr(a, b):
    global registers
    if __intregister(a) and __intregister(b):
        registers[a] -= registers[b]
        flags['zero'] = registers[a] == 0
    else:
        raise TypeError(f"{__name__} expects two integer registers")


def zeroflg():
    """zeroflg(): Return the value of the ZERO flag"""
    return flags['zero']
