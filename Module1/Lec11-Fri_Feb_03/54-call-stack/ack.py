# it's global, so sue me
ACKS = 0

def ack(m, n):
    # count the number of times this function is called
    global ACKS
    ACKS += 1

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    else:
        print("Error: this is all wrong, I shouldn't be here")


print(ack(5, 0))
print(f"There were {ACKS} calls to ack() in this program")