import chess
import copy

def alpha_beta(board, depth, alpha, beta):
	white_king_space, black_king_space = (0, 0), (0, 0)
	position = copy.deepcopy(board.board)

	for space in position.keys():
		if postion.get(space, LIMIT) != LIMIT and position[space].value == 500:
			if position[space].color == "White":
				white_king_space = space
			if position[space].color == "Black":
				black_king_space = space

	if (depth == 0 or (position[white_king_space].king_in_checkmate() or position[black_king_space].king_in_checkmate())):
		return (board.get_scores(), None, None)
	else:
		if board.player_turn == "White":
			move_piece = None
			best_move = None
			for space in position.keys():
				piece = position.get(space, LIMIT)
				if piece != LIMIT:
					new_position = copy.deepcopy(position)
					for move in piece.moves:
						new_position[move] = copy.deepcopy(piece)
						new_position[piece.location] = None
						new_board = copy.deepcopy(board)
						new_board.board = new_position
						score, move_piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
						if score > alpha: # White maximizes the score
							alpha = score
							best_move = move
							if alpha >= beta: # alpha beta cutoff
								break
			return (alpha, move_piece, best_move)
		elif board.player_turn == "Black":
			move_piece = None
			best_move = None
			for space in position.keys():
				piece = position.get(space, LIMIT)
				if piece != LIMIT:
					new_position = copy.deepcopy(position)
					for move in piece.moves:
						new_position[move] = copy.deepcopy(piece)
						new_position[piece.location] = None
						new_board = copy.deepcopy(board)
						new_board.board = new_position
						score, move_piece, move = alpha_beta(new_board, depth - 1, alpha, beta)
						if score < beta:
							beta = score
							best_move = move
							if alpha >= beta:
								break
			return (beta, move_piece, best_move)