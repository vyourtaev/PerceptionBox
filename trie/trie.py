import unittest

class Trie(object):
    '''
    classdocs
    '''

    def __init__(self,):
        '''
        Constructor
        '''
        self.isWord = False
        self.node = {}
        
            
    def build(self, str):
        """
        Takes a str and splits it character wise 
        Arguments:
        - `str`: The string to be stored in the trie
        """
        node = self.node
        for ch in str:
            if node.has_key(ch) is True:
                node = node[ch]
            else :
                node[ch] = {}
                node = node[ch]

    def search(self, str):
        node = self.node
        for ch in str:
            if node.has_key(ch) is True:
                node = node[ch]
            else :
                return False
        return True
    
class TrieTest(unittest.TestCase):
    """ Test case for the above trie data structure
    """
    words = ["oath","pea","eat","rain"]  
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v'],
    ]   
    
    def setUp(self):
        self.trie = Trie()
        self.trie.build('oathpeaeatrain')

    def testSearch(self):
        self.assertTrue(self.trie.search('oathpeaeatrain'))
        
    def testSearchFail(self):
        self.assertFalse(self.trie.search('pid'))

    def testPrefixSearch(self):
        self.assertTrue(self.trie.search('oath'))
