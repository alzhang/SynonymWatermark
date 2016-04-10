import nltk as nl
import random as rnd
import string
import getSynonyms as wordnet

class SynonymWatermark:
    def __init__(self, txt, complexity):
        self.text = txt
        self.complexity = complexity
        self.net = wordnet.loadWordNet()

    def notProperWord(self, word):
        return word[0].islower()


    def makeCopies(numCopies):
        copies = []
        for i in range(numCopies):
            copies.append(makeCopy())

        return copies
    
    def convertPOS(self,pos):
        if "N" in pos:
            return 'n'
        if "V" in pos:
            return 'v'
        if "A" in pos:
            return 'a'
        print pos
        return 'n'

    def makeCopy(self):
        tokens = nl.word_tokenize(self.text)
        tags = nl.pos_tag(tokens)

        weight = 0

        for i in range(len(tokens)):
            weight = weight + rnd.random() * self.complexity

            if weight > 1 and self.notProperWord(tokens[i]):
                _,pos = tags[i]
                pos = self.convertPOS(pos)
                synonym = wordnet.getSynonym(self.net,tokens[i],pos) #send tags[i] to thesaurus
                if synonym:
                    tokens[i] = synonym
                    weight = 0

        return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
