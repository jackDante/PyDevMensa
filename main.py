# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



#LEZIONE 1 -----------------------------------------
def concatenazionestringhe(stringa1, stringa2, stringa3):
    somma = 0
    print(somma)


def ciaomondo():
    print("ciaomondo!")


def funzione_somma(x, y, z):
    somma = 4
    ciaomondo()
    print(somma)



def print_funzione():
    x = "Hi"  # string
    x = 10  # int
    x = True  # boolean
    x = 2.5  # float
    x = x + 20
    #stampa a video la variabile x
    print(x)
    print(type(x))


# programma che illustra il controllo If
def condizioneIF():
    i = 10
    if (i > 15):
        print("10 is less than 15")
    print("I am Not in if")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_funzione()
    #concatenazionestringhe("Ciao   ", "Mondo!")
    #a = input()
    #print(a)
    concatenazionestringhe("C", "i", "ao")
    funzione_somma(1, 2, 3)
    concatenazionestringhe(1, 2, 3)
    funzione_somma("C", "i", "ao")
