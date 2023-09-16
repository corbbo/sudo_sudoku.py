# sudo_sudoku.py -- A program to solve a sudoku puzzle
# Thiago Zilberknop, 16-09-2023

import time as t
import os
import random

def checkPlay(board, row, col, num):
    """
    Returns True if the attempted play is valid, False otherwise
    :param board: the sudoku board
    :param row: the row of the attempted move
    :param col: the column of the attempted move
    :param num: the number of the attempted move
    :return: boolean
    """
    
    # Check row for num
    for i in range(9):
        if (board[row][i] == num): return False
    
    # Check column for num
    for i in range(9):
        if (board[i][col] == num): return False
    
    # Check 3x3 squares for num
    xSquare = (row // 3) * 3 # Gets the first row of the 3x3 square
    ySquare = (col // 3) * 3 # Gets the first column of the 3x3 square
    
    for i in range(3):
        for j in range(3):
            if (board[xSquare + i][ySquare + j] == num): return False
            
    return True # No conflicts found, move is valid, returns True

def isEmpty(board, row, col):
    """
    Returns True if the cell is empty, False otherwise
    :param board: the sudoku board
    :param row: the row of the cell
    :param col: the column of the cell
    :return: boolean
    """
    if (board[row][col] == 0): return True
    else: return False
    
def findEmpty(board):
    """
    Returns the position of the first empty cell found
    :param board: the sudoku board
    :return: (row, col)
    """
    for row in range(9):
        for col in range(9):
            if (isEmpty(board, row, col)): return (row, col)
    
    return (-1, -1) # No empty cells found, returns (-1, -1)
def sudoSudoku(board, printflag):
    """
    Solves the sudoku board
    :param board: the sudoku board
    :return: boolean
    """
    row, col = findEmpty(board)                 # Finds the next empty cell
    if row == -1: return True                   # If no empty cells are found, the board is solved
    for num in range (1, 10):  
        if (printflag == True): printBoard(board)       # Prints new board state 
        if (checkPlay(board, row, col, num)):   # If the attempted play is valid
            board[row][col] = num               # Makes the play
            if (sudoSudoku(board, printflag)): return True # Begins checking the next empty cell recursively; for as long as the next move is valid, the function will keep calling itself until the board is solved
            else: board[row][col] = 0           # If the recursion fails at some point, the last attempted move is undone and the next number is tried (backtracking)
    return False                                # If no number works for the given cell, the board is unsolvable

def printBoard(board):
    """
    Prints the sudoku board
    :param board: the sudoku board
    :return: None
    """
    os.system("cls")    # Clears the screen so that the board is always printed at the same place so you can see the plays being made
    for row in range(9):
        if (row % 3 == 0 and row != 0): print("- - - - - - - - - - -")
        for col in range(9):
            if (col % 3 == 0 and col != 0): print("| ", end = "")
            if (board[row][col] == 0):
                print(" ", end = " ")
            else:
                print(board[row][col], end = " ")
        print()
        
def genBoard(board = []):
    """
    Generates a random sudoku board
    :return: board
    """
    if (board == []):
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0, 0]]
    
    for row in range(9):
        for col in range(9):
            num = random.randint(1, 9)
            if (checkPlay(board, row, col, num)): board[row][col] = num
            else:
                col -= 1
                if (col < 0):
                    col = 8
                    row -= 1
                if (row < 0): return genBoard()     # If the random board became unsolvable, starts generating again
                board[row][col] = 0
                
            
    return board
    
def main():
    choice = 0
    while (choice != "4"):
        board = genBoard()
        printBoard(board)
        print("[1] Solve this board\n[2] Solve this board printing every play (this will take significantly longer)\n[3] Generate another board\n[4] Exit")
        choice = input()
        time = t.time()
        if (choice == "1"):
            if (sudoSudoku(board, False)): printBoard(board)
            else: print("This board is unsolvable")
            print("Time elapsed: ", t.time() - time, " seconds")
            print("Generate another board? (y/n)")
            if (input() == "y"): continue
            else: return
        elif (choice == "2"):
            if (sudoSudoku(board, True)): printBoard(board)
            else: print("This board is unsolvable")
            print("Time elapsed: ", t.time() - time, " seconds")
            print("Generate another board? (y/n)")
            if (input() == "y"): continue
            else: return
        elif (choice == "3"):
            board = genBoard()
            printBoard(board)
            continue
        elif (choice == "4"): return
        else: print("Invalid choice")
            
main()