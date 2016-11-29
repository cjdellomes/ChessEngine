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
			(4,0): King((4,0), 500, False, 'White', []),
			(4,1): Pawn((4,1), 1, False, 'White', [(4,2)]),
			(4,2): None,
			(4,3): None,
			(4,4): None,
			(4,5): None,
			(4,6): Pawn((4,6), 1, False, 'Black', [(4,5)]),
			(4,7): King((4,7), 1, False, 'Black', []),
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
	def __getitem__(self,key):
		return self.board[key]

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

class Queen(Piece):

	def __init__(self, *args):
		super(Queen, self).__init__(*args)



class Rook(Piece):

	def __init__(self, *args):
		super(Rook, self).__init__(*args)

class Bishop(Piece):

	def __init__(self, *args):
		super(Bishop, self).__init__(*args)

class Knight(Piece):

	def __init__(self, *args):
		super(Knight, self).__init__(*args)

class Pawn(Piece):

	def __init__(self, *args):
		super(Pawn, self).__init__(*args)

	def calculate_moves(self, board):
		x = self.location[0]
		y = self.location[1]
		moves = []
		# if ! self.has_moved:
		if self.color == "White":
			if not self.has_moved and board[(x, y + 2)] == None:
				moves.append((x, y + 2))
			if board[(x, y + 1)] == None:
				moves.append((x, y + 1))
		else:
			if not self.has_moved and board[(x, y - 2)] == None:
				moves.append((x, y - 2))
			if board[(x, y - 1)] == None:
				moves.append((x , y - 1))
		return moves
