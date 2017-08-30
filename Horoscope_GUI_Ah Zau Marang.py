# Titel: 161 Horoskop
# Författare: Ah Zau Marang
# Datum: 2014-08-25
#
# Skriv ett program som utfärdar ett ”personligt” horoskop baserat på en persons födelsedata.

from tkinter import *   #importerar modul(tkinter)
import os   #importerar modul(os)
import random   #importerar modul(random)


#En klass som beskriver ett grafiskt användargränssnitt för programmet.
class Applikation(Frame):
    # Konstruktorn, initierar attributen master, file1-9 och listor.
    def __init__(self, master, file1, file2, file3, file4, file5, file6, file7, file8, file9):
        Frame.__init__(self, master) #kopplar klassen(Frame) med konstruktorn
        self.grid() #skapar rutnät på skärmen
        self.create_widgets()   #kopplar metoden till ram på skärmen
        self.horoskopFil_barn = file1
        self.egenskapFil_barn = file4
        self.konsekvensFil_barn = file7
        
        self.horoskopFil_ungdom = file2
        self.egenskapFil_ungdom = file5
        self.konsekvensFil_ungdom = file8
        
        self.horoskopFil_vuxen = file3
        self.egenskapFil_vuxen = file6
        self.konsekvensFil_vuxen = file9
        
        self.egenskap = list()
        self.konsekvens = list()
    
        self.ekonomi = list()
        self.love = list ()
        self.utbildning = list()
        self.livstil = list()
        self.personlig = list()
        
        
        
    # Skapar widgets med hjälp av klasser från modul(tkinter) och placerar dem på skärmen.
    def create_widgets(self):
        self.photo = PhotoImage(file="image1.gif")  #upladdar en bild fil.
        self.label1=Label(self, image=self.photo)   #skapar en etikett med en bild i.
        self.label1.grid(columnspan=700, row=0, sticky=W)   #placering av etiketten på skärmen.
        
        self.label2=Label(self,text='Mata in födelsedata(siffror) för att se spådomar just för dig!', fg='black')    #skapar en etikett med en text
        self.label2.grid(columnspan=700, row=1, sticky=W)   #placering av etiketten på skärmen.
        
        self.label3=Label(self, text='Välkommen till 161 Horoskop!', fg='brown', font=('Verdana', 20, 'bold'))  #skapar en etikett med en rubrik
        self.label3.grid(columnspan=700, row=0, sticky=E)   #placering av rubriken på skärmen.

        self.entry1 = Entry(self,textvariable=yearVar)  #skapar en inträde till inmatning för år.
        self.entry1.grid(row=2,column=0, sticky=W)  #placering av inträden på skärmen.

        self.entry2 = Entry(self, textvariable=monthVar)    #skapar en inträde till inmatning för månad.
        self.entry2.grid(row=2, column=1, sticky=W) #placering av inträden på skärmen.

        self.entry3 = Entry(self, textvariable=dayVar)  #skapar en inträde till inmatning för månad.
        self.entry3.grid(row=2, column=2, sticky=W) #placering av inträden på skärmen.

        def quit(): #en metod som avslutar programkörning.
            print('Hejdå, välkommen åter!')
            os._exit(99)
        
        self.button2=Button(self,text='Quit >>', command=quit).grid(row=5, sticky=W)    #skapar en knapp med text(Quit >>) som är kopplad till metoden(quit)
        
        self.button1=Button(self,text='OK >>', command=self.utskrift).grid(row=3,column=0, sticky=W)   #skapar en knapp med text(OK >>) som är kopplad till metoden(utskrift)

        self.text = Text(self)  # skapar en textfält.
        self.text.config(font=('arial', 11, 'normal'), fg='green')     #initierar teckensnitt i textfältet.     
        self.text.config(width=80, height=15)   #skapar textfälts storlek.
        self.text.tag_configure('color', foreground='red', font=('Tempus Sans ITC', 12))    #skapar teckensnitt för text i textfältet med nyckelord(color)
        self.text.tag_configure('big', font=('Verdana', 15, 'bold'))    #skapar teckensnitt för text i textfältet med nyckelord(color)
        self.text.grid(columnspan=700, row=4, sticky=W) #placerar textfältet på skärmen.

    # en metod som kontrollerar födelsedatum och skriver ut uttalanden, en slumpmässigt sammansatt spådom och fel meddelande i textfältet på skärmen.
    def utskrift(self):
        if yearVar.get().isdigit() == False or monthVar.get().isdigit() == False or dayVar.get().isdigit() == False: #kontrollerar om inmattning är bara siffror.
            self.text.delete(0.0, END)  #rensar textfältet.
            self.text.insert(0.0, 'Du har matat in ett felaktigt födelsedatum. Försök igen!', 'color')   #infoga/skriver ut texten i textfältet.
        else:
            ar = int(yearVar.get()) #konverterar inmatat årtal och lagrar det till variabel(ar).
            manad = int(monthVar.get()) #konverterar inmatat månadtal och lagrar det till variabel(manad).
            dag = int(dayVar.get()) #konverterar inmatat dagtal och lagrar det till variabel(dag).
            length = len(yearVar.get()) #lagrar längden av strängen(årtal) till variabel(ar).
            self.older = 2014 - ar #räknar ut ålder och lagrar det till en attribut(older).
            self.index = ar + manad + dag    #skapar ett index genom att plussa år-, månad- och dagtal.
            if ar == 0 or manad == 0 or dag == 0:   #if-sats som kontrollerar som ar <= 0 or manad <= 0 or dag <= 0.
                self.text.delete(0.0, END)  #rensar textfältet.
                self.text.insert(0.0,'Du har matat in ett felaktigt födelsedatum. Försök igen!', 'color')   #infoga/skriver ut texten i textfältet.
            else:
                if length == 4 and ar <= 2014:   #if-sats som kontrollerar om årtal är ett fyrsiffrigt årtal och mindre eller lika med 2014.
                    if manad <= 12:   #if-sats som kontrollerar om månadtal är mindre eller lika med 12.
                        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    #en lista med antal dagar för vanliga månader.
                        i = manad - 1   #räknar ut ett tal, ett mindre än inmatat månadtal.
                        if self.older < 0:  #if-sats som kontrollerar om ålder är mindre än 0.
                            self.text.delete(0.0, END)  #rensar textfältet.
                            self.text.insert(0.0,'Du har matat in ett felaktigt födelsedatum. Försök igen!', 'color')   #infoga/skriver ut texten i textfältet.
                        elif ar == 2014 and manad == 8 and dag > 25:    #elif som kontrollerar om årtal är lika med 2014, månad = 8 och dag > 25.
                            self.text.delete(0.0, END)  #rensar textfältet.
                            self.text.insert(0.0,'Du har matat in ett felaktigt födelsedatum. Försök igen!', 'color')   #infoga/skriver ut texten i textfältet.
                        elif dag > month[i] and dag == 29:  #elif som kontrollerar om dag > month[i] and dag = 29.
                            if ar % 400 == 0:   #if-sats som kontroller om det är skottår.
                                self.uttalandenUtskrift()
                            else:
                                self.text.delete(0.0, END)  #rensar textfältet.
                                self.text.insert(0.0,'Du har matat in ett felaktigt födelsedatum. Försök igen!', 'color')    #infoga/skriver ut texten i textfältet.
                        elif dag < month[i]:    #elif som kontrollerar om dag < month[i].
                            self.uttalandenUtskrift()
                        else:
                            self.text.delete(0.0, END)
                            self.text.insert(0.0,'Du har matat in ett felaktigt födelsedatum. Försök igen!', 'color')
                    else:
                        self.text.delete(0.0, END)
                        self.text.insert(0.0,'Du har matat in ett felaktigt födelsedatum. Försök igen!', 'color')
                else:
                    self.text.delete(0.0, END)
                    self.text.insert(0.0,'Du har matat in ett felaktigt årtal. Försök igen!', 'color')


    

    #en metod som kontrollerar åldersgrupper och skapar en horoskopskatalog med uttalanden som finns i fil.
    def uttalanden(self):
        self.egenskaper = [self.ekonomi, self.love, self.utbildning, self.livstil, self.personlig]  #initierar en lista(egenskaper) med listor i.
        if self.older >=0 and self.older <= 15:     #if-sats som kontroller om attributen, older, >=0 and <= 15.
            filename = self.horoskopFil_barn   #lagrar attributen(horoskopFil_b) till variabeln(filename).
        elif self.older >15 and self.older <=25:    #elif som kontroller om self.older >15 and self.older <=25.
            filename = self.horoskopFil_ungdom   #lagrar attributen till variabeln(filename).
        elif self.older >25:    #if-sats som kontroller om self.older >25.
            filename = self.horoskopFil_vuxen   #lagrar attributen till variabeln(filename).

        start = 0
        file = open(filename, 'rU') #öppnar och läser filen(filename) och lagrar den till variabel(file).
        for line in file:   #for-sats som läser in varje rad i filen.
            mening = line.strip()   #lagrar varje rad till variabel(mening) genom att strippa.
            if mening != '':    #if-sats som kontrollerar om rad är tom.
                self.egenskaper[start].append(mening+'\n')  #adderar varje mening i en lista i listan(egenskaper).
            else:
                start += 1  #ökar variabel(start) med ett varje gång den läser in en tom rad.
        file.close()    #stänger filen.
        return self.egenskaper  #returnerar listan(egenskaper).

    # en metod som skriver ut uttallanden. 
    def uttalandenUtskrift(self):
        nummer = self.index      #lagrar indexet till variabel(nummer).
        ekonomi, love, utbildning, livstil, personlig =self.uttalanden()    #lagrar listor i listan(egenskaper) till variabler(ekonomi, love, utbildning, livstil, personlig) till variabel(nummer) genom att kalla de från metoden(uttalanden)
        ekonomiModulo = nummer % len(ekonomi)   #räknar ut modulo avseende på listan(ekonomi)
        loveModulo = nummer % len(love)   #räknar ut modulo avseende på listan(love)
        utbildningModulo = nummer % len(utbildning)   #räknar ut modulo avseende på listan(utbildning)
        livstilModulo = nummer % len(livstil)   #räknar ut modulo avseende på listan(livstil)
        personligModulo = nummer % len(personlig)   #räknar ut modulo avseende på listan(personlig)
        spadomText = self.spadomUtskrift()  #lagrar returvärdet från metoden(spadomUtskrift) till variabel(spadomText).
        self.text.delete(0.0, END)  #rensar textfältet.
        self.text.insert(0.0, spadomText)   #infoga/skriver ut variabel(spadomText) i textfältet.
        self.text.insert(0.0, "             *Dagens slumpmässigt spådom för dig*\n", 'big')   #infoga/skriver ut texten i textfältet.
        self.text.insert(0.0, personlig[personligModulo])   #infoga/skriver ut en mening från listan(personlig) i textfältet med hjälp av modulo värdet.
        self.text.insert(0.0, livstil[livstilModulo])   #infoga/skriver ut en mening från listan(livstil) i textfältet med hjälp av modulo värdet.
        self.text.insert(0.0, utbildning[utbildningModulo])   #infoga/skriver ut en mening från listan(utbildning) i textfältet med hjälp av modulo värdet.
        self.text.insert(0.0, love[loveModulo])   #infoga/skriver ut en mening från listan(love) i textfältet med hjälp av modulo värdet.
        self.text.insert(0.0, ekonomi[ekonomiModulo])   #infoga/skriver ut en mening från listan(ekonomi) i textfältet med hjälp av modulo värdet.
        self.text.insert(0.0, "             (Horoskop baserat på din födelsedata)\n", 'big')    #infoga/skriver ut texten i textfältet.
        del ekonomi[:]  #rensar allt innehåll i listan(ekonomi).
        del love[:]  #rensar allt innehåll i love(ekonomi).
        del utbildning[:]  #rensar allt innehåll i utbildning(ekonomi).
        del livstil[:]  #rensar allt innehåll i livstil(ekonomi).
        del personlig[:]  #rensar allt innehåll i personlig(ekonomi).


    # en metod som beskriver en slumpmässigt sammansatt spådom.
    def spadomUtskrift(self):

        if self.older >=0 and self.older <= 15:     #if-sats som kontroller om attributen, older, >=0 and <= 15.
            filename1=self.egenskapFil_barn   #lagrar attributen(egenskapFil_b) till variabeln(filename1).
            filename2=self.konsekvensFil_barn   #lagrar attributen(konsekvensFil_b) till variabeln(filename2).
        elif self.older >15 and self.older <=25:    #elif som kontroller om self.older >15 and self.older <=25.
            filename1=self.egenskapFil_ungdom    #lagrar attributen till variabeln(filename1).
            filename2=self.konsekvensFil_ungdom  #lagrar attributen till variabeln(filename2).
        elif self.older >25:    #elif som kontroller om self.older >25.
            filename1=self.egenskapFil_vuxen    #lagrar attributen till variabeln(filename1).
            filename2=self.konsekvensFil_vuxen  #lagrar attributen till variabeln(filename2).

        file = open(filename1, 'rU')    #öppnar och läser filen(filename1) och lagrar den till variabel(file).
        for line in file:   #for-sats som läser in varje rad i filen.
            mening = line.strip()   #lagrar varje rad till variabel(mening) genom att strippa.
            self.egenskap.append(mening)  #adderar varje mening i en lista i listan(egenskap).
        file.close()    #stänger filen.
        
        fileTwo = open(filename2, 'rU')
        for line in fileTwo:
            mening = line.strip()
            self.konsekvens.append(mening)
        file.close()
        
        lista1 = len(self.egenskap)     #lagrar längden av listan(egenskap) till variabel(lista1).
        lista2 = len(self.konsekvens)   #lagrar längden av listan(konsekvens) till variabel(lista1).
        egenskapTal = random.randrange(0,lista1)    #slumpar ett tal mellan 0 och lista1 och lagrar det till variabel(egenskapTal).
        konsekvensTal = random.randrange(0,lista2)    #slumpar ett tal mellan 0 och lista2 och lagrar det till variabel(konsekvensTal).
        spadom = 'Din ' + self.egenskap[egenskapTal] + ' förorsakar ' + self.konsekvens[konsekvensTal]      #lagrar en sträng med slumpade meningar från listor, egenskap och konsekvens.
        del self.egenskap[:]    #rensar allt innehål i listan(egenskap).
        del self.konsekvens[:]  #rensar allt innehål i listan(konsekvens).
        return spadom   #returnerar variabeln(spadom).



# -----Huvudprogram----------
        
#skapar fönster
root = Tk()

#modifierar root fönster
root.title("Horoskop") #ger fönstret en titel.   
root.geometry("700x450")    #avgör hur bredd och högd fönstret ska vara.

#initierar inmatat värden till strängar.
yearVar = StringVar()   #initierar inmatat värdet från inträdet(entry1) till sträng.
yearVar.set('åååå')     #visar texten(åååå) på inträdet(entry1).
monthVar = StringVar()  #initierar inmatat värdet från inträdet(entry2) till sträng.
monthVar.set('dd')      #visar texten(mm) på inträdet(entry2).
dayVar = StringVar()    #initierar inmatat värdet från inträdet(entry3) till sträng.
dayVar.set('dd')        #visar texten(dd) på inträdet(entry3).


#lagrar filer till variabler
horoskop_barn = 'horoskop_barn.txt'    #lagrar filen(horoskop_barn.txt) till en variabel(horoskop_b).
horoskop_ungdom = 'horoskop_ungdom.txt'
horoskop_vuxen = 'horoskop_vuxen.txt'

egenskap_barn = 'egenskap_barn.txt'
egenskap_ungdom = 'egenskap_ungdom.txt'
egenskap_vuxen = 'egenskap_vuxen.txt'

konsekvens_barn = 'konsekvens_barn.txt'
konsekvens_ungdom = 'konsekvens_ungdom.txt'
konsekvens_vuxen = 'konsekvens_vuxen.txt'

#skapar en objekt med klassen(Application) med parametrar i.
app = Applikation(root, horoskop_barn, horoskop_ungdom, horoskop_vuxen, egenskap_barn, egenskap_ungdom, egenskap_vuxen, konsekvens_barn,konsekvens_ungdom,konsekvens_vuxen)

#startar slinga
root.mainloop()


