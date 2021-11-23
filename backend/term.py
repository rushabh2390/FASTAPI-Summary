class Term:
    def __init__(self):
        self.stem_word=None
        self.words=[]
        self.grammar_term=[]
        self.grammar_word_count=[]
        self.count=0
        self.word_weight=0.0
        self.index = []
    def setproperty(self,st, word, gterm):
        self.stem_word = st
        self.words.append(word)
        self.grammar_term.append(gterm)
        self.grammar_word_count.append(1)
        self.count = 1
    def display(self):
        print("word",self.stem_word)
        print("word-list",self.words)
        print("grammar term",self.grammar_term)
        print("grammar term count", self.grammar_word_count)
        print("total count", self.count)
        print("weight",self.word_weight)
        print("indexes",self.index)

    def getword(self):  
        # return (", ".join(self.words))
        return self.words

    def addindex(self,ind):
        self.index.append(ind)