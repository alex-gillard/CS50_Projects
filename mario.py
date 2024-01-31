# TODO
from cs50 import get_int


# Creating block and gap variables
block = "#"
gap = " "


def main():
    # Prompt user for height of pyramid until input is properly received
    while True:
        size = get_int("Height: ")
        if size >= 1 and size <= 8:
            break
    # Loops which iteratively print blocks and gaps
    i = 0
    for i in range(size):
        for j in range(size - i - 1):
            print(gap, end="")
        for k in range(i + 1):
            print(block, end="")
        print()


main()
