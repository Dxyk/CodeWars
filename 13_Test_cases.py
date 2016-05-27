import unittest

etm = __import__('13_escape_the_mines')


class TestEscapeMine(unittest.TestCase):
    def test_basic_1d_map(self):
        minemap = [[True]]
        self.assertEqual(etm.solve(minemap, {'x': 0, 'y': 0}, {'x': 0, 'y': 0}),
                         [])

    def test_regular_2d_map(self):
        minemap = [[True, False], [True, True]]
        self.assertEqual(etm.solve(minemap, {'x': 0, 'y': 0}, {'x': 1, 'y': 0}),
                         ['right'])

    def test_regular_2d_map_2(self):
        minemap = [[True, False], [True, True]]
        self.assertEqual(etm.solve(minemap, {'x': 0, 'y': 0}, {'x': 1, 'y': 0}),
                         ['right', 'down'])

    def test_linear_map_left_to_right(self):
        minemap = [[True], [True], [True], [True]]
        self.assertEqual(etm.solve(minemap, {'x': 0, 'y': 0}, {'x': 3, 'y': 0}),
                         ['right', 'right', 'right'])

    def test_linear_map_right_to_left(self):
        minemap = [[True], [True], [True], [True]]
        self.assertEqual(etm.solve(minemap, {'x': 0, 'y': 0}, {'x': 3, 'y': 0}),
                         ['left', 'left', 'left'])

    def test_2d_with_obstacles(self):
        minemap = [[True, True, True], [False, False, True], [True, True, True]]
        self.assertEqual(etm.solve(minemap, {'x': 0, 'y': 0}, {'x': 2, 'y': 0}),
                         ['down', 'down', 'right', 'right', 'up', 'up'])
