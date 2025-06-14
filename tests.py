import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_dir_root(self):
        result = get_files_info("calculator", ".")
        print(result)

    def test_pkg_dir(self):
        result = get_files_info("calculator", "pkg")
        print(result)

    def test_bin_dir(self):
        # should return error string
        result = get_files_info("calculator", "/bin")
        print(result)

    def test_parent_dir(self):
        # should return error string
        result = get_files_info("calculator", "../")
        print(result)

if __name__ == "__main__":
    unittest.main()