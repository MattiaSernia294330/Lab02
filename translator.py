import string

import dictionary as dizionarietto
class Translator:

    def __init__(self):
        self.dizionario=dizionarietto.Dictionary()

    def printMenu(self):
        return "1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit"

    def loadDictionary(self, dict):
        with open(dict, 'r') as file:
            riga=file.readline()
            while riga!=''and riga !='\n':
                riga=riga.strip("\n")
                lista=riga.split(" ")
                self.dizionario.addWord(lista[0].lower(), lista[1].lower())
                riga=file.readline()
            file.close()

    def handleAdd(self, entry):
        a=True
        lista=entry.split(" ")
        for i in lista:
            if i.isalpha()==False:
                a=False
                break
        if a==False:
            print("scrivi solo parole non numeri o punti")
        parole=''
        for i in range(1,len(lista)):
            if i==1:
                parole=lista[i]
            else:
                parole+=" "+lista[i]
        self.dizionario.addWord(lista[0].lower(), parole.lower())

    def handleTranslate(self, query):
        if query.isalpha():
            return self.dizionario.translate(query.lower())
        return "devi usare solo lettere"

    def handleWildCard(self,query):
        stringa=''
        query=query.lower()
        counter=0
        for i in range(0,len(query)):
            if query[i]=='?':
                counter+=1
        for element in string.ascii_lowercase:
            query2=query.replace("?",element)
            if counter>1 or query2.isalpha()!=True:
                return "puoi usare solo un carattere speciale e deve essere <?>"
            if self.dizionario.translateWordWildCard(query2)!="la parola non esiste":
                stringa+=f"\n{query2}: {self.dizionario.translateWordWildCard(query2)}"
        if stringa!='':
            return stringa.lstrip("\n")
        return "non ci sono parole"
