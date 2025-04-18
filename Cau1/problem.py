import numpy as np
import os 

class Problem:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.zeros((self.board_size, self.board_size), dtype = int)

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            print(' '.join(map(str,row)).replace('0','-').replace('1','X').replace('2','O'))
        print()

    def is_valid_move(self, row, col):
        return self.board[row, col] == 0
    
    def make_move(self,row,col,player):
        if self.is_valid_move(row,col):
            self.board[row, col] = player
            return True
        return False
    
    def has_won(self, player):
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row,col] == player:
                    for direction in directions:
                        count = 1
                        for step in range(1,4):
                            new_row = row + direction[0] * step
                            new_col = col + direction[1] * step
                            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size and self.board[new_row, new_col] == player:
                                count += 1
                            else:
                                break
                        if count == 4:
                            return True
        return False
    
    def is_draw(self):
        return not np.any(self.board == 0)
