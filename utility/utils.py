import chess
import random

## game class ##
class chess_game:
    def __init__(self,mode_flag):
        self.mode = mode_flag
        self.board = chess.Board()
    def play(self):
        while self.board.is_game_over() == False:
            if self.mode == 'human_vs_AI':
                # human's turn
                print(self.board)
                print(self.board.legal_moves)
                cmd_wrong = False
                while cmd_wrong == False:
                    try:
                        cmd = input("Make a move: ")
                        self.board.push_san(cmd)
                        cmd_wrong = True
                    except:
                        print('Illegal move! Try: ')
                        print(self.board.legal_moves)
                        time.sleep(1)                               # time to cancel
                print(self.board)
            else:
                # random AI's turn if not game_over
                if self.board.is_game_over() == False:
                    cmd_AI = random_agent(self.board)
                    self.board.push(cmd_AI)
            # AI's turn if not game_over
            if self.board.is_game_over() == False:
                #cmd_AI = random_agent(self.board)
                max, cmd_AI = minimax_agent(self.board,d=2)
                self.board.push(cmd_AI)
        self.endscreen()

    def endscreen(self):
        print(self.board)
        print(self.board.result())




## agents ##
def random_agent(board):
    """agent returns random, yet legal, chess move
    board is chess.py class
    """
    n_legal = board.legal_moves.count()
    random_pick = random.randint(0,n_legal-1)
    cmd = str(list(board.legal_moves)[random_pick])
    cmd_AI = chess.Move.from_uci(cmd)
    print('AI moves: ',cmd_AI)
    return cmd_AI

def minimax_agent(board,d):
    """agent returns legal move based on minimax algorithm with depth d
    board is chess.py class
    d is depth
    """
    max = -999999
    for move in list(board.legal_moves):
        board.push(chess.Move.from_uci(str(move)))
        #print(board)
        value_i = -negaMax(board,d-1)
        board.pop()
        #print('Global outcome: ', value_i)
        if value_i > max:
            max = value_i
            best_move = move
        #print('Current global best: ',max,best_move)
    print('AI moves: ',best_move)
    return max, chess.Move.from_uci(str(best_move))

## utility functions ##
def negaMax(board,d):
    """negated minmax algorithm with depth d
    board is chess.py class
    d is depth
    """
    max = -9999999
    if d == 0:
        #print('Value at bottom: ', evaluate_value(board))
        return evaluate_value(board)
    #print(board.legal_moves)
    for move in list(board.legal_moves):
        board.push(chess.Move.from_uci(str(move)))
        #print(board)
        value_i = -negaMax(board,d-1)
        board.pop()
        #print('outcome analysis: ', value_i)
        if value_i > max:
            max = value_i
            best_move = move
        #print('current best: ', max, best_move)
    return max


    return move_AI

def evaluate_value(board):
    """returns the expected value of a given board based on the
    "Simplified Evaluation Function" by Tomasz Michniewski

    board is chess.py class
    returns the expected value in [centipawns]
    """
    # piecewise values
    P = 100
    N = 320
    B = 330
    R = 500
    Q = 900
    K = 20000
    piece_value = [P,N,B,R,Q,K]
    # count active pieces of black
    pawns = len(board.pieces(chess.PAWN, chess.BLACK))
    knights = len(board.pieces(chess.KNIGHT, chess.BLACK))
    bishops = len(board.pieces(chess.BISHOP, chess.BLACK))
    rooks = len(board.pieces(chess.ROOK, chess.BLACK))
    queen = len(board.pieces(chess.QUEEN, chess.BLACK))
    king = len(board.pieces(chess.KING, chess.BLACK))
    piece_active_black = [pawns,knights,bishops,rooks,queen,king]
    # count active pieces of white
    pawns = len(board.pieces(chess.PAWN, chess.WHITE))
    knights = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bishops = len(board.pieces(chess.BISHOP, chess.WHITE))
    rooks = len(board.pieces(chess.ROOK, chess.WHITE))
    queen = len(board.pieces(chess.QUEEN, chess.WHITE))
    king = len(board.pieces(chess.KING, chess.WHITE))
    piece_active_white = [pawns,knights,bishops,rooks,queen,king]
    # calculate material value of board
    material_value_black = sum([a*b for a,b in zip(piece_active_black,piece_value)])
    material_value_white = sum([a*b for a,b in zip(piece_active_white,piece_value)])

    # PAWN
    pawntable = [
     0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5, -5,-10,  0,  0,-10, -5,  5,
    5, 10, 10,-20,-20, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0]
    # manipulate pawntable to match board.pieces indexing
    pawntable = pawntable[::-1]
    pawn_val = 0
    #evaluate white pawn position
    for i in board.pieces(chess.PAWN, chess.WHITE):
        pawn_val += pawntable[i]
    postion_value_white = pawn_val
    #evaluate black pawn position
    pawn_val = 0
    for i in board.pieces(chess.PAWN, chess.BLACK).mirror():
        pawn_val += pawntable[i]
    postion_value_black = pawn_val
    # BISHOP
    bishopstable = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -20,-10,-10,-10,-10,-10,-10,-20]
    # manipulate bishopstable to match board.pieces indexing
    bishopstable = bishopstable[::-1]
    bishop_val = 0
    #evaluate white bishop position
    for i in board.pieces(chess.BISHOP, chess.WHITE):
        bishop_val += bishopstable[i]
    postion_value_white += bishop_val
    #evaluate black bishop position
    bishop_val = 0
    for i in board.pieces(chess.BISHOP, chess.BLACK).mirror():
        bishop_val += bishopstable[i]
    postion_value_black += bishop_val
    # KNIGHT
    knightstable = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50]
    # manipulate knightstable to match board.pieces indexing
    knightstable = knightstable[::-1]
    knight_val = 0
    #evaluate white knight position
    for i in board.pieces(chess.KNIGHT, chess.WHITE):
        knight_val += knightstable[i]
    postion_value_white += knight_val
    #evaluate black knight position
    knight_val = 0
    for i in board.pieces(chess.KNIGHT, chess.BLACK).mirror():
        knight_val += knightstable[i]
    postion_value_black += knight_val
    # ROOK
    rookstable = [
     0,  0,  0,  0,  0,  0,  0,  0,
      5, 10, 10, 10, 10, 10, 10,  5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
      0,  0,  0,  5,  5,  0,  0,  0]
    # manipulate rookstable to match board.pieces indexing
    rookstable = rookstable[::-1]
    rook_val = 0
    #evaluate white rook position
    for i in board.pieces(chess.ROOK, chess.WHITE):
        rook_val += rookstable[i]
    postion_value_white += rook_val
    #evaluate black rook position
    rook_val = 0
    for i in board.pieces(chess.ROOK, chess.BLACK).mirror():
        rook_val += rookstable[i]
    postion_value_black += rook_val
    # QUEEN
    queenstable = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
     -5,  0,  5,  5,  5,  5,  0, -5,
      0,  0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20]
    # manipulate queenstable to match board.pieces indexing
    queenstable = queenstable[::-1]
    queen_val = 0
    #evaluate white queen position
    for i in board.pieces(chess.QUEEN, chess.WHITE):
        queen_val += queenstable[i]
    postion_value_white += queen_val
    #evaluate black queen position
    queen_val = 0
    for i in board.pieces(chess.QUEEN, chess.BLACK).mirror():
        queen_val += queenstable[i]
    postion_value_black += queen_val
    # KING
    kingstable = [
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -20,-30,-30,-40,-40,-30,-30,-20,
    -10,-20,-20,-20,-20,-20,-20,-10,
     20, 20,  0,  0,  0,  0, 20, 20,
     20, 30, 10,  0,  0, 10, 30, 20]
    # manipulate kingstable to match board.pieces indexing
    kingstable = kingstable[::-1]
    king_val = 0
    #evaluate white king position
    for i in board.pieces(chess.KING, chess.WHITE):
        king_val += kingstable[i]
    postion_value_white += king_val
    #evaluate black king position
    king_val = 0
    for i in board.pieces(chess.KING, chess.BLACK).mirror():
        king_val += kingstable[i]
    postion_value_black += king_val


    # calculate total value of board
    value = (material_value_white - material_value_black) + (postion_value_white - postion_value_black)
    if not board.turn:
        value = -value
    return value
