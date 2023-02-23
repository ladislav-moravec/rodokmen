class Osoba:
    # Třída reprezentuje osobu v rodokmenu

    otec = None
    matka = None
    jmeno = None

    # Kontstruktor
    def __init__(self, jmeno, otec, matka):
        self.jmeno = jmeno
        self.otec = otec
        self.matka = matka

    # Vrátí textovou reprezentaci osoby
    def __str__(self):
        return self.jmeno
