import pygame
import time
from boardStart import bo

#starting board

def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board, number, position):

    #Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    #Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3 
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == number and (i, j) != position:
                return False

    return True

def print_board(board):
    #solves a sudoku board using backtracking

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if bo[i][j] == 0:   #empty - 0
                return (i, j) #row, col

    return None

print_board(bo)
solve(bo)
print("            ")
print_board(bo)