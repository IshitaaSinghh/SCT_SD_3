import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0  
                return False
    return True

def solve():
    board = []

    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, board[i][j])
        messagebox.showinfo("Success", "Sudoku Solved!")
    else:
        messagebox.showerror("Error", "No solution exists.")

root = tk.Tk()
root.title("Sudoku Solver - SkillCraft Technology")
root.geometry("400x450")

entries = []

for i in range(9):
    row = []
    for j in range(9):
        e = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
        e.grid(row=i, column=j, padx=3, pady=3)
        row.append(e)
    entries.append(row)

solve_button = tk.Button(root, text="Solve Sudoku", font=("Arial", 14), command=solve)
solve_button.grid(row=10, column=0, columnspan=9, pady=15)

root.mainloop()