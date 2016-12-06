from collections import defaultdict
import copy
LIMIT = "Out of bounds"
class Board:

	def __init__(self, board):
		self.board = board

	def __init__(self):
		self.board = {
			(0,0): Rook((0,0), 5, False, 'White', []),
			(0,1): Pawn((0,1), 1, False, 'White', [(0,2)]),
			(0,2): None,
			(0,3): None,
			(0,4): None,
			(0,5): None,
			(0,6): Pawn((0,6), 1, False, 'Black', [(0,5)]),
			(0,7): Rook((0,7), 5, False, 'Black', []),
			(1,0): Knight((1,0), 3, False, 'White', [(0,2), (2,2)]),
			(1,1): Pawn((1,1), 1, False, 'White', [(1,2)]),
			(1,2): None,
			(1,3): None,
			(1,4): None,
			(1,5): None,
			(1,6): Pawn((1,6), 1, False, 'Black', [(1,5)]),
			(1,7): Knight((1,7), 3, False, 'Black', [(0,5), (2,5)]),
			(2,0): Bishop((2,0), 3, False, 'Black', []),
			(2,1): Pawn((2,1), 1, False, 'Black', [(2,2)]),
			(2,2): None,
			(2,3): None,
			(2,4): None,
			(2,5): None,
			(2,6): Pawn((2,6), 1, False, 'Black', [(2,5)]),
			(2,7): Bishop((2,7), 3, False, 'Black', []),
			(3,0): Queen((3,0), 9, False, 'White', []),
			(3,1): Pawn((3,1), 1, False, 'White', [(3,2)]),
			(3,2): None,
			(3,3): None,
			(3,4): None,
			(3,5): None,
			(3,6): Pawn((3,6), 1, False, 'Black', [(3,5)]),
			(3,7): Queen((3,7), 1, False, 'Black', []),
			(4,0): King(False, False, (4,0), 500, False, 'White', []),
			(4,1): Pawn((4,1), 1, False, 'White', [(4,2)]),
			(4,2): None,
			(4,3): None,
			(4,4): None,
			(4,5): None,
			(4,6): Pawn((4,6), 1, False, 'Black', [(4,5)]),
			(4,7): King(False, False, (4,7), 1, False, 'Black', []),
			(5,0): Bishop((5,0), 3, False, 'White', []),
			(5,1): Pawn((5,1), 1, False, 'White', [(5,2)]),
			(5,2): None,
			(5,3): None,
			(5,4): None,
			(5,5): None,
			(5,6): Pawn((5,6), 1, False, 'Black', [(5,5)]),
			(5,7): Bishop((5,7), 1, False, 'Black', []),
			(6,0): Knight((6,0), 3, False, 'White', [(5,2), (7,2)]),
			(6,1): Pawn((6,1), 1, False, 'White', [(6,2)]),
			(6,2): None,
			(6,3): None,
			(6,4): None,
			(6,5): None,
			(6,6): Pawn((6,6), 1, False, 'Black', [(6,5)]),
			(6,7): Knight((6,7), 1, False, 'Black', [(5,5), (7,5)]),
			(7,0): Rook((7,0), 6, False, 'White', []),
			(7,1): Pawn((7,1), 1, False, 'White', [(7,2)]),
			(7,2): None,
			(7,3): None,
			(7,4): None,
			(7,5): None,
			(7,6): Pawn((7,6), 1, False, 'Black', [(7,5)]),
			(7,7): Rook((7,7), 6, False, 'Black', [])
		}

	#To make testing easier
	def clear_board(self):
		for key in self.board:
			self.board[key] = None
		return self.board

	def __getitem__(self,key):
		self.board.setdefault(key,LIMIT)
		return self.board[key]

	def __setitem__(self,key,value):
		self.board[key] = value

class Piece(object):

	def __init__(self, location = None, value = None, has_moved = None, color = None, moves = []):
		self.location = location
		self.value = value
		self.has_moved = has_moved
		self.color = color
		self.moves = moves

class King(Piece):

	def __init__(self, in_check = False, in_checkmate = False, *args):
		super(King, self).__init__(*args)
		self.in_check = in_check
		self.in_checkmate = in_checkmate

	def king_in_check(self, board):
		in_check = False
		enemy = "Black" if self.color == "White" else "White"
		for space in board:
			piece = board[space]
			if piece != None and self.location != piece.location:
				if self.location in piece.moves and piece.color == enemy:
					in_check = True
		return in_check

	def king_in_checkmate(self, board):
		return self.king_in_check(board) and not self.calculate_moves(board)

	def calculate_moves(self, board):
		moves = []
		x,y = self.location[0], self.location[1]
		enemy = "Black" if self.color == "White" else "White"
		up, down, left, right = (x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)
		upper_left, upper_right, lower_right, lower_left = (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)

		next_board = copy.deepcopy(board)
		self_copy = copy.deepcopy(self)
		x2,y2 = self_copy.location[0], self_copy.location[1]

		if board[up] == None or board[up].color == enemy:
			self_copy.location = (x2, y2 + 1)
			next_board[up] = self_copy
			next_board[self.location] = None
			if not next_board[up].king_in_check(next_board):
				moves.append(up)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		if board[down] == None or board[down].color == enemy:
			self_copy.location = (x2, y2 - 1)
			next_board[down] = self_copy
			next_board[self.location] = None
			if not next_board[down].king_in_check(next_board):
				moves.append(down)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		if board[left] == None or board[left].color == enemy:
			self_copy.location = (x2 - 1, y2)
			next_board[left] = self_copy
			next_board[self.location] = None
			if not next_board[left].king_in_check(next_board):
				moves.append(left)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		if board[right] == None or board[right].color == enemy:
			self_copy.location = (x2 + 1, y2)
			next_board[right] = self_copy
			next_board[self.location] = None
			if not next_board[right].king_in_check(next_board):
				moves.append(right)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		if board[upper_left] == None or board[upper_left] == enemy:
			self_copy.location = (x2 - 1, y2 + 1)
			next_board[upper_left] = self_copy
			next_board[self.location] = None
			if not next_board[upper_left].king_in_check(next_board):
				moves.append(upper_left)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		if board[upper_right] == None or board[upper_right] == enemy:
			self_copy.location = (x2 + 1, y2 + 1)
			next_board[upper_right] = self_copy
			next_board[self.location] = None
			if not next_board[upper_right].king_in_check(next_board):
				moves.append(upper_right)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		if board[lower_right] == None or board[lower_right] == enemy:
			self_copy.location = (x2 + 1, y2 - 1)
			next_board[lower_right] = self_copy
			next_board[self.location] = None
			if not next_board[lower_right].king_in_check(next_board):
				moves.append(lower_right)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		if board[lower_left] == None or board[lower_left] == enemy:
			self_copy.location = (x2 - 1, y2 - 1)
			next_board[lower_left] = self_copy
			next_board[self.location] = None
			if not next_board[lower_left].king_in_check(next_board):
				moves.append(lower_left)
			next_board = board.copy()
			self_copy = copy.deepcopy(self)

		print(moves)
		print(" ")

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

	def calculate_moves(self, board):
		x = self.location[0]
		y = self.location[1]
		moves = []
		enemy = "Black" if self.color == "White" else "White"
		spc1, spc2, spc3, spc4, spc5,spc6, spc7, spc8 = (x-2,y+1), (x+2, y-1), (x+1, y-2), (x-1, y+2), (x+2, y+1), (x+1, y+2), (x-2, y-1), (x-1, y-2) 
		if board[spc1] == None or board[spc1].color == enemy:
			moves.append(spc1)
		if board[spc2] == None or board[spc2].color == enemy:
			moves.append(spc2)
		if board[spc3] == None or board[spc3].color == enemy:
			moves.append(spc3)
		if board[spc4] == None or board[spc4].color == enemy:
			moves.append(spc4)
		if board[spc5] == None or board[spc5].color == enemy:
			moves.append(spc5)
		if board[spc6] == None or board[spc6].color == enemy:
			moves.append(spc6)
		if board[spc7] == None or board[spc7].color == enemy:
			moves.append(spc7)
		if board[spc8] == None or board[spc8].color == enemy:
			moves.append(spc8)
		return moves


class Pawn(Piece):

	def __init__(self, *args):
		super(Pawn, self).__init__(*args)

	def calculate_moves(self, board):
		x = self.location[0]
		y = self.location[1]
		moves = []
		# if ! self.has_moved:
		if self.color == "White":
			if board[(x, y + 1)] == None:
				moves.append((x, y + 1))
				if not self.has_moved and board[(x, y + 2)] == None:
					moves.append((x, y + 2))
			if board[(x + 1, y + 1)] != LIMIT and board[(x + 1, y + 1)] != None and board[(x + 1, y + 1)].color == "Black":
				moves.append((x + 1, y + 1))
			if board[(x - 1, y + 1)] != LIMIT and board[(x - 1, y + 1)] != None and board[(x - 1, y + 1)].color == "Black":
				moves.append((x - 1, y + 1))
		else:
			if board[(x, y - 1)] == None:
				moves.append((x , y - 1))
				if not self.has_moved and board[(x, y - 2)] == None:
					moves.append((x, y - 2))
			if board[(x - 1, y - 1)] != LIMIT and board[(x - 1, y - 1)] != None and board[(x - 1, y - 1)].color == "White":
				moves.append((x - 1, y - 1))
			if board[(x + 1, y - 1)] != LIMIT and board[(x + 1, y - 1)] != None and board[(x + 1, y - 1)].color == "White":
				moves.append((x + 1, y - 1))
		return moves
