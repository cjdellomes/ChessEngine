import alpha_beta
import chess
import copy
import random
from collections import defaultdict

def greeting():
	name = "Pufferfish"
	description = "Dankest fish in the sea!"
	return ("Hello I am %s, the %s. \nYou go first!" % (name,description))

def calculate_move_easy (board):
	print("Random move made")
	random_dict = {}
	possible_keys = []
	for key in board.keys():
		if board[key] != chess.LIMIT and board[key] != None and board[key].color == "Black":
			possible_keys.append(key)
			random_dict[key] = board[key].calculate_moves(board)
	random_prev_key = possible_keys[random.randint(0, len(possible_keys) - 1)]
	rand_list = random_dict[random_prev_key]
	length_rand_list = len(rand_list)
	while length_rand_list == 0:
		random_prev_key = possible_keys[random.randint(0, len(possible_keys) - 1)]
		rand_list = random_dict[random_prev_key]
		length_rand_list = len(rand_list)
	random_new_move = rand_list[random.randint(0, length_rand_list - 1)]
	print("Possible moves I could have made: ")
	print(board[random_prev_key].calculate_moves(board))
	board[random_new_move] = board[random_prev_key]
	board[random_new_move].location = random_new_move
	board[random_new_move].has_moved = True
	board[random_prev_key] = None
	print("Moving " + str(random_prev_key) + " to " + str(random_new_move))
	return random_prev_key, random_new_move, board

def calculate_computer_move (board):
	this_board = chess.Board()
	this_board.position = board;
	best_score, best_piece, best_move = alpha_beta.alpha_beta(this_board, 2, -alpha_beta.infinite, alpha_beta.infinite)
	# If there is no discernable best move, make a random one
	if best_move == None:
		return calculate_move_easy(board)
	else:
		board[best_move] = copy.deepcopy(best_piece)
		board[best_move].has_moved = True
		board[best_piece.location] = None
		print("Moving " + str(best_piece.location) + " to " + str(best_move))
		return best_piece.location, best_move, board

def user_move (prev_coord,new_coord, board, user):
	print("Moving " + str (prev_coord) + " to " + str(new_coord))
	valid_move = True
	enemy = "Black" if user == "Human" else "White"
	if board[prev_coord] == None or board[prev_coord] == chess.LIMIT or board[prev_coord].color == enemy:
		if board[prev_coord] == None:
			print("You are attempting to move nothing")
		print("That is an illegal move")
		valid_move = False
	elif new_coord not in board[prev_coord].calculate_moves(board):
		print("That is an illegal move")
		print("The moves you can make are ")
		print(type(board[prev_coord]))
		print(board[prev_coord].calculate_moves(board))
		valid_move = False
	if valid_move:
		board[new_coord] = board[prev_coord]
		board[new_coord].location = new_coord
		board[new_coord].has_moved = True
		board[prev_coord] = None
	return board, valid_move

def calculate_letter (number):
	return chr(number + 97)


def main():
	print(greeting())
	board = chess.Board()
	position = board.get_position()
	position = defaultdict(lambda:chess.LIMIT, position)
	checkmate = False
	while not checkmate:
		valid_move = False
		while not valid_move:
			try:
				eval("1 if True else 2")
				prev_coord = input("What piece will you move? ")
				x = ord(prev_coord[0]) - 97
				y = int(prev_coord[1]) - 1
				new_coord = input("To what space? ")
				x2 = ord(new_coord[0]) - 97
				y2 = int(new_coord[1]) - 1
				position, valid_move = user_move((x,y),(x2,y2),position, "Human")
			except SyntaxError:
				# doesn't have ternary
				prev_coord = raw_input("What piece will you move? ")
				x = ord(prev_coord[0]) - 97
				y = int(prev_coord[1]) - 1
				new_coord = raw_input("To what space? ")
				x2 = ord(new_coord[0]) - 97
				y2 = int(new_coord[1]) - 1
				position, valid_move = user_move((x,y),(x2,y2),position, "Human")
		comp_prev_move, comp_new_move, position = calculate_computer_move(position)
		print(calculate_letter(comp_prev_move[0]) + str(comp_prev_move[1] + 1) + " to " + calculate_letter(comp_new_move[0]) + str(comp_new_move[1] + 1))
		checkmate_board = chess.Board()
		checkmate_board.position = copy.deepcopy(position)
		king_locations = checkmate_board.king_locations()
		checkmate = checkmate_board.position[king_locations[0]].king_in_checkmate(checkmate_board.position) or checkmate_board.position[king_locations[1]].king_in_checkmate(checkmate_board.position)

if __name__ == "__main__":
	main()