#!/usr/bin/python3
"""Module to solve the N queens problem."""


from sys import argv, exit as status

if len(argv) != 2:
    print("Usage: nqueens N")
    status(1)
try:
    N = int(argv[1])
except ValueError:
    print("N must be a number")
    status(1)
if N < 4:
    print("N must be at least 4")
    status(1)

queens = [[i, -1] for i in range(N)]


def check_queen(queen):
    """Check if a queen is alredy in a position.

    Args:
        queen (int): queen position to check

    Returns:
        bool
    """
    for i in range(N):
        if queens[i][1] == queen:
            return True
    return False


def check_board(position, queen):
    """function thath check solution

    Args:
        position (int): current position.
        queen (int): current queen.

    Returns:
        bool
    """
    if check_queen(queen):
        return False
    i = 0
    while i < position:
        if abs(queens[i][1] - queen) == abs(i - position):
            return False
        i += 1
    return True


def solve_nq(queen):
    """Solves the N Queens using Backtracking.

    Args:
        queen (int): current queen.
    """
    for count in range(N):
        for i in range(queen, N):
            queens[i][1] = -1
        if check_board(queen, count):
            queens[queen][1] = count
            if queen == N - 1:
                print(queens)
            else:
                solve_nq(queen + 1)


if __name__ == '__main__':
    QUEEN = 0
    solve_nq(QUEEN)
