from collections import defaultdict
import copy
LIMIT = "Out of bounds"
class Board(object):

	def __init__(self, position, player_turn = "White"):
		self.position = position
		self.player_turn = player_turn

	def __init__(self):
		self.position = {
			(0,0): Rook((0,0), 5, False, 'White', []),
			(0,1): Pawn((0,1), 1, False, 'White', [(0,2)]),
			(0,2): None,
			(0,3): None,
			(0,4): None,
			(0,5): None,
			(0,6): Pawn((0,6), -1, False, 'Black', [(0,5)]),
			(0,7): Rook((0,7), -5, False, 'Black', []),
			(1,0): Knight((1,0), 3, False, 'White', [(0,2), (2,2)]),
			(1,1): Pawn((1,1), 1, False, 'White', [(1,2)]),
			(1,2): None,
			(1,3): None,
			(1,4): None,
			(1,5): None,
			(1,6): Pawn((1,6), -1, False, 'Black', [(1,5)]),
			(1,7): Knight((1,7), -3, False, 'Black', [(0,5), (2,5)]),
			(2,0): Bishop((2,0), 3, False, 'White', []),
			(2,1): Pawn((2,1), 1, False, 'White', [(2,2)]),
			(2,2): None,
			(2,3): None,
			(2,4): None,
			(2,5): None,
			(2,6): Pawn((2,6), -1, False, 'Black', [(2,5)]),
			(2,7): Bishop((2,7), -3, False, 'Black', []),
			(3,0): Queen((3,0), 9, False, 'White', []),
			(3,1): Pawn((3,1), 1, False, 'White', [(3,2)]),
			(3,2): None,
			(3,3): None,
			(3,4): None,
			(3,5): None,
			(3,6): Pawn((3,6), -1, False, 'Black', [(3,5)]),
			(3,7): Queen((3,7), -9, False, 'Black', []),
			(4,0): King(False, False, (4,0), 500, False, 'White', []),
			(4,1): Pawn((4,1), 1, False, 'White', [(4,2)]),
			(4,2): None,
			(4,3): None,
			(4,4): None,
			(4,5): None,
			(4,6): Pawn((4,6), -1, False, 'Black', [(4,5)]),
			(4,7): King(False, False, (4,7), -500, False, 'Black', []),
			(5,0): Bishop((5,0), 3, False, 'White', []),
			(5,1): Pawn((5,1), 1, False, 'White', [(5,2)]),
			(5,2): None,
			(5,3): None,
			(5,4): None,
			(5,5): None,
			(5,6): Pawn((5,6), -1, False, 'Black', [(5,5)]),
			(5,7): Bishop((5,7), -3, False, 'Black', []),
			(6,0): Knight((6,0), 3, False, 'White', [(5,2), (7,2)]),
			(6,1): Pawn((6,1), 1, False, 'White', [(6,2)]),
			(6,2): None,
			(6,3): None,
			(6,4): None,
			(6,5): None,
			(6,6): Pawn((6,6), -1, False, 'Black', [(6,5)]),
			(6,7): Knight((6,7), -3, False, 'Black', [(5,5), (7,5)]),
			(7,0): Rook((7,0), 5, False, 'White', []),
			(7,1): Pawn((7,1), 1, False, 'White', [(7,2)]),
			(7,2): None,
			(7,3): None,
			(7,4): None,
			(7,5): None,
			(7,6): Pawn((7,6), -1, False, 'Black', [(7,5)]),
			(7,7): Rook((7,7), -5, False, 'Black', [])
		}
		self.player_turn = "White"

	#To make testing easier

	# Returns just the object's dictionary, not the whole object
	def clear_board(self):
		for key in self.position:
			self.position[key] = None
		return self.position

	def __getitem__(self,key):
		self.position.setdefault(key,LIMIT)
		return self.position[key]

	def __setitem__(self,key,value):
		self.position[key] = value

	def get_position(self):
		return self.position

	def get_score(self, color):
		piece_sum_value = 0
		for space in self.position:
			piece = self.position.get(space, LIMIT)
			if piece != LIMIT and piece.color == color:
				piece_sum_value += piece.value
		return piece_sum_value

	def get_scores(self):
		white_sum_value, black_sum_value = 0, 0
		for space in self.position:
			piece = self.position.get(space, LIMIT)
			if piece != LIMIT and piece != None:
				if piece.color == "White":
					white_sum_value += piece.value
				if piece.color == "Black":
					black_sum_value += piece.value
		return white_sum_value + black_sum_value

	def legal_moves(self):
		legal_moves = []
		for space in self.position:
			piece = self.position.get(space, LIMIT)
			if piece != LIMIT and piece != None:
				piece.moves = piece.calculate_moves(self.position)
				for move in piece.moves:
					legal_moves.append((piece, move))
		return legal_moves

	def legal_moves(self, color):
		legal_moves = []
		for space in self.position:
			piece = self.position.get(space, LIMIT)
			if piece != LIMIT and piece != None and piece.color == color:
				piece.moves = piece.calculate_moves(self.position)
				for move in piece.moves:
					legal_moves.append((piece, move))
		return legal_moves

	def king_locations(self):
		white_king_space, black_king_space = (), ()
		position = copy.deepcopy(self.position)

		# Finds the coordinate of both kings
		for space in position.keys():
			if position.get(space, LIMIT) != LIMIT and position.get(space) != None and (position.get(space, LIMIT).value == 500 or position.get(space, LIMIT).value == -500):
				if position[space].color == "White":
					white_king_space = space
				if position[space].color == "Black":
					black_king_space = space
		return (white_king_space, black_king_space)

class Piece(object):

	def __init__(self, location = None, value = None, has_moved = None, color = None, moves = []):
		self.location = location
		self.value = value
		self.has_moved = has_moved
		self.color = color
		self.moves = moves

	def calculate_moves(self, position):
		raise NotImplementedError("Calculate moves has not been implemented yet")

class King(Piece):

	def __init__(self, in_check = False, in_checkmate = False, *args):
		super(King, self).__init__(*args)
		self.in_check = in_check
		self.in_checkmate = in_checkmate

	def king_in_check(self, position):
		in_check = False
		enemy = "Black" if self.color == "White" else "White"
		for space in position.keys():
			piece = position.get(space, LIMIT)
			if piece != LIMIT and piece != None and self.location != piece.location and piece.value != 500 and piece.value != -500:
				piece.moves = piece.calculate_moves(position)
				if self.location in piece.moves and piece.color == enemy:
					in_check = True
		return in_check

	def king_in_checkmate(self, position):
		return self.king_in_check(position) and not self.calculate_moves(position)

	def calculate_moves(self, position):
		moves = []
		x,y = self.location[0], self.location[1]
		enemy = "Black" if self.color == "White" else "White"
		up, down, left, right = (x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)
		upper_left, upper_right, lower_right, lower_left = (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)

		next_board = copy.deepcopy(position)
		self_copy = copy.deepcopy(self)
		x2,y2 = self_copy.location[0], self_copy.location[1]
		if position.get(up, LIMIT) != LIMIT:
			if position[up] == None or position[up].color == enemy:
				self_copy.location = (x2, y2 + 1)
				next_board[up] = self_copy
				next_board[self.location] = None
				if not next_board[up].king_in_check(next_board):
					moves.append(up)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		if position.get(down, LIMIT) != LIMIT:
			if position[down] == None or position[down].color == enemy:
				self_copy.location = (x2, y2 - 1)
				next_board[down] = self_copy
				next_board[self.location] = None
				if not next_board[down].king_in_check(next_board):
					moves.append(down)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		if position.get(left, LIMIT) != LIMIT:
			if position[left] == None or position[left].color == enemy:
				self_copy.location = (x2 - 1, y2)
				next_board[left] = self_copy
				next_board[self.location] = None
				if not next_board[left].king_in_check(next_board):
					moves.append(left)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		if position.get(right, LIMIT) != LIMIT:
			if position[right] == None or position[right].color == enemy:
				self_copy.location = (x2 + 1, y2)
				next_board[right] = self_copy
				next_board[self.location] = None
				if not next_board[right].king_in_check(next_board):
					moves.append(right)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		if position.get(upper_left, LIMIT) != LIMIT:
			if position[upper_left] == None or position[upper_left] == enemy:
				self_copy.location = (x2 - 1, y2 + 1)
				next_board[upper_left] = self_copy
				next_board[self.location] = None
				if not next_board[upper_left].king_in_check(next_board):
					moves.append(upper_left)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		if position.get(upper_right, LIMIT) != LIMIT:
			if position[upper_right] == None or position[upper_right] == enemy:
				self_copy.location = (x2 + 1, y2 + 1)
				next_board[upper_right] = self_copy
				next_board[self.location] = None
				if not next_board[upper_right].king_in_check(next_board):
					moves.append(upper_right)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		if position.get(lower_right, LIMIT) != LIMIT:
			if position.get(lower_right, LIMIT) == None or position[lower_right] == enemy:
				self_copy.location = (x2 + 1, y2 - 1)
				next_board[lower_right] = self_copy
				next_board[self.location] = None
				if not next_board[lower_right].king_in_check(next_board):
					moves.append(lower_right)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		if position.get(lower_left, LIMIT) != LIMIT:
			if position[lower_left] == None or position[lower_left] == enemy:
				self_copy.location = (x2 - 1, y2 - 1)
				next_board[lower_left] = self_copy
				next_board[self.location] = None
				if not next_board[lower_left].king_in_check(next_board):
					moves.append(lower_left)
				next_board = copy.deepcopy(position)
				self_copy = copy.deepcopy(self)
		return moves

class Queen(Piece):

	def __init__(self, *args):
		super(Queen, self).__init__(*args)

	def calculate_moves(self, board):
		#Copied and pasted from rook
		x,y = self.location[0], self.location[1]
		moves = []
		enemy = "Black" if self.color == "White" else "White"
		up, down, left, right = False, False, False, False
		xcounter, ycounter = self.location[0], self.location[1]
		while not up:
			space = board.get((x,ycounter + 1), LIMIT)
			if space == None:
				ycounter += 1
				moves.append((x,ycounter))
			elif space != LIMIT and space.color == enemy:
				ycounter += 1
				moves.append((x,ycounter))
				up = True
			else:
				up = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not down:
			space = board.get((x,ycounter - 1), LIMIT)
			if space == None:
				ycounter -= 1
				moves.append((x,ycounter))
			elif space != LIMIT and space.color == enemy:
				ycounter -= 1
				moves.append((x,ycounter))
				down = True
			else:
				down = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not right:
			space = board.get((xcounter + 1,y), LIMIT)
			if space == None:
				xcounter += 1
				moves.append((xcounter,y))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				moves.append((xcounter,y))
				right = True
			else:
				right = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not left:
			space = board.get((xcounter - 1,y), LIMIT)
			if space == None:
				xcounter -= 1
				moves.append((xcounter,y))
			elif space != LIMIT and space.color == enemy:
				xcounter -= 1
				moves.append((xcounter,y))
				left = True
			else:
				left = True
		#copied from bishop
		x,y = self.location[0], self.location[1]
		enemy = "Black" if self.color == "White" else "White"
		xcounter, ycounter = self.location[0], self.location[1]
		upper_left, upper_right, lower_right, lower_left = False, False, False, False
		while not upper_left:
			space = board.get((xcounter - 1, ycounter + 1), LIMIT)
			if space == None:
				xcounter -= 1
				ycounter += 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
				upper_left = True
			else:
				upper_left = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not upper_right:
			space = board.get((xcounter + 1, ycounter + 1), LIMIT)
			if space == None:
				xcounter += 1
				ycounter += 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				ycounter += 1
				moves.append((xcounter, ycounter))
				upper_right = True
			else:
				upper_right = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not lower_right:
			space = board.get((xcounter + 1, ycounter - 1), LIMIT)
			if space == None:
				xcounter += 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
				lower_right = True
			else:
				lower_right = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not lower_left:
			space = board.get((xcounter - 1, ycounter - 1), LIMIT)
			if space == None:
				xcounter -= 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter -= 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
				lower_left = True
			else:
				lower_left = True
		return moves

class Rook(Piece):

	def __init__(self, *args):
		super(Rook, self).__init__(*args)

	def calculate_moves(self, board):
		x,y = self.location[0], self.location[1]
		moves = []
		enemy = "Black" if self.color == "White" else "White"
		up, down, left, right = False, False, False, False
		xcounter, ycounter = self.location[0], self.location[1]
		while not up:
			space = board.get((x,ycounter + 1), LIMIT)
			if space == None:
				ycounter += 1
				moves.append((x,ycounter))
			elif space != LIMIT and space.color == enemy:
				ycounter += 1
				moves.append((x,ycounter))
				up = True
			else:
				up = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not down:
			space = board.get((x,ycounter - 1), LIMIT)
			if space == None:
				ycounter -= 1
				moves.append((x,ycounter))
			elif space != LIMIT and space.color == enemy:
				ycounter -= 1
				moves.append((x,ycounter))
				down = True
			else:
				down = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not right:
			space = board.get((xcounter + 1,y), LIMIT)
			if space == None:
				xcounter += 1
				moves.append((xcounter,y))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				moves.append((xcounter,y))
				right = True
			else:
				right = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not left:
			space = board.get((xcounter - 1,y), LIMIT)
			if space == None:
				xcounter -= 1
				moves.append((xcounter,y))
			elif space != LIMIT and space.color == enemy:
				xcounter -= 1
				moves.append((xcounter,y))
				left = True
			else:
				left = True
		return moves


class Bishop(Piece):

	def __init__(self, *args):
		super(Bishop, self).__init__(*args)

	def calculate_moves(self, board):
		x,y = self.location[0], self.location[1]
		moves = []
		enemy = "Black" if self.color == "White" else "White"
		xcounter, ycounter = self.location[0], self.location[1]
		upper_left, upper_right, lower_right, lower_left = False, False, False, False
		while not upper_left:
			space = board.get((xcounter - 1, ycounter + 1), LIMIT)
			if space == None:
				xcounter -= 1
				ycounter += 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
				upper_left = True
			else:
				upper_left = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not upper_right:
			space = board.get((xcounter + 1, ycounter + 1), LIMIT)
			if space == None:
				xcounter += 1
				ycounter += 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				ycounter += 1
				moves.append((xcounter, ycounter))
				upper_right = True
			else:
				upper_right = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not lower_right:
			space = board.get((xcounter + 1, ycounter - 1), LIMIT)
			if space == None:
				xcounter += 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter += 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
				lower_right = True
			else:
				lower_right = True
		xcounter, ycounter = self.location[0], self.location[1]
		while not lower_left:
			space = board.get((xcounter - 1, ycounter - 1), LIMIT)
			if space == None:
				xcounter -= 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
			elif space != LIMIT and space.color == enemy:
				xcounter -= 1
				ycounter -= 1
				moves.append((xcounter, ycounter))
				lower_left = True
			else:
				lower_left = True
		return moves

class Knight(Piece):

	def __init__(self, *args):
		super(Knight, self).__init__(*args)

	def calculate_moves(self, position):
		x = self.location[0]
		y = self.location[1]
		moves = []
		enemy = "Black" if self.color == "White" else "White"
		spc1, spc2, spc3, spc4, spc5,spc6, spc7, spc8 = (x-2,y+1), (x+2, y-1), (x+1, y-2), (x-1, y+2), (x+2, y+1), (x+1, y+2), (x-2, y-1), (x-1, y-2) 
		if  position.get(spc1, LIMIT) != LIMIT:
			if position[spc1] == None or position[spc1].color == enemy:
				moves.append(spc1)
		if position.get(spc2, LIMIT) != LIMIT: 
			if position[spc2] == None or position[spc2].color == enemy:
				moves.append(spc2)
		if position.get(spc3, LIMIT) != LIMIT :
			if position[spc3] == None or position[spc3].color == enemy:
				moves.append(spc3)
		if position.get(spc4, LIMIT) != LIMIT:
			if position[spc4] == None or position[spc4].color == enemy:
				moves.append(spc4)
		if position.get(spc5, LIMIT) != LIMIT: 
			if position[spc5] == None or position[spc5].color == enemy:
				moves.append(spc5)
		if position.get(spc6, LIMIT) != LIMIT: 
			if position[spc6] == None or position[spc6].color == enemy:
				moves.append(spc6)
		if position.get(spc7, LIMIT) != LIMIT: 
			if position[spc7] == None or position[spc7].color == enemy:
				moves.append(spc7)
		if position.get(spc8, LIMIT) != LIMIT: 
			if position[spc8] == None or position[spc8].color == enemy:
				moves.append(spc8)
		return moves


class Pawn(Piece):

	def __init__(self, *args):
		super(Pawn, self).__init__(*args)

	def calculate_moves(self, position):
		x = self.location[0]
		y = self.location[1]
		moves = []
		# if ! self.has_moved:
		if self.color == "White":
			if position.get((x, y + 1), LIMIT) != LIMIT and position[(x, y + 1)] == None:
				moves.append((x, y + 1))
				if not self.has_moved and position.get((x, y + 2), LIMIT) != LIMIT and position[(x, y + 2)] == None:
					moves.append((x, y + 2))
			if position.get((x + 1, y + 1), LIMIT) != LIMIT and position[(x + 1, y + 1)] != None and position[(x + 1, y + 1)].color == "Black":
				moves.append((x + 1, y + 1))
			if position.get((x - 1, y + 1), LIMIT) != LIMIT and position[(x - 1, y + 1)] != None and position[(x - 1, y + 1)].color == "Black":
				moves.append((x - 1, y + 1))
		else:
			if position.get((x, y - 1), LIMIT) != LIMIT and position[(x, y - 1)] == None:
				moves.append((x , y - 1))
				if not self.has_moved and position.get((x, y - 2), LIMIT) != LIMIT and position[(x, y - 2)] == None:
					moves.append((x, y - 2))
			if position.get((x - 1, y - 1), LIMIT) != LIMIT and position[(x - 1, y - 1)] != None and position[(x - 1, y - 1)].color == "White":
				moves.append((x - 1, y - 1))
			if position.get((x + 1, y - 1), LIMIT) != LIMIT and position[(x + 1, y - 1)] != None and position[(x + 1, y - 1)].color == "White":
				moves.append((x + 1, y - 1))
		return moves