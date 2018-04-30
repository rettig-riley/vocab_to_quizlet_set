"""VocabList.py
Creates a VocabList object by asking the user for terms and definitions.

Author: Riley Rettig
Date created: Jan 28 2017
Date last edited: April 30 2017
"""


class VocabList:
    def __init__(self):

        self.terms = []
        print("Terms?:\n (Enter empty when finished)")
        while True:
            term = input()
            if term != "":
                self.terms.append(term)
            else:
                break

        self.definitions = []
        print("Definitions?:\n (Enter empty when finished)")
        while True:
            definition = input()
            if definition != "":
                self.definitions.append(definition)
            else:
                break


def main():
    vocab = VocabList()
    print("Terms: " + str(vocab.terms))
    print("Definitions: " + str(vocab.definitions))
    
if __name__ == '__main__':
    main()
