import translator as tr

t = tr.Translator()
continua=True
t.loadDictionary("dictionary.txt")
while continua==True:

    t.printMenu()

    testo = input(f"scegli un opzione:\n{t.printMenu()}\n")

    # Add input control here!

    if int(testo) == 1:
        print("okay, che parola devo aggiungere?")
        parole = input()
        t.handleAdd(parole)
    if int(testo) == 2:
        traduzione=input("okay, che parola devo cercare?\n")
        print(t.handleTranslate(traduzione))
    if int(testo) == 3:
        traduzione=input("okay, che parola con ? devo cercare\n")
        print(t.handleWildCard(traduzione))
    if int(testo) == 4:
        continua=False


