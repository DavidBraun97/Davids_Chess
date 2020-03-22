## cmd line chess engine using negated Minimax + quiescence search algorithm

# Instructions:
```
1) clone repository to your local machine
2) open cmd line and move to local directory: ...\Davids_Chess
2) run: python play.py
3) follow instructions in cmd line to choose settings
```

# Quiescence Search
> Quiescence Search is performed at the end of the main (negamax) search. The purpose of this search is to only evaluate "quiet" positions, or positions where there are no winning tactical moves to be made. This search is needed to avoid the horizon effect. Simply stopping your search when you reach the desired depth and then evaluate, is very dangerous. Consider the situation where the last move you consider is QxP. If you stop there and evaluate, you might think that you have won a pawn. But what if you were to search one move deeper and find that the next move is PxQ? You didn't win a pawn, you actually lost a queen. Hence the need to make sure that you are evaluating only quiescent (quiet) positions.

# For further information regarding chess engines and evaluation metrics refer to:
https://www.chessprogramming.org/
