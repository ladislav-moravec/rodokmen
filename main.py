from osoba import Osoba
from rodokmen import Rodokmen

# Vytvoření a navázání osob
abraham = Osoba("Abraham Simpson", None, None)
penelope = Osoba("Penelope Olsen", None, None)
pan = Osoba("Pan Bouvier", None, None)
jackie = Osoba("Jackie Bouvier", None, None)
herb = Osoba("Herb Powers", abraham, penelope)
homer = Osoba("Homer Simpson", abraham, penelope)
marge = Osoba("Marge Simpson", pan, jackie)
selma = Osoba("Selma Bouvier", pan, jackie)
bart = Osoba("Bart Simpson", homer, marge)
# Vytvoření vypsání rodokmenu
rodokmen_barta = Rodokmen(bart)
rodokmen_homera = Rodokmen(homer)
rodokmen_barta.vypis()
print()
rodokmen_homera.vypis()