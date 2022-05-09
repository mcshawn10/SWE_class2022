

import unittest
import pathlib as pl
#from proj import StringStat

class TestStringStat(unittest.TestCase):
    '''This test case raises an error if the file does not exist in the current work folder'''
    def assertIsFile(self, path):
            if not pl.Path(path).resolve().is_file():
                raise AssertionError("File does not exist: %s" % str(path))

    def test_return_stats(self, path):
        '''This case will test that the file exists and the file is not empy'''
        self.assertIsFile(path)
        f = open(path, 'r')
        ls = [line for line in f.readlines()]
        self.assertTrue(len(ls))

    def test_replace_word(self, word, path):
        '''This case will test that the word exists in the file'''
        input_file = open(path, 'r')
        i = 0

        for line in input_file.readlines():
            
            
            if word in line:
                
                i+=1

        self.assertTrue(i)

