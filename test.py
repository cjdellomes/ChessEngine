import unittest
import chess

class TestStringMethods(unittest.TestCase):

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
        self.assertEqual(piece.calculate_moves(board), [empty_spc1,empty_spc2, enemy_loc1, enemy_loc2])
        #Note to self probably should change the object's location but not necessary for test
        board[empty_spc2] = board[enemy_loc1]
        board[enemy_loc1] = chess.Pawn(enemy_loc1, 1, False, 'White', [])
        board[enemy_loc2] = chess.Pawn(enemy_loc1, 1, False, 'White', [])
        self.assertEqual(piece.calculate_moves(board), [empty_spc1])
        board[empty_spc1] = board[empty_spc2]
        board[empty_spc2] = None
        self.assertEqual(piece.calculate_moves(board), [])
        #resetting board and testing board boundries
        board = chess.Board()
        location = (7,7)
        piece = chess.Pawn(location, 1, False, 'White', [])
        board[(location)] = piece
        self.assertEqual(piece.calculate_moves(board),[])

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
        self.assertEqual(piece.value, 1)
        self.assertTrue(isinstance(piece,chess.Pawn))
        self.assertEqual(piece.color, "Black")
        self.assertEqual(piece.calculate_moves(board), [empty_spc1,empty_spc2,enemy_loc1,enemy_loc2])
        #Note to self probably should change the object's location but not necessary for test
        board[empty_spc2] = board[enemy_loc1]
        board[enemy_loc1] = chess.Pawn(enemy_loc1, 1, False, 'Black', [])
        board[enemy_loc2] = chess.Pawn(enemy_loc1, 1, False, 'Black', [])
        self.assertEqual(piece.calculate_moves(board), [empty_spc1])
        board[empty_spc1] = board[empty_spc2]
        board[empty_spc2] = None
        self.assertEqual(piece.calculate_moves(board), [])
        #resetting board and testing board boundries
        board = chess.Board()
        location = (0,0)
        piece = chess.Pawn(location, 1, False, 'Black', [])
        board[(location)] = piece
        self.assertEqual(piece.calculate_moves(board),[])

        

if __name__ == '__main__':
    unittest.main()