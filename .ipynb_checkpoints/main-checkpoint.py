import chess
import sys
import random
import chess.svg
import train
import chess.pgn

class State(object):
	def __init__(self, board = None):
		if board is None:
			self.board = chess.Board()
		else:
			self.board = board

	def expend_node(self):
		lst = []
		for moves in self.board.legal_moves:
			x = str(moves)
			self.board.push_uci(x)
			lst.append(self.board.copy())
			self.board.pop()
		return lst

if __name__ == "__main__":
	s = State()

pgn = open("data/db_2.pgn")

first_game = chess.pgn.read_game(pgn)
board1 = first_game.board()


for move in first_game.mainline_moves():
	board1.push(move)
	chess.svg.board(board1, size=350)
	print(board1)
	print()
	print()
