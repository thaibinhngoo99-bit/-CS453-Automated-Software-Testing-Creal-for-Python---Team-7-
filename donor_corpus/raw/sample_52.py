# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


import unittest

"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b[(len(b) - len(a)):] == a, a[(len(a) - len(b)):] == b)[len(a) >= len(b)]


class TestEndOther(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(end_other('Hiabc', 'abc'), True)

    def test_case_01(self):
        self.assertEqual(end_other('AbC', 'HiaBc'), True)

    def test_case_02(self):
        self.assertEqual(end_other('abc', 'abXabc'), True)

    def test_case_03(self):
        self.assertEqual(end_other('Hiabc', 'abcd'), False)

    def test_case_04(self):
        self.assertEqual(end_other('Hiabc', 'bc'), True)

    def test_case_05(self):
        self.assertEqual(end_other('Hiabcx', 'bc'), False)

    def test_case_06(self):
        self.assertEqual(end_other('abc', 'abc'), True)

    def test_case_07(self):
        self.assertEqual(end_other('xyz', '12xyz'), True)

    def test_case_08(self):
        self.assertEqual(end_other('yz', '12xz'), False)

    def test_case_09(self):
        self.assertEqual(end_other('Z', '12xz'), True)

    def test_case_10(self):
        self.assertEqual(end_other('12', '12'), True)

    def test_case_11(self):
        self.assertEqual(end_other('abcXYZ', 'abcDEF'), False)

    def test_case_12(self):
        self.assertEqual(end_other('ab', 'ab12'), False)

    def test_case_13(self):
        self.assertEqual(end_other('ab', '12ab'), True)



if __name__ == "__main__":
    unittest.main()
