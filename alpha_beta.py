import chess
import copy
import time
import math
LIMIT = chess.LIMIT
infinite = math.inf
counter = 0

def alpha_beta(board, depth, alpha, beta):
	print((board, depth, alpha, beta))
	global counter
	counter += 1
	white_king_space, black_king_space = (), ()
	position = copy.deepcopy(board.board)

	# Finds the coordinate of both kings
	for space in position.keys():
		if position.get(space, LIMIT) != LIMIT and position.get(space) != None and (position.get(space, LIMIT).value == 500 or position.get(space, LIMIT).value == -500):
			if position[space].color == "White":
				white_king_space = space
			if position[space].color == "Black":
				black_king_space = space

	if (depth == 0 or (position[white_king_space].king_in_checkmate(position) or position[black_king_space].king_in_checkmate(position))):
		return (board.get_scores(), None, None)
	else:
		if board.player_turn == "White":
			move_piece = None
			best_move = None
			for piece_move_tuple in board.legal_moves():
				piece = piece_move_tuple[0]
				move = piece_move_tuple[1]
				new_position = copy.deepcopy(position)
				new_position[piece] = copy.deepcopy(piece)
				new_position[piece.location] = None
				new_board = copy.deepcopy(board)
				new_board.board = new_position
				new_board.player_turn = "Black"
				score, move_piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
				if score > alpha:
					alpha = score
					best_move = move
					if alpha >= beta:
						break
			return (alpha, move_piece, best_move)
		elif board.player_turn == "Black":
			move_piece = None
			best_move = None
			for piece_move_tuple in board.legal_moves():
				piece = piece_move_tuple[0]
				move = piece_move_tuple[1]
				new_position = copy.deepcopy(position)
				new_position[piece] = copy.deepcopy(piece)
				new_position[piece.location] = None
				new_board = copy.deepcopy(board)
				new_board.board = new_position
				new_board.player_turn = "White"
				score, move_piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
				if score > alpha:
					beta = score
					best_move = move
					if alpha >= beta:
						break
			return (beta, move_piece, best_move)

		# if board.player_turn == "White":
		# 	move_piece = None
		# 	best_move = None
		# 	for space in position.keys():
		# 		piece = position.get(space, LIMIT)
		# 		print('piece: ' + str(piece))
		# 		if piece != LIMIT and piece != None:
		# 			new_position = copy.deepcopy(position)
		# 			for move in piece.moves:
		# 				print('move: ' + str(move))
		# 				new_position[move] = copy.deepcopy(piece)
		# 				new_position[piece.location] = None
		# 				new_board = copy.deepcopy(board)
		# 				new_board.board = new_position
		# 				new_board.player_turn = "Black"
		# 				score, move_piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
		# 				if score > alpha: # White maximizes the score
		# 					alpha = score
		# 					best_move = move
		# 					if alpha >= beta: # alpha beta cutoff
		# 						break
		# 	return (alpha, move_piece, best_move)
		# elif board.player_turn == "Black":
		# 	move_piece = None
		# 	best_move = None
		# 	for space in position.keys():
		# 		piece = position.get(space, LIMIT)
		# 		print('space: ' + str(piece))
		# 		if piece != LIMIT and piece != None:
		# 			new_position = copy.deepcopy(position)
		# 			for move in piece.moves:
		# 				print('move: ' + str(move))
		# 				new_position[move] = copy.deepcopy(piece)
		# 				new_position[piece.location] = None
		# 				new_board = copy.deepcopy(board)
		# 				new_board.board = new_position
		# 				new_board.player_turn = "White"
		# 				score, move_piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
		# 				if score < beta: # Black minimizes the score
		# 					beta = score
		# 					best_move = move
		# 					if alpha >= beta: # alpha beta cutoff
		# 						break
		# 	return (beta, move_piece, best_move)

def run_alpha_beta():
	start_time = time.time()
	board = chess.Board()

	print(alpha_beta(board, 3, -infinite, infinite))
	print(time.time() - start_time)
	print(counter)

run_alpha_beta()