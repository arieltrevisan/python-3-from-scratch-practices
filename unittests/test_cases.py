import unittest as ut

"""

https://docs.python.org/3/library/unittest.html#test-discovery

"""


class TestClassOne(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        # print("setupClass")
        pass

    @classmethod
    def tearDownClass(cls):
        # print("tearDownClass")
        pass

    # setup of each method
    def setUp(self):
        # print("setUp")
        pass

    # teardown of each method
    def tearDown(self):
        # print("tearDown")
        pass

    def test_bool(self):
        value = True
        self.assertTrue(value, "Not True")

    def test_equals(self):
        value_1 = 1
        value_2 = 1
        self.assertEqual(value_1, value_2)

    def test_raise(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0


class TestClassTwo(ut.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        list_1 = [1, 2, 3]
        list_2 = [2, 3, 1]
        self.assertCountEqual(list_1, list_2)


if __name__ == '__main__':
    ut.main(verbosity=2)
