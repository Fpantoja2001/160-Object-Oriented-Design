import unittest
from assignment1 import prime_decomposition

class testAssignment1(unittest.TestCase):
    def test_prime_decomp850(self):
        self.assertTrue([2,5,5,17],prime_decomposition(850))

    def test_prime_decomp1(self):
        self.assertTrue([[]],prime_decomposition(1))

    def test_prime_decomp181(self):
        self.assertTrue([181],prime_decomposition(181))

    def test_prime_decomp42(self):
        self.assertTrue([2,3,7],prime_decomposition(42))
        

if __name__=='__main__':
    unittest.main()