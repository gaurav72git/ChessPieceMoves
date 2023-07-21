from __future__ import annotations
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.get('/test')
def test_method():
    return f"THis is test method"

class ChessMoves(BaseModel):
    Pawn: str 
    Queen: str 
    King: str 
    Bishop: str 
    Knight: str 
    Rook: str 


def check_valid_moves_for_knight(board, row_pos, col_pos):
    valid_moves_for_knight = [
        [row_pos-1, col_pos-2],
        [row_pos+1, col_pos-2],
        [row_pos-1, col_pos+2],
        [row_pos+1, col_pos+2],
        [row_pos-2, col_pos-1],
        [row_pos+2, col_pos-1],
        [row_pos-2, col_pos+1],
        [row_pos+2, col_pos+1],
    ]

    move = []

    for value in valid_moves_for_knight:
        row_move = value[0]
        col_move = value[1]

        if row_move >= 1 and row_move <=8 and col_move >= 1 and col_move <= 8:
            if board[row_move][col_move] == 0:
                move_name = chr(row_move+64)
                move_name += str(col_move)
                move.append(move_name)

                
    return {
        "valid_moves": move
    }

def rook_moves(board, row_rook, col_rook):
    for r in board:
        for c in r:
            if c == col_rook:
                board[r][c] = 1
            if r == row_rook:
                board[r][c] = 1

def bishop_moves(board, row_bishop, col_bishop):
    pass

@app.post('/chess/knight')
def valid_moves_for_knight(positions: ChessMoves):
    queen_pos = positions.Queen
    rook_pos = positions.Rook
    knight_pos = positions.Knight
    bishop_pos = positions.Knight

    rows = 9
    cols = 9
    board = [[0]*cols]*rows
    
    row_queen = int(ord(queen_pos[0])-64)
    col_queen = int(queen_pos[1])
    row_rook = int(ord(rook_pos[0])-64)
    col_rook = int(rook_pos[1])
    row_knight = int(ord(knight_pos[0])-64)
    col_knight = int(knight_pos[1])
    row_bishop = int(ord(bishop_pos[0])-64)
    col_bishop = int(bishop_pos[1])

    board[row_queen][col_queen] = 1
    board[row_rook][col_rook] = 1
    board[row_knight][col_knight] = 1
    board[row_bishop][col_bishop] = 1

    rook_moves(board, row_rook, col_rook)
    bishop_moves(board, row_bishop, col_bishop)

    moves = check_valid_moves_for_knight(board, row_knight, col_knight)

    return moves
    
    
    
    
    


    

