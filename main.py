import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")
scelta=t.printMenu()
while scelta!=5:
    if scelta==1:
        stringa=input("okay, quale parola devo aggiungere?\n")
        lista=stringa.split(" ")
        parte_due=''
        for i in range(1, len(lista)):
            parte_due+=f" {lista[i]}"
        tupla=[lista[0], parte_due.lstrip(" ")]
        t.handleAdd(tupla)
    elif scelta==2:
        stringa=input("okay, che parola devo tradurre?\n")
        print(f'{t.handleTranslate(stringa)}')
    elif scelta==3:
        risposta=t.handleWildCard(input("okay, che parola devo tradurre?\n"))
        if risposta=="":
            risposta="sei un coglione, non trovo nessuna parola"
        print(risposta)

    else:
        print("scegli una delle 5 opzioni")
    scelta=t.printMenu()



