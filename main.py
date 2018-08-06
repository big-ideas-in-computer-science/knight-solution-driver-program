#!/usr/bin/env python3
from sys import argv, exit
import experiment


def parameter_error_and_exit():
    """Print the correct argv parameter usage and exit"""
    print("Incorrect usage")
    print("Correct usage is {} n i j k ".format(argv[0]))
    print("""Where
\t- n is the size of the board
\t- i is the initial row coordinate of the knight
\t- j is the initial column coordinate of the knight
\t- k is the number of generations allowed for the algorithm""")
    exit(1)


def main():
    """Main function"""
    if len(argv) != 5:
        parameter_error_and_exit()
    
    try:
        board_size = int(argv[1])
        start_row = int(argv[2])
        start_col = int(argv[3])
        generation_max = int(argv[4])
    except(ValueError):
        parameter_error_and_exit()

    print("Running on a {0}x{0} board".format(board_size))
    print("With knight starting at ({},{})".format(start_row, start_col))
    print("and maximum generations allowed: {}".format(generation_max))

    best_path_found = experiment.run(board_size, start_row, start_col, generation_max)

    print("Output: {}".format(best_path_found))


if __name__ == "__main__":
    main()
