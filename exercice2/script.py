def filtrer_prenoms(prenoms):
    prenoms_valides = []
    for prenom in prenoms:
        if prenom.startswith('A'):
            print(f"{prenom} : prénom valide")
            prenoms_valides.append(prenom)
        else:
            print(f"{prenom} : prénom invalide")
    return prenoms_valides

# Exemple d'utilisation
liste_prenoms = ["Alice", "Bob", "Anna", "Charles", "Amélie"]
prenoms_valides = filtrer_prenoms(liste_prenoms)
print("Prénoms valides :", prenoms_valides)
