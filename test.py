import unittest
import chess

class TestStringMethods(unittest.TestCase):
    def test_board(self):
        board = chess.Board()
        self.assertTrue(isinstance(board, chess.Board))

        board.board = board.clear_board()
        self.assertTrue(isinstance(board, chess.Board))
        for key in board.get_board():
            self.assertEqual(board.get_board()[key],None)

    def test_white_pawn(self):
        board = chess.Board()
        piece = board[(1,1)]
        enemy_loc1 = (2,2)
        enemy_loc2 = (0,2)
        empty_spc1 = (1,2)
        empty_spc2 = (1,3)
        board[enemy_loc1] = chess.Pawn(enemy_loc1, 1, False, 'Black', [])
        board[enemy_loc2] = chess.Pawn(enemy_loc2, 1, False, 'Black', [])

        #testing initialization of object
        self.assertEqual(piece.location,(1,1))
        self.assertFalse(piece.has_moved)
        self.assertEqual(piece.value, 1)
        self.assertTrue(isinstance(piece,chess.Pawn))
        self.assertEqual(piece.color, "White")

        #testing moves
        self.assertEqual(piece.calculate_moves(board.get_board()), [empty_spc1,empty_spc2, enemy_loc1, enemy_loc2])

        #Note to self probably should change the object's location but not necessary for test
        board[empty_spc2] = board[enemy_loc1]
        board[enemy_loc1] = chess.Pawn(enemy_loc1, 1, False, 'White', [])
        board[enemy_loc2] = chess.Pawn(enemy_loc1, 1, False, 'White', [])
        self.assertEqual(piece.calculate_moves(board.get_board()), [empty_spc1])
        board[empty_spc1] = board[empty_spc2]
        board[empty_spc2] = None
        self.assertEqual(piece.calculate_moves(board.get_board()), [])

        #resetting board and testing board boundries
        board = chess.Board()
        location = (7,7)
        piece = chess.Pawn(location, 1, False, 'White', [])
        board[(location)] = piece
        self.assertEqual(piece.calculate_moves(board.get_board()),[])
        


    def test_black_pawn(self):
        board = chess.Board()
        piece = board[(1,6)]
        enemy_loc1 = (0,5)
        enemy_loc2 = (2,5)
        empty_spc1 = (1,5)
        empty_spc2 = (1,4)
        board[enemy_loc1] = chess.Pawn(enemy_loc1, 1, False, 'White', [])
        board[enemy_loc2] = chess.Pawn(enemy_loc2, 1, False, 'White', [])
        self.assertEqual(piece.location,(1,6))
        self.assertFalse(piece.has_moved)
        self.assertEqual(piece.value, -1)
        self.assertTrue(isinstance(piece,chess.Pawn))
        self.assertEqual(piece.color, "Black")
        self.assertEqual(piece.calculate_moves(board.get_board()), [empty_spc1,empty_spc2,enemy_loc1,enemy_loc2])

        #Note to self probably should change the object's location but not necessary for test
        board[empty_spc2] = board[enemy_loc1]
        board[enemy_loc1] = chess.Pawn(enemy_loc1, 1, False, 'Black', [])
        board[enemy_loc2] = chess.Pawn(enemy_loc1, 1, False, 'Black', [])
        self.assertEqual(piece.calculate_moves(board.get_board()), [empty_spc1])
        board[empty_spc1] = board[empty_spc2]
        board[empty_spc2] = None
        self.assertEqual(piece.calculate_moves(board.get_board()), [])

        #resetting board and testing board boundries
        board = chess.Board()
        location = (0,0)
        piece = chess.Pawn(location, 1, False, 'Black', [])
        board[(location)] = piece
        self.assertEqual(piece.calculate_moves(board.get_board()),[])

    def test_knight(self):
        board = chess.Board().clear_board()
        pieceLocation = (4,3)
        spc1 = (2,4)
        spc2 = (3,5)
        spc3 = (5,5)
        spc4 = (6,4)
        spc5 = (6,2)
        spc6 = (5,1)
        spc7 = (3,1)
        spc8 = (2,2)
        piece = chess.Knight(pieceLocation, 5, False, 'White', [])
        board[pieceLocation] = piece
        self.assertEqual(piece.location, pieceLocation)
        self.assertFalse(piece.has_moved)
        self.assertEqual(piece.value,5)
        self.assertTrue(isinstance(piece,chess.Knight))
        self.assertEqual(piece.color,'White')

        #Made into a set because order does not really matter -Peyton Cross
        self.assertEqual(set(piece.calculate_moves(board)),set([spc1,spc2,spc3,spc4,spc5,spc6,spc7,spc8]))
        board[spc1] = chess.Pawn(spc1, 1, False, "Black", [])
        self.assertEqual(set(piece.calculate_moves(board)),set([spc1,spc2,spc3,spc4,spc5,spc6,spc7,spc8]))
        board[spc1] = chess.Pawn(spc1, 1, False, "White", [])
        self.assertEqual(set(piece.calculate_moves(board)),set([spc2,spc3,spc4,spc5,spc6,spc7,spc8]))

    def test_bishop(self):
        board = chess.Board().clear_board()
        pieceLocation = (4,3)
        spc1, spc2, spc3, spc4, spc5, spc6, spc7, spc8, spc9, spc10, spc11, spc12, spc13 = (5,4),(6,5),(7,6),(3,2),(2,1),(1,0),(3,4),(2,5),(1,6),(0,7),(5,2),(6,1),(7,0)
        piece = chess.Bishop(pieceLocation, 7, False, 'White', [])
        board[pieceLocation] = piece
        self.assertEqual(set(piece.calculate_moves(board)), set([spc1, spc2, spc3, spc4, spc5, spc6, spc7, spc8, spc9, spc10, spc11, spc12, spc13]))
        board[spc1] = chess.Rook(pieceLocation, 5, False, 'Black', [])
        self.assertEqual(set(piece.calculate_moves(board)), set([spc1, spc4, spc5, spc6, spc7, spc8, spc9, spc10, spc11, spc12, spc13]))
        board[spc1] = chess.Rook(pieceLocation, 5, False, 'White', [])
        self.assertEqual(set(piece.calculate_moves(board)), set([spc4, spc5, spc6, spc7, spc8, spc9, spc10, spc11, spc12, spc13]))

    def test_rook(self):
        board = chess.Board().clear_board()
        pieceLocation = (4,3)
        spc1, spc2, spc3, spc4, spc5, spc6, spc7, spc8, spc9, spc10, spc11, spc12, spc13, spc14 = (3,3), (2,3), (1,3), (0,3),(4,2),(4,1),(4,0),(5,3),(6,3),(7,3),(4,4),(4,5),(4,6),(4,7)
        piece = chess.Rook(pieceLocation, 6, False, 'White', [])
        board[pieceLocation] = piece
        self.assertEqual(set(piece.calculate_moves(board)), set([spc1, spc2, spc3, spc4, spc5, spc6, spc7, spc8, spc9, spc10, spc11, spc12, spc13, spc14]))

    def test_queen(self):
        board = chess.Board().clear_board()
        pieceLocation = (4,3)
        diag_spaces = [(5,4),(6,5),(7,6),(3,2),(2,1),(1,0),(3,4),(2,5),(1,6),(0,7),(5,2),(6,1),(7,0)]
        horiz_spaces = [(3,3), (2,3), (1,3), (0,3),(4,2),(4,1),(4,0),(5,3),(6,3),(7,3),(4,4),(4,5),(4,6),(4,7)]
        piece = chess.Queen(pieceLocation, 10, False, 'White', [])
        board[pieceLocation] = piece
        self.assertEqual(set(piece.calculate_moves(board)), set(diag_spaces + horiz_spaces))

    def test_king(self):
        board = chess.Board().clear_board()
        pieceLocation = (4,3)
        surrounding_spaces = [(4,4),(4,2),(5,3),(3,3),(5,4),(3,4),(3,2),(5,2)]
        piece = chess.King(False, False, pieceLocation, 500, False, 'White', [])
        board[pieceLocation] = piece

        self.assertEqual(piece.location, (4,3))
        self.assertFalse(piece.has_moved)
        self.assertEqual(piece.value, 500)
        self.assertTrue(isinstance(piece, chess.King))
        self.assertEqual(piece.color, 'White')

        self.assertFalse(piece.king_in_check(board))
        self.assertEqual(set(piece.calculate_moves(board)), set(surrounding_spaces))

        board[(7,7)] = chess.Pawn((7,7), 1, False, 'Black', [(7,6)])
        self.assertFalse(piece.king_in_check(board))
        self.assertEqual(set(piece.calculate_moves(board)), set(surrounding_spaces))

        board[(4,4)] = chess.Queen((4,4), 10, False, 'Black', [])
        board[(4,4)].moves = board[(4,4)].calculate_moves(board)
        possible_moves = [(4,4), (3,2), (5,2)]
        self.assertTrue(piece.king_in_check(board))
        self.assertEqual(set(piece.calculate_moves(board)), set(possible_moves))

        board[(4,2)] = chess.Queen((4,2), 10, False, 'Black', [])
        board[(4,2)].moves = board[(4,2)].calculate_moves(board)
        possible_moves = []
        self.assertEqual(set(piece.calculate_moves(board)), set([]))
        self.assertTrue(piece.king_in_check(board))
        self.assertTrue(piece.king_in_checkmate(board))

if __name__ == '__main__':
    unittest.main()