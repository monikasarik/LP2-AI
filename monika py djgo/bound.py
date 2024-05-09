class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.row_attacked = [False] * n
        self.upper_diag_attacked = [False] * (2*n - 1)
        self.lower_diag_attacked = [False] * (2*n - 1)
        self.solutions = []

    def is_safe(self, row, col):
        return not self.row_attacked[row] and not self.upper_diag_attacked[row + col] and not self.lower_diag_attacked[row - col + self.n - 1]

    def solve_n_queens(self, col):
        if col == self.n:
            # Convert board to a printable solution
            solution = [''.join('Q' if cell == 1 else '.' for cell in row) for row in self.board]
            self.solutions.append(solution)
            return True

        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.row_attacked[row] = True
                self.upper_diag_attacked[row + col] = True
                self.lower_diag_attacked[row - col + self.n - 1] = True

                if self.solve_n_queens(col + 1):
                    return True

                self.board[row][col] = 0
                self.row_attacked[row] = False
                self.upper_diag_attacked[row + col] = False
                self.lower_diag_attacked[row - col + self.n - 1] = False

        return False

    def find_solutions(self):
        self.solve_n_queens(0)
        return self.solutions

def print_solutions(solutions):
    if solutions:
        print(f"Found {len(solutions)} solutions:")
        for idx, solution in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            for row in solution:
                print(row)
            print()
    else:
        print("No solutions found.")

if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard (n x n): "))
    n_queens = NQueens(n)
    solutions = n_queens.find_solutions()
    print_solutions(solutions)
