import unittest
import chess

class TestStringMethods(unittest.TestCase):

    def test_white_pawn(self):
        board = chess.Board()
        piece = board[(0,1)]
        self.assertTrue(piece.location,(0,1))
        self.assertFalse(piece.has_moved)
        self.assertEqual(piece.value, 1)
        self.assertTrue(isinstance(piece,chess.Pawn))
        self.assertEqual(piece.color, "White")
        self.assertEqual(piece.calculate_moves(board), [(0,3),(0,2)])

    def test_black_pawn(self):
        board = chess.Board()
        piece = board[(0,6)]
        self.assertTrue(piece.location,(0,6))
        self.assertFalse(piece.has_moved)
        self.assertEqual(piece.value, 1)
        self.assertTrue(isinstance(piece,chess.Pawn))
        self.assertEqual(piece.color, "Black")
        self.assertEqual(piece.calculate_moves(board), [(0,4),(0,5)])


if __name__ == '__main__':
    unittest.main()