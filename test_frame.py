
import pytest
import time
import unittest


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        time.sleep(1)
        print('the testing started')
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('the testing ended')
    
    def test_search1(self):
        print('checing if 3 is 3')
        time.sleep(4)
        
        assert 3 == 3
    
    def test_search2(self):
        print('check if 3 si 5')
        time.sleep(1)
        
        assert 3 == 3