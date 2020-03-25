# Neural Network + Minimax Search - Chess Engine
## Overview:
This python built chess engine comprises of a classical negated Minimax search algorithm. Quiescence search is supported to avoid nodes at max depth that end in an unfavorable position (see below for explanation).

At each node, the current board state is evaluated.
Here two metrics are implemented:
1) static evaluation metric based on: https://www.chessprogramming.org/Simplified_Evaluation_Function
2) Neural Network prediction (trained on 10k+ chess games of players with more than 2000 elo)

This results in a deep learning enhanced evaluation metric which achieves a more humanlike chess play. 

## Further improvements:
1) revise net architecture & training (hyperparameter, training data..) Up until now: only training on 10000 games for 20 epochs... (use (multiple) GPUs) 
2) implement more efficient search algorithms and make use of move ordering (e.g. explore most promising moves first)

## Instructions:
```
1) clone repository to your local machine
2) open cmd line and move to local directory: ...\Davids_Chess
3) run: python play.py
4) follow instructions in cmd line to choose settings
```

## Quiescence Search
> Quiescence Search is performed at the end of the main (negamax) search. The purpose of this search is to only evaluate "quiet" positions, or positions where there are no winning tactical moves to be made. This search is needed to avoid the horizon effect. Simply stopping your search when you reach the desired depth and then evaluate, is very dangerous. Consider the situation where the last move you consider is QxP. If you stop there and evaluate, you might think that you have won a pawn. But what if you were to search one move deeper and find that the next move is PxQ? You didn't win a pawn, you actually lost a queen. Hence the need to make sure that you are evaluating only quiescent (quiet) positions.

## For further information regarding chess engines and evaluation metrics refer to:
https://www.chessprogramming.org/
## python-chess:
https://python-chess.readthedocs.io/en/latest/
## database
https://www.ficsgames.org/download.html
