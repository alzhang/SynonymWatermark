# load wordnet file
# parse wordnet file
import re

filename = "core-wordnet.txt"

def loadWordNet():
  #read file
  f = open(filename,'r')

  wordnet = {}
  wordnet["a"] = {}
  wordnet["n"] = {}
  wordnet["v"] = {}


  for line in f:
    #format
    #(pos) [(word)%#:##:##::] [(word_again)] syn,syn,syn
    matchObj = re.match( r'([anv]) \[(.*)%.*\] \[(.*)\](.*)',line)#\[(.*)\] (?:([^,]), )*',line)
    pos = matchObj.group(1)
    word = matchObj.group(2)
    word2 = matchObj.group(3)
    syn = matchObj.group(4)
    syn = syn.strip().split(", ")
    
    if not(word in wordnet[pos]):
      wordnet[pos][word] = []
    wordnet[pos][word].extend(syn)
      
  f.close()
  return wordnet


def getSynonym(net,word,pos):
  if not(word in net[pos]):
    return None
  for syn in net[pos][word]:
    if len(syn) > 0:
      return syn
  return None
  #pick the most common of the words

net = loadWordNet()
