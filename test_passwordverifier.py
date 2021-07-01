import unittest
import passwordverifier
from passwordverifier import password
from passwordverifier import num_check
from passwordverifier import up_check
from passwordverifier import lo_check
class Testpasswordverifier(unittest.TestCase):
    def test_passwordlength0(self):
        self.assertGreater(len(password),0)

    def test_password8(self):
        self.assertGreaterEqual(len(password),8)  

    def test_num_check(self):
        self.assertTrue(num_check)  

    def test_up_check(self):
        self.assertTrue(up_check)

    def test_lo_check(self):
        self.assertTrue(lo_check)    



if __name__ == '__main__':
    unittest.main()       
