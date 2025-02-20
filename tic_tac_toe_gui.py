import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        """Initialize the game logic."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.symbols = ["💖", "💰"]
        self.current_player = 0  # Index 0: 💖, Index 1: 💰
    
    def make_move(self, row, col):
        """Make a move and check the game status."""
        if self.board[row][col] == " ":
            self.board[row][col] = self.symbols[self.current_player]
            if self.check_winner():
                return f"Player {self.symbols[self.current_player]} wins!"
            elif self.is_draw():
                return "It's a draw!"
            self.current_player = 1 - self.current_player  # Switch player
            return None
        return "Invalid move! Try again."

    def check_winner(self):
        """Check if the current player has won."""
        sym = self.symbols[self.current_player]

        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == sym for j in range(3)):  # Rows
                return True
            if all(self.board[j][i] == sym for j in range(3)):  # Columns
                return True

        if all(self.board[i][i] == sym for i in range(3)) or \
           all(self.board[i][2 - i] == sym for i in range(3)):  # Diagonals
            return True

        return False

    def is_draw(self):
        """Check if the game is a draw (board is full)."""
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_game(self):
        """Reset the board for a new game."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0


class TicTacToeGUI:
    def __init__(self, root):
        """Initialize the GUI and game logic."""
        self.root = root
        self.root.title("Tic-Tac-Toe 💖 vs 💰")
        self.game = TicTacToe()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        """Create the 3x3 grid of buttons."""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=("Arial", 24),
                                               width=5, height=2, command=lambda r=i, c=j: self.on_click(r, c))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        """Handle a button click, update game logic, and refresh UI."""
        result = self.game.make_move(row, col)
        if result:
            self.update_ui()
            messagebox.showinfo("Game Over", result)
            self.reset_board()
        else:
            self.update_ui()

    def update_ui(self):
        """Update the button text to reflect the game state."""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.game.board[i][j])

    def reset_board(self):
        """Reset the board when the game ends."""
        self.game.reset_game()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
