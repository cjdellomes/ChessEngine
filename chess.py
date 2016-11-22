class Board:

	def __init__(self, board):
		self.board = board

	def __init__(self):
		self.board = {
			'a1': Rook(),
			'a2': Pawn(),
			'a3': None,
			'a4': None,
			'a5': None,
			'a6': None,
			'a7': Pawn(),
			'a8': Rook(),
			'b1': Knight(),
			'b2': Pawn(),
			'b3': None,
			'b4': None,
			'b5': None,
			'b6': None,
			'b7': Pawn(),
			'b8': Knight(),
			'c1': Bishop(),
			'c2': Pawn(),
			'c3': None,
			'c4': None,
			'c5': None,
			'c6': None,
			'c7': Pawn(),
			'c8': Bishop(),
			'd1': Queen(),
			'd2': Pawn(),
			'd3': None,
			'd4': None,
			'd5': None,
			'd6': None,
			'd7': Pawn(),
			'd8': Queen(),
			'e1': King(),
			'e2': Pawn(),
			'e3': None,
			'e4': None,
			'e5': None,
			'e6': None,
			'e7': Pawn(),
			'e8': King(),
			'f1': Bishop(),
			'f2': Pawn(),
			'f3': None,
			'f4': None,
			'f5': None,
			'f6': None,
			'f7': Pawn(),
			'f8': Bishop(),
			'g1': Knight(),
			'g2': Pawn(),
			'g3': None,
			'g4': None,
			'g5': None,
			'g6': None,
			'g7': Pawn(),
			'g8': Knight(),
			'h1': Rook(),
			'h2': Pawn(),
			'h3': None,
			'h4': None,
			'h5': None,
			'h6': None,
			'h7': Pawn(),
			'h8': Rook()
		}

class Piece:

	def __init__(self, location = None, value = None, has_moved = None, color = None):
		self.location = location
		self.value = value
		self.has_moved = has_moved
		self.color = color

class King(Piece):

	def __init__(self, in_check = False, in_checkmate = False):
		super(King, self).__init__()
		self.in_check = in_check
		self.in_checkmate = in_checkmate

class Queen(Piece):

	def __init__(self):
		super(Queen, self).__init__()

class Rook(Piece):

	def __init__(self):
		super(Rook, self).__init__()

class Bishop(Piece):

	def __init__(self):
		super(Bishop, self).__init__()

class Knigth(Piece):

	def __init__(self):
		super(Knight, self).__init__()

class Pawn(Piece):

	def __init__(self):
		super(Pawn, self).__init__()