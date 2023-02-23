class Rodokmen:
    # Reprezentuje rodokmen určité osoby

    koren = None # Kořen rodokmenu, tedy osoba, pro kterou se vypisuje

    # Konstruktor
    def __init__(self, koren):
        self.koren = koren

    def vypis_osobu_a_predky(self, osoba):
        if osoba:
            print(osoba)
            self.vypis_osobu_a_predky(osoba.otec)
            self.vypis_osobu_a_predky(osoba.matka)

    def vypis(self):
        print("Rodokmen pro osobu {0}".format(self.koren))
        self.vypis_osobu_a_predky(self.koren)

