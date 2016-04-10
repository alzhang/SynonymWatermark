import nltk as nl
import random as rnd
import string
from nltk.corpus import wordnet as wn
import getSynonyms as wordnet

class SynonymWatermark:
    def __init__(self, txt, complexity):
        self.text = txt
        self.complexity = complexity
        self.net = wordnet.loadWordNet()
        self.tags = []
 #       self.calculateWeights()

    def notProperWord(self, word):
        return word[0].islower()


    def makeCopies(numCopies):
        copies = []
        for i in range(numCopies):
            copies.append(makeCopy())

        return copies
    
    def convertPosNLTK(self,pos):
        if "N" in pos:
            return wn.NOUN
        if "A" in pos:
            return wn.ADJ
        if "V" in pos:
            return wn.VERB
        return wn.NOUN

    def convertPos(self,pos):
        if "N" in pos:
            return 'n'
        if "A" in pos:
            return 'a'
        if "V" in pos:
            return 'v'
        return 'n'

    def makeCopy(self):
        tokens = nl.word_tokenize(self.text)
        tags = nl.pos_tag(tokens)

        weight = 0

        for i in range(len(tokens)):
            weight = weight + rnd.random() * self.complexity

            if weight > 1 and self.notProperWord(tokens[i]):
                _,pos = tags[i]
                pos = self.convertPos(pos)
                synonym = wordnet.getSynonym(self.net,tokens[i],pos) #send tags[i] to thesaurus
                if synonym:
                    tokens[i] = synonym
                    weight = 0

        return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()

    def countSynsets(self, word, pos):
        return len(wn.synsets(word, pos))

    def calculateWeights(self):
        tokens = nl.word_tokenize(self.text)
        nltkTags = nl.pos_tag(tokens)
        print "CALCULATING WEIGHTS"
        for i in range(len(tokens)):
            weight = 0.0
            word,pos = nltkTags[i]
            if word.islower():
                weight += 0.2
            count = self.countSynsets(word, self.convertPosNLTK(pos))
            pos = self.convertPos(pos)
            if count >= 1:
                print count
                print word
                #weight += 1.0/count
                weight += count/12.0
            syn = wordnet.getSynonym(self.net, word, pos)
            if syn:
                weight += 3
            self.tags.append( [word,pos,weight,i,syn] )

        print len(self.tags)
        unsortedlist = self.tags.sort(key=lambda x: 0-x[2])
        print self.tags[0]
        print self.tags[1]
        print self.tags[2]
        print self.tags[3]
        print self.tags[4]
        print self.tags[5]
        print self.tags[6]
        print self.tags[7]

