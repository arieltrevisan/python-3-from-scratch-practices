import unittest as ut
from unittests import test_cases

# Load from TestCase
# case1 = ut.TestLoader().loadTestsFromTestCase(test_cases.TestClassOne)
# case2 = ut.TestLoader().loadTestsFromTestCase(test_cases.TestClassTwo)
# cases = [case1, case2]

# Load from Module
cases = ut.TestLoader().loadTestsFromModule(test_cases)

suite = ut.TestSuite(cases)
ut.TextTestRunner(verbosity=2).run(suite)
