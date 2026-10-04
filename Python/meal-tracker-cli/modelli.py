OBIETTIVI_STANDARD = {
    "carne-bianca": 2,
    "carne-rossa": 1,
    "pesce": 2,
    "uova": 1,
    "latticini": 1,
    "legumi": 3,
}
GIORNI = ["lunedi", "martedi", "mercoledi", "giovedi", "venerdi", "sabato", "domenica"]
MOMENTI = ["pranzo", "cena"]


class DatoNonValido(ValueError):
    pass


class Bambino:
    def __init__(self, nome, scuola=""):
        # salva nome e scuola
        self.nome = nome
        self.scuola = scuola
        # crea il dizionario dei pasti, vuoto
        self.pasti = {}
        # crea gli obiettivi come copia di OBIETTIVI_STANDARD
        self.obiettivi = OBIETTIVI_STANDARD.copy()
        

    def aggiungi_pasto(self, giorno, momento, categoria):
        # controlla che giorno, momento e categoria siano validi
        # se non lo sono, solleva DatoNonValido con un messaggio chiaro
        # altrimenti salva il pasto

        if not all(isinstance(v, str) for v in (giorno, momento, categoria)):
            raise DatoNonValido("giorno, momento e categoria devono essere testi")
        if giorno not in GIORNI:
            raise DatoNonValido("Il giorno inserito non è valido") 
        if momento not in MOMENTI:
            raise DatoNonValido("Il tipo di pasto inserito non è valido") 
        if categoria not in self.obiettivi:
            raise DatoNonValido("La categoria inserita non è valida") 
        
        self.pasti[(giorno, momento)] = categoria

    def conteggi(self):
        # restituisce {categoria: quante_volte}
        risultato = {categoria: 0 for categoria in self.obiettivi}
        for categoria in self.pasti.values():
            risultato[categoria] += 1
        return risultato

    def mancanti(self):
    # restituisce {categoria: quante_ne_mancano}, solo per quelle dove manca qualcosa
        conteggi = self.conteggi()
        risultato = {}
        for categoria, obiettivo in self.obiettivi.items():
            # calcola quante ne mancano
            mancano = obiettivo - conteggi[categoria]
            # se è maggiore di zero, aggiungi la categoria a risultato
            if mancano > 0:
                risultato[categoria] = mancano
        return risultato
    
    def suggerimento(self):
        # restituisce una lista di al massimo 2 categorie, quelle con più "mancanti"
        mancanti = self.mancanti()
        ordinate = sorted(mancanti, key=lambda categoria: mancanti[categoria], reverse=True) # le categorie ordinate dal numero di mancanti più alto
        return ordinate[:2]       # solo le prime 2


if __name__ == "__main__":
    anna = Bambino("Anna")
    anna.aggiungi_pasto("lunedi", "pranzo", "pesce")
    print(anna.conteggi())
    print(anna.mancanti())
    print(anna.suggerimento())