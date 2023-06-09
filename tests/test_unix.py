from algorithms.unix import (
    join_with_slash,
    full_path,
    split,
    simplify_path_v1, simplify_path_v2
)
import os
import unittest


class TestUnixPath(unittest.TestCase):
    def test_join_with_slash(self):
        self.assertEqual("path/to/dir/file",
                         join_with_slash("path/to/dir/", "file"))
        self.assertEqual("path/to/dir/file",
                         join_with_slash("path/to/dir", "file"))
        self.assertEqual("http://algorithms/part",
                         join_with_slash("http://algorithms", "part"))
        self.assertEqual("http://algorithms/part",
                         join_with_slash("http://algorithms/", "part"))


    def test_split(self):
        # Test url path
        path = "https://algorithms/unix/test.py"
        expect_result = split(path)
        self.assertEqual("https://algorithms/unix", expect_result[0])
        self.assertEqual("test.py", expect_result[1])
        # Test file path
        path = "algorithms/unix/test.py"
        expect_result = split(path)
        self.assertEqual("algorithms/unix", expect_result[0])
        self.assertEqual("test.py", expect_result[1])

