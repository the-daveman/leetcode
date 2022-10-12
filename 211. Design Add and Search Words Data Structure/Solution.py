import re
class WordDictionary:

    def __init__(self):
        self.Dictionary = {}

    def addWord(self, word: str) -> None:
        self.Dictionary[word] = True

    def search(self, word: str) -> bool:
        if(re.search('\.',word)): # wildcard logic
            for w in self.Dictionary.keys():
                if (re.search('^'+word+'$',w)): # if word found in dictionary (=~)
                    return True
        else: # simple lookup
            if word in self.Dictionary:
                return self.Dictionary[word]
        return False # failure case


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
