#!/usr/bin/python3
"""
N queens module
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed at board[row][col]
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(board, row, N, solutions):
    """
    Recursive utility function to find all solutions to the N Queens problem.

    Parameters:
    - board: List representing the current state of the chessboard
    - row: Current row being considered
    - N: Size of the chessboard
    - solutions: List to store all found solutions
    """
    if row == N:
        # Found a solution, add to solutions list
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve_nqueens_util(board, row + 1, N, solutions)


def solve_nqueens(N):
    """
    Solves the N Queens problem and prints the solutions.

    Parameters:
    - N: Size of the chessboard
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
