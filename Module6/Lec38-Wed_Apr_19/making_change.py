import sys


USA = [25, 10, 5, 1]
EU = [50, 20, 10, 5, 2, 1]

def iChange(amount, coins):
    """Keep track of the largest coin we can use from our stack"""
    top = 0
    change = []
    while amount > 0:
        if amount >= coins[top]:
            amount -= coins[top]
            change += [coins[top]]
        else:
            while amount < coins[top]:
                top += 1  # We have to manually keep track of which coins to use
    return change


# What does the recursive solution look like?
# Use Anton's Big Recursive Idea to evolve it
def rChange(amount, coins):
    pass


# Make change for 87 cents by default,
# or take a number of cents from the command line
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    cents = int(sys.argv[1])
else:
    cents = 87


print(f"Change for {cents} cents ITERATIVELY = {iChange(cents, USA)}")
print(f"Change for {cents} cents RECURSIVELY = {rChange(cents, USA)}")
