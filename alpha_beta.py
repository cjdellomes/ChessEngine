import chess
import copy
import time
import math
LIMIT = chess.LIMIT
infinite = float('inf')
counter = 0

def alpha_beta(board, depth, alpha, beta):
	# Uncomment this print to watch the function recurse
	# print((board, depth, alpha, beta))
	global counter
	counter += 1
	position = copy.deepcopy(board.position)
	white_king_space, black_king_space = board.king_locations()

	if (depth == 0 or (position[white_king_space].king_in_checkmate(position) or position[black_king_space].king_in_checkmate(position))):
		return (board.get_scores(), None, None)
	else:
		best_piece = None
		best_move = None
		if board.player_turn == "White":
			for piece_move_tuple in board.legal_moves("White"):
				tuple_piece = piece_move_tuple[0]
				tuple_move = piece_move_tuple[1]
				new_position = copy.deepcopy(position)
				new_position[tuple_piece] = copy.deepcopy(tuple_piece)
				new_position[tuple_piece.location] = None
				new_board = copy.deepcopy(board)
				new_board.board = new_position
				new_board.player_turn = "Black"
				score, piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
				if score > alpha:
					alpha = score
					best_piece = piece
					best_move = move
					if alpha >= beta:
						break
			return (alpha, best_piece, best_move)
		else:
			for piece_move_tuple in board.legal_moves("Black"):
				tuple_piece = piece_move_tuple[0]
				tuple_move = piece_move_tuple[1]
				new_position = copy.deepcopy(position)
				new_position[tuple_piece] = copy.deepcopy(tuple_piece)
				new_position[tuple_piece.location] = None
				new_board = copy.deepcopy(board)
				new_board.board = new_position
				new_board.player_turn = "White"
				score, piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
				if score > alpha:
					beta = score
					best_piece = piece
					best_move = move
					if alpha >= beta:
						break
			return (beta, best_piece, best_move)

def run_alpha_beta():
	start_time = time.time()
	board = chess.Board()

	print(alpha_beta(board, 2, -infinite, infinite))
	print(time.time() - start_time)
	print(counter)