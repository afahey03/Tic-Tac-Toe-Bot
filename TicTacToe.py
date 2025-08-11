# Aidan Fahey
# 6/22/2025
# AI Tic-Tac-Toe game
# AI will always make the best move, either winning or forcing a draw.

import random

def PrintBoard(board): # Prints current board state

    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def CheckWinner(board): # Checks if winner or tie

    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    # Check for tie
    if " " not in board:
        return "Tie"
    
    return None

def Minimax(board, depth, isMaximizing, ai, user): # Minimax algorithm for AI moves

    winner = CheckWinner(board)
    
    if winner == ai:
        return 10 - depth
    elif winner == user:
        return depth - 10
    elif winner == "Tie":
        return 0
    
    if isMaximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = ai
                score = Minimax(board, depth + 1, False, ai, user)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = user
                score = Minimax(board, depth + 1, True, ai, user)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def AIMove(board, ai, user): # Determines best move for AI using Minimax

    best_score = -float('inf')
    best_move = None
    
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            score = Minimax(board, 0, False, ai, user)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move

def Main(): # Main game loop

    board = [" "] * 9
    print("\nWelcome to Tic-Tac-Toe against AI!\n")
    
    # Let the player choose X or O
    user = input("Choose X or O (or 'Quit'): ").upper()
    while user not in ["X", "O"]:
        if user.upper() == "QUIT":
            print("Thanks for playing! Goodbye!\n")
            return
        user = input("Please choose either X or O (or 'Quit'): ").upper()
        
    
    ai = "O" if user == "X" else "X"
    
    # Randomize who goes first
    currentPlayer = random.choice([user, ai])
    print(f"\n{currentPlayer} goes first!\n")
    
    while True:

        PrintBoard(board)
        
        if currentPlayer == user:
            # User turn
            while True:
                userInput = input(f"\nEnter your move (1-9, {user}) or 'Quit': ")
                if userInput.upper() == "QUIT":
                    print("Thanks for playing! Goodbye!\n")
                    return
                try:
                    move = int(userInput) - 1
                    if 0 <= move <= 8 and board[move] == " ":
                        print(f"You chose position {move + 1}\n")
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a number between 1 and 9 or 'Quit'")
        else:
            # AI turn
            print(f"\nAI ({ai}) is thinking...")
            move = AIMove(board, ai, user)
            print(f"AI chooses position {move + 1}\n")
        
        board[move] = currentPlayer
        
        winner = CheckWinner(board)
        if winner:
            PrintBoard(board)
            print()
            if winner == "Tie":
                print("It's a tie!")
                print()
            elif winner == user:
                print("Congratulations! You won!") # This will never happen, AI will always at least draw
                print()
            else:
                print("AI wins!")
                print()
            break
        
        # Switch players
        currentPlayer = ai if currentPlayer == user else user

if __name__ == "__main__":
    Main()