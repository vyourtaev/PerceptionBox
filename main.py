#!/usr/bin/env python

def make_lookups(board, words=""):
    # Make set of valid characters.
    chars = set()
    for word in board:
        chars.update(word)

    words = set(x for x in words if set(x) <= chars)
    prefixes = set()
    for w in words:
        for i in range(len(w)+1):
            prefixes.add(w[:i])

    return words, prefixes

def make_trie(board):
    """
    trie = { (x, y):set([(x0,y0), (x1,y1), (x2,y2)]), }
    """
    root = None
    trie = { root:set() }
    chardict = { root:'' }

    for i, row in enumerate(board):
        for j, char in enumerate(row):
            chardict[(i, j)] = char
            node = (i, j)
            children = set()
            trie[node] = children
            trie[root].add(node)
            add_children(node, children, board)

    return trie, chardict

def add_children(node, children, board):
    x0, y0 = node
    for i in [-1,0,1]:
        x = x0 + i
        if not (0 <= x < len(board)):
            continue
        for j in [-1,0,1]:
            y = y0 + j
            if not (0 <= y < len(board[0])) or (i == j == 0):
                continue

            children.add((x,y))
            
def to_word(chardict, pos_list):
    return ''.join(chardict[x] for x in pos_list)

def find_words(trie, chardict, position, prefix, results, words, prefixes):
    """ 
      trie :: mapping (x,y) to set of reachable positions
      chardict :: mapping (x,y) to character
      position :: current position (x,y) -- equals prefix[-1]
      prefix :: list of positions in current string
      results :: set of words found
      words :: set of valid words in the dictionary
      prefixes :: set of valid words or prefixes thereof
    """
    word = to_word(chardict, prefix)

    if word not in prefixes:
        return

    if word in words:
        results.add(word)

    for child in trie[position]:
        if child not in prefix:
            find_words(trie, chardict, child, prefix+[child], results, words, prefixes)

words = ["oath","pea","eat","rain"]  
board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v'],
    ]   
trie, chardict = make_trie(board)
word, prefixes = make_lookups(board, words)
result = set()
find_words(trie, chardict, None, [], result, words, prefixes)

print result




