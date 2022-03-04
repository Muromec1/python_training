def print_square(width: int, height: int) -> None:
    separator = "*"
    print_full_row(width, separator)
    print_half_rows(width, height, separator)
    print_full_row(width, separator)

def print_full_row(width, separator):
    # felső oldal
    for i in range(0, width):
        print(separator, end="")
    print()

def print_half_rows(width: int, height: int, separator) -> None:
    for j in range(0, height - 2):
        print(separator, end="")
        for i in range(0, width - 2):
            print(" ", end="")
        print(separator)




print_square(10, 6)