import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
# Part 1: Tests for create_rectangle
        def test_create_rectangle_1(self):
            rect = hw2.create_rectangle(data.Point(2, 2), data.Point(10, 10))
            self.assertEqual(rect.top_left, data.Point(2, 10))
            self.assertEqual(rect.bottom_right, data.Point(10, 2))

        def test_create_rectangle_2(self):
            rect = hw2.create_rectangle(data.Point(5, 5), data.Point(3, 8))
            self.assertEqual(rect.top_left, data.Point(3, 8))
            self.assertEqual(rect.bottom_right, data.Point(5, 5))

# Part 2: Tests for shorter_duration_than
        def test_shorter_duration_than_1(self):
            self.assertTrue(hw2.shorter_duration_than(data.Duration(3, 30), data.Duration(4, 0)))

        def test_shorter_duration_than_2(self):
            self.assertFalse(hw2.shorter_duration_than(data.Duration(5, 0), data.Duration(4, 30)))

# Part 3: Tests for songs_shorter_than
        def test_songs_shorter_than_1(self):
            song_list = [
                data.Song("Artist1", "Title1", data.Duration(3, 0)),
                data.Song("Artist2", "Title2", data.Duration(4, 0)),
            ]
            result = hw2.songs_shorter_than(song_list, data.Duration(3, 30))
            self.assertEqual(result, [song_list[0]])

        def test_songs_shorter_than_2(self):
            song_list = [
                data.Song("Artist1", "Title1", data.Duration(5, 0)),
                data.Song("Artist2", "Title2", data.Duration(3, 15)),
            ]
            result = hw2.songs_shorter_than(song_list, data.Duration(4, 0))
            self.assertEqual(result, [song_list[1]])

# Part 4: Tests for running_time
        def test_running_time_1(self):
            song_list = [
                data.Song("Artist1", "Title1", data.Duration(3, 30)),
                data.Song("Artist2", "Title2", data.Duration(4, 0)),
            ]
            result = hw2.running_time(song_list, [0, 1])
            self.assertEqual(result, data.Duration(7, 30))

        def test_running_time_2(self):
            song_list = [
                data.Song("Artist1", "Title1", data.Duration(1, 30)),
                data.Song("Artist2", "Title2", data.Duration(2, 15)),
            ]
            result = hw2.running_time(song_list, [1])
            self.assertEqual(result, data.Duration(2, 15))

# Part 5: Tests for validate_route
        def test_validate_route_1(self):
            city_links = [['a', 'b'], ['b', 'c'], ['c', 'd']]
            self.assertTrue(hw2.validate_route(city_links, ['a', 'b', 'c', 'd']))

        def test_validate_route_2(self):
            city_links = [['a', 'b'], ['b', 'c']]
            self.assertFalse(hw2.validate_route(city_links, ['a', 'c']))

# Part 6: Tests for longest_repetition
        def test_longest_repetition_1(self):
            self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 1, 1, 1]), 4)

        def test_longest_repetition_2(self):
            self.assertIsNone(hw2.longest_repetition([]))

if __name__ == '__main__':
        unittest.main()