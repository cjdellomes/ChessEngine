import chess
def greeting():

	name = "Pufferfish"
	description = "Dankest fish in the sea!"
	return ("Hello I am %s, the %s" % (name,description))

def main():
	print(greeting())
	board = chess.Board()

if __name__ == "__main__":
	main()