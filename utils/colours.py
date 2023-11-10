RESET = "\033[0m"
BLACK = "\033[30;1m"
RED = "\033[31;1m"
GREEN = "\033[32;1m"
YELLOW = "\033[33;1m"
BLUE = "\033[34;1m"
PURPLE = "\033[35;1m"
CYAN = "\033[36;1m"
WHITE = "\033[37;1m"


def print_rainbow(*args):
    colors = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96]
    counter = 0
    for arg in args:
        arg = str(arg)
        for a in arg:
            c = colors[counter]
            counter += 1
            counter = counter % len(colors)
            print("\033[{};1m".format(c), end='')
            print(a, end='')
        print(end=' ')
    print("\033[0m")


def print_red(*args):
    print(RED, end='')
    print(*args, end='')
    print(RESET)


def print_blue(*args):
    print(BLUE, end='')
    print(*args, end='')
    print(RESET)


def print_yellow(*args):
    print(YELLOW, end='')
    print(*args, end='')
    print(RESET)


def print_green(*args):
    print(GREEN, end='')
    print(*args, end='')
    print(RESET)


if __name__ == "__main__":
    print_rainbow("Hello World! Hello World! Hello World!")
