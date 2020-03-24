import chess
import chess.pgn
import numpy as np


## import
def pulldata(n):
    pgn = open('data/ChessData_2014.pgn')
    X,y = [], []
    outcomes = {'1/2-1/2':0, '0-1':-1, '1-0':1}
    # Iterate through all games
    for i in range(n):
        game = chess.pgn.read_game(pgn)
        # Iterate through all moves and play them on a board.
        if game is None:
            print('Ended early after parsing {} games.'.format(int(i)))
            return X,np.asarray(y)
        board = game.board()
        iter = 0
        X_i,y_i = [], []
        for move in game.mainline_moves():
            board.push(move)
            result = 1
            boardstate = []
            ## read board state ##
            code = [True,False]
            for idx_squ in range(64):
                for col in range(2):
                    col_code = code[col]
                    for piece_code in range(1,7):
                        piece_idx = list(board.pieces(piece_code, col_code))
                        if idx_squ in piece_idx:
                            boardstate.append(1)
                        else:
                            boardstate.append(0)

            if iter == 0:
                X_i = np.array(boardstate, ndmin=2).T
            else:
                X_i = np.column_stack((X_i, np.array(boardstate)))
            result_i = outcomes[game.headers['Result']]
            y_i.append(result_i)
            # consider next move
            iter += 1
        ## postprocess data and append to output ##
        if i == 0:
            X = X_i
            y.extend(y_i)
        else:
            try:
                X = np.column_stack((X, X_i))
                y.extend(y_i)
            except:
                print('Error in game {} -> skipped.'.format(int(i)))
                print('So far: ',np.shape(X),np.shape(y))
                print('New: ',np.shape(X_i),np.shape(y_i))
        ## Logging ##
        if ((i+1)%1000) == 0:
            print('Has parsed {} games so far.'.format(int(i)))
            print('So far: ',np.shape(X),np.shape(y))
    print('Ended after parsing {} games.'.format(int(i)))
    return X,np.asarray(y)
def pullandstore(n):
    X,y = pulldata(n)
    np.savez_compressed('data/ChessData_2014_compressed.npz', a=X, b=y)
def load_training_data():
    with np.load('data/ChessData_2014_compressed.npz') as data:
        X = data['a']
        y = data['b']
    return X,y
