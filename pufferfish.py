import chess

def greeting():
	name = "Pufferfish"
	description = "Dankest fish in the sea!"
	return ("Hello I am %s, the %s" % (name,description))

def main():
	print(greeting())
	board = chess.Board()
	print(board[(0,1)].calculate_moves(board))
	print(board[(0,6)].calculate_moves(board))
	print(board[(200,300)])


if __name__ == "__main__":
	main()