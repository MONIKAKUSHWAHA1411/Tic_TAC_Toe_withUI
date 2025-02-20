import pytest
from tic_tac_toe_gui import TicTacToe

@pytest.fixture
def game():
    """Fixture to create a new game instance for each test."""
    return TicTacToe()

def test_initial_board_empty(game):
    """Test if the board is initialized empty."""
    assert all(cell == " " for row in game.board for cell in row)

def test_valid_move(game):
    """Test if a valid move updates the board."""
    game.make_move(0, 0)
    assert game.board[0][0] == "💖"

def test_invalid_move(game):
    """Test if making a move on an occupied space is invalid."""
    game.make_move(0, 0)
    result = game.make_move(0, 0)
    assert result == "Invalid move! Try again."

def test_winner_row(game):
    """Test if a player wins with a row."""
    game.make_move(0, 0)  # 💖
    game.make_move(1, 0)  # 💰
    game.make_move(0, 1)  # 💖
    game.make_move(1, 1)  # 💰
    result = game.make_move(0, 2)  # 💖 wins
    assert result == "Player 💖 wins!"

def test_winner_column(game):
    """Test if a player wins with a column."""
    game.make_move(0, 0)  # 💖
    game.make_move(0, 1)  # 💰
    game.make_move(1, 0)  # 💖
    game.make_move(1, 1)  # 💰
    result = game.make_move(2, 0)  # 💖 wins
    assert result == "Player 💖 wins!"

def test_winner_diagonal(game):
    """Test if a player wins with a diagonal."""
    game.make_move(0, 0)  # 💖
    game.make_move(0, 1)  # 💰
    game.make_move(1, 1)  # 💖
    game.make_move(0, 2)  # 💰
    result = game.make_move(2, 2)  # 💖 wins
    assert result == "Player 💖 wins!"

def test_draw(game):
    """Test if the game detects a draw."""
    moves = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 2), (2, 0)
    ]
    for i, (row, col) in enumerate(moves):
        result = game.make_move(row, col)
        if i < 8:
            assert result is None
        else:
            assert result == "It's a draw!"
