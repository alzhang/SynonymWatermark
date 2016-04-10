import nltk as nl
import random as rnd
import string

class SynonymWatermark:
    def __init__(self, txt, complexity):
        self.text = txt
        self.complexity = complexity

    def notProperWord(self, word):
        return word[0].islower()


    def makeCopies(numCopies):
        copies = []
        for i in range(numCopies):
            copies.append(makeCopy())

        return copies

    def makeCopy(self):
        tokens = nl.word_tokenize(self.text)
        tags = nl.pos_tag(tokens)

        weight = 0

        for i in range(len(tokens)):
            weight = weight + rnd.random() * self.complexity

            if weight > 1 and self.notProperWord(tokens[i]):
                synonym = "" #send tags[i] to thesaurus
                tokens[i] = synonym
                weight = 0

        return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
