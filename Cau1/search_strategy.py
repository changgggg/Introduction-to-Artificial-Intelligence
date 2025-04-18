from problem import Problem

class SearchStrategy:
    def __init__(self, problem, search_depth):
        self.problem = problem
        self.search_depth = search_depth

    def alpha_beta_search(self, depth, alpha, beta, maximizing_player):
        if self.problem.has_won(1):
            return -10
        if self.problem.has_won(2):
            return 10
        if self.problem.is_draw() or depth == 0:
            return 0
        
        if maximizing_player:
            max_eval = -float('inf')
            for row in range(self.problem.board_size):
                for col in range(self.problem.board_size):
                    if self.problem.is_valid_move(row, col):
                            self.problem.board[row,col] = 2
                            eval = self.alpha_beta_search(depth - 1, alpha, beta, False)
                            self.problem.board[row, col] = 0
                            max_eval = max(max_eval,eval)
                            alpha = max(alpha, eval)
                            if beta <= alpha:
                                break
            return max_eval
        else:
            min_eval = float('inf')
            for row in range(self.problem.board_size):
                for col in range(self.problem.board_size):
                    if self.problem.is_valid_move(row, col):
                        self.problem.board[row, col] = 1
                        eval = self.alpha_beta_search(depth-1,alpha, beta, True)
                        self.problem.board[row, col] = 0
                        min_eval = min(min_eval, eval)
                        beta = min (beta, eval)
                        if beta <= alpha:
                            break
            return min_eval
    
    def get_best_move(self):
        best_val = -float('inf')
        best_move = (-1,-1)
        for row in range(self.problem.board_size):
            for col in range(self.problem.board_size):
                if self.problem.is_valid_move(row,col):
                    self.problem.board[row, col] = 2
                    move_val = self.alpha_beta_search(self.search_depth, -float('inf'), -float('inf'), False)
                    self.problem.board[row, col] = 0
                    if move_val > best_val:
                        best_move = (row, col)
                        best_val = move_val
        
        return best_move
