#Parte 1
Titolo="Delitto e castigo"
Autore="Dostoevskij"
Numero_Copie_Disponibili=100
Prezzo_Medio=14.99
Disponibile=True
print(f"Titolo: {Titolo} , Autore: {Autore} , Copie: {Numero_Copie_Disponibili} , Prezzo Medio {Prezzo_Medio} $ , Disponibilita: {Disponibile}")
#Parte 2
Libreria_5=[
    "1984","Notti Bianche","Il Sosia","Il Giocatore","Delitto e Castigo"
]
copie_libro={"1984":5,"Notti Bianche":12,"Il Giocatore":1,"Il Sosia":4,"Delitto e Castigo":10}
utenti_registrati={"Vittoria","Peppe","Muffin"}
#Parte 3
class Libro:
    def __init__(self,titolo,autore,anno,copie_disponibili):
        self.titolo=titolo
        self.autore=autore
        self.anno=anno
        self.copie_disponibili=copie_disponibili
    def info(self):
        print(f"Titolo: {self.titolo} , Autore: {self.autore} , Anno: {self.anno} , Copie Disponibili: {self.copie_disponibili}")

L=Libro("Notti bianche","Dostoevskij",1848,14)
L.info()
L2=Libro("Attack on titan","Isayama",2009,10)
L2.info()

class Utente:
    def __init__(self,nome,eta,id_utente):
        self.nome=nome
        self.eta=eta
        self.id_utente=id_utente
    def scheda(self):
        print(f"Nome: {self.nome}, Eta: {self.eta}, Id_utente:{self.id_utente}" )            

class Prestito:
    def __init__(self,utente,libro,giorniprestito):
        self.utente=utente
        self.libro=libro
        self.giorniprestito=giorniprestito
    def dettagli(self):
        print(f"L utente {self.utente.nome} ha preso in prestito {self.libro.titolo} per {self.giorniprestito} giorni")


utente_test= Utente("Vittoria",19,"ID_001")
libro_test= Libro("Notti bianche","Dostoevskij",1848,12)     

nuovo_prestito=Prestito(utente_test,libro_test,14)
nuovo_prestito.dettagli()
#Parte 4

def presta_libro(utente,libro,giorni):
    if libro.copie_disponibili>=1:
        libro.copie_disponibili-=1
        return Prestito(utente,libro,giorni)
    else:
        print("ERRORE")

libro_a = Libro("Notti Bianche", "Dostoevskij", 1848, 3)
libro_b = Libro("1984", "Orwell", 1949, 1)
libro_c = Libro("Il Giocatore", "Dostoevskij", 1866, 0)

utente_1 = Utente("Vittoria", 19, "ID_001")
utente_2 = Utente("Peppe", 23, "ID_002")
utente_3 = Utente("Diego", 22, "ID_003")

prestito_1=presta_libro(utente_1,libro_a,14)
if prestito_1:
    prestito_1.dettagli()

prestito_2=presta_libro(utente_2,libro_b,7)
if prestito_2:
    prestito_2.dettagli()

prestito_3=presta_libro(utente_3,libro_c,30)
if prestito_3:
    prestito_3.dettagli()

libro_a.info()
libro_b.info()
libro_c.info()

if prestito_1:
    prestito_1.dettagli()
if prestito_2:
    prestito_2.dettagli()



