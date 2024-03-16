class Dictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, parola1, parola2):
        if parola1 not in self.dictionary:
            self.dictionary[parola1] = parola2
        else:
            self.dictionary[parola1]+=" "+parola2

    def translate(self, parola):
        if parola not in self.dictionary:
            return "la parola non esiste"
        return self.dictionary[parola]

    def translateWordWildCard(self, parola):
        if parola not in self.dictionary:
            return "la parola non esiste"
        return self.dictionary[parola]