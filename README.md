# Tic-Tac-Toe-MiniMax
This is a one file project that contains:
A tic tac toe game manager class runable in 9 lines of code like so:
```python
game = Game()
game.print_board()
while game.game_over is False:
    if game.players_turn == 1:
        prob, choice = minimax(game.board)
        game.turn(choice)
    else:
        x = input("Enter the space you would like to go 1-9(left to right, top to bottom):")
        game.turn(x)
```
And a MiniMax Algorithm that get's a list of moves
that are as good as eachother, 
then picks a random move, for (semi)random play.

The current running code gives information from the minimax algorithm including move choices.
