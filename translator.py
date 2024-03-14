import os.path
import string


class Translator:

    def __init__(self):
        self.dizionario={}

    def printMenu(self):
        numero = int(input("scegli un opzione: \n1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n5. Exit\n"))
        return numero

    def loadDictionary(self, dict):
        if os.path.exists(dict)!=True:
            raise ValueError("Errorazzo de Dio")
        with open(dict, 'r') as file:
            riga = file.readline()
            while riga != '':
                riga = riga.strip("\n")
                lista = riga.split(" ")
                if lista[0] not in self.dizionario:
                    self.dizionario[lista[0]] = lista[1]
                riga = file.readline()
        file.close()

    def handleAdd(self, entry):
        verifica=entry[1].split(" ")
        abba=""
        for i in range(0,len(verifica)):
            abba+=verifica[i]
        if entry[0].isalpha()==False or abba.isalpha()==False:
            raise ValueError('Errorazzo de Dio')
        if entry[0].lower() not in self.dizionario:
            self.dizionario[entry[0].lower()] = entry[1].lower()
        with open('dictionary.txt', 'w') as file:
            for i in self.dizionario:
                file.write(f'{i} {self.dizionario[i]}\n')
        file.close()

    def handleTranslate(self, query):
        if query.isalpha()!= True:
            raise ValueError('Errorazzo de Dio')
        if query.lower() not in self.dizionario:
            return "parola non trovata"
        return self.dizionario[query.lower()]

    def handleWildCard(self,query):
        query=f"D{query.lower()}D"
        lista=query.split("?")
        listazza=[]
        listazza_parole=[]
        if lista[0].isalpha()== False or lista[1].isalpha()==False:
            raise ValueError('Errorazzo de Dio')
        for i in string.ascii_lowercase:
            parola=f"{lista[0]}{i}{lista[1]}"
            parola =parola.rstrip("D").lstrip("D")

            if self.handleTranslate(parola)!="parola non trovata":
                listazza_parole.append(parola)
                listazza.append(self.handleTranslate(parola))
        final=""
        for i in range(0,len(listazza_parole)):
            final+=f"{listazza_parole[i]}: {listazza[i]}\n"
        return final.rstrip("\n")
