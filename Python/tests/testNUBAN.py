import unittest
import sys
sys.path.append('..')
import NUBAN as nuban

class AdapterTest(unittest.TestCase):
    def setUp(self):
        self.account_number = "2034327658"
        self.bank_code =  "11" #first bank
    def test_nuban(self):
        assertTrue(nuban.validate_nuban_account(self.bank_code,self.account_number))
        assertTrue(nuban.NUBAN().is_valid_NUBAN(self.bank_code+self.account_number))
        self.account_number[-1]="6"
        assertFalse(nuban.validate_nuban_account(self.bank_code,self.account_number))
        assertFalse(nuban.NUBAN().is_valid_NUBAN(self.bank_code+self.account_number))
        self.bank_code = "058"
        assertFalse(nuban.validate_nuban_account(self.bank_code,self.account_number))
        assertFalse(nuban.NUBAN().is_valid_NUBAN(self.bank_code+self.account_number))
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
