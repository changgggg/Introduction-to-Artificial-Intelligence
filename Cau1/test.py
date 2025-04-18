from search_strategy import SearchStrategy
from problem import Problem

game = Problem(8)
strategy = SearchStrategy(game, 4)
player_turn = True

while True: 
    game.print_board()
    if player_turn:
        row, col = map(int, input("Enter your move ( row , col):").split())
        if game.make_move(row, col, 1):
            if game.has_won(1):
                game.print_board()
                print('Player win')
                break
            player_turn = False
    
    else:
        row, col = strategy.get_best_move()
        if row != -1:
            game.make_move(row,col,2)
            if game.has_won(2):
                game.print_board()
                print("Computer win")
                break
            player_turn = True

    if game.is_draw():
        game.print_board()
        print("draw")
        break
