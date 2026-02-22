import tkinter as tk
from tkinter import messagebox
import math

board = [" " for _ in range(9)]

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_full():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    buttons[move].config(text="O")

def player_move(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X")

        if check_winner("X"):
            messagebox.showinfo("Game Over", "You Win!")
            reset_game()
            return

        if is_full():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
            return

        best_move()

        if check_winner("O"):
            messagebox.showinfo("Game Over", "AI Wins!")
            reset_game()
            return

        if is_full():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()

root = tk.Tk()
root.title("Tic Tac Toe AI")

buttons = []

for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text= " ")
root.mainloop()
