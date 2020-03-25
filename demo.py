import chess
import numpy as np
from utility.NN_utils import *
from model import *

"""!This file is used for debugging and development!"""
## import
#pulldata(10000)
#
# model = NN()
# chess_model = model.load_model()
# board = chess.Board()
# print(board)
# X_test_b = preprocess_board(board)
# score = predict(chess_model,X_test_b)
# print("Score: {} .\n".format(score))
# for move in list(board.legal_moves):
#     board.push(chess.Move.from_uci(str(move)))
#     print(board)
#     X_test_b = preprocess_board(board)
#     score = model.predict(X_test_b)
#     print("Score: {} .".format(score))
#     board.pop()



# board.push_san('e4')
# board.push_san('e5')
# board.push_san('Nf3')
# board.push_san('Nc6')
# board.push_san('Bc4')
# board.push_san('Nf6')
# board.push_san('d3')
# board.push_san('Be7')
# board.push_san('Nc3')
# board.push_san('d6')
# board.push_san('h3')
# board.push_san('Na5')
# print(board)
# X_test_b = preprocess_board(board)
# X,y = load_training_data()
# n = len(y)
# print(np.shape(X),np.shape(y))
# X_test =  X[11:12,:]
# y_test = y[0,]
# print(X_test)
# print(y_test)
# print(np.shape(X_test),np.shape(y_test))
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# print(X_test_b)
# print(np.shape(X_test_b))
# score = model.predict(X_test_b)
# print("Score: {} .".format(score))
# print(X_test_b==X_test)
# model = NN()
# board = chess.Board()
#
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# board.push_san('e4')
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# board.push_san('e5')
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# board.push_san('Qh5')
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# board.push_san('Nc6')
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# board.push_san('Bc4')
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# board.push_san('Nf6')
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
#
# board.push_san('Qxf7')
# print(board)
# X_test = preprocess_board(board)
# score = model.predict(X_test)
# print("Score: {} .".format(score))
# print(X_test)
# print(np.shape(X_test))
