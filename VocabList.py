# -*- coding: utf-8 -*-
# VocabList.py
# Author: Riley Rettig
# Date created: Jan 28 2017
# Date last edited: Jan 28 2017

class VocabList:
    
    #need attribute references for terms and definitions
    def __init__(self):
        self.terms = []
        print("Terms?:\n (Enter empty when finished)")
        while True:
            term = input()
            if term!="":
                self.terms.append(term)
            else:
                break

        self.defs = []
        print("Definitions?:\n (Enter empty when finished)")
        while True:
            defin = input()
            if defin != "":
                self.defs.append(defin)
            else:
                break

        
    
        
def main():
    #terms = ["a", "b", "c"]
    #defs = ["d", "e", "f"]
    vocab = VocabList()
    print ("Terms: " + str(vocab.terms))
    print ("Definitions: " + str(vocab.defs))
    
if __name__ == '__main__':
    main()
    
