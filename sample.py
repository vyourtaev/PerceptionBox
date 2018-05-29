#!/usr/bin/env python 

import unittest
from trie.trie import TrieTest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TrieTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
    unittest.main()