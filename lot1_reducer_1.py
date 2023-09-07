import sys

current_ville = None
current_cmde = None
current_annee = None
current_objet = None
results = {}

for line in sys.stdin:
    line = line.strip()
    mapper = line.split(',')

    if len(mapper) == 0:
        continue

    if mapper[0] == "AN":
        print(line)
        continue
    else:
        ville = mapper[1]
        cmde = mapper[2]
        annee = mapper[3]
        codobj_libobj = mapper[4] + "-" + mapper[5]
        qte_str = mapper[7]
        tailleobj = mapper[8]

        try:
            qte = int(qte_str)
        except ValueError:
            continue

        if current_ville != ville or current_cmde != cmde or current_annee != annee or current_objet != codobj_libobj:
            results.setdefault(ville, {}).setdefault(cmde, {}).setdefault(annee, {}).setdefault(codobj_libobj, {}).setdefault(tailleobj, 0)
        results[ville][cmde][annee][codobj_libobj][tailleobj] += qte
        
        current_ville = ville
        current_cmde = cmde
        current_annee = annee
        current_objet = codobj_libobj

# Filtrer les résultats en ne gardant que les quantités > 5
filtered_results = {}
for ville, cmdes in results.items():
    for cmde, annees in cmdes.items():
        for annee, objets in annees.items():
            for objet, tailles in objets.items():
                for taille, quantite in tailles.items():
                    if quantite > 5:
                        filtered_results.setdefault(ville, {}).setdefault(cmde, {}).setdefault(annee, {}).setdefault(objet, {}).setdefault(taille, quantite)

# Créer un dictionnaire pour stocker le nombre de commandes par ville, par année et le détail de la commande
final_results = {}

# Parcourir les résultats filtrés
for ville, cmdes in filtered_results.items():
    for cmde, annees in cmdes.items():
        for annee, objets in annees.items():
            for objet, tailles in objets.items():
                for taille, quantite in tailles.items():
                    if ville not in final_results:
                        final_results[ville] = {}
                    if annee not in final_results[ville]:
                        final_results[ville][annee] = {'nombre_commandes': 0, 'details_commandes': []}
                    final_results[ville][annee]['nombre_commandes'] += 1

                    # Créer une liste d'objets avec nom, taille et quantité
                    details_objets = []
                    if taille != "NULL":
                        details_objets.append("{objet}-{taille}-{quantite}".format(objet = objet, taille = taille, quantite = quantite))
                    else:
                        details_objets.append("{objet}-{taille}-{quantite}".format(objet = objet, taille = "Taille unique", quantite = quantite))
                    # Ajouter le détail de la commande à la liste des détails
                    final_results[ville][annee]['details_commandes'].append({'numero_commande': cmde, 'objets': details_objets})

output_lines = []

for key, value in final_results.items():
    ville = key
    for annee, info in value.items():
        nombre_commandes = info['nombre_commandes']
        details_commandes = info['details_commandes']
        
        output_line = "{ville}, {annee}, {nombre_commandes}, ".format(ville = ville, annee = annee, nombre_commandes = nombre_commandes)
        for detail_commande in details_commandes:
            numero_commande = detail_commande['numero_commande']
            objets = "".join(detail_commande['objets'])
            output_line += "{numero_commande}, {objets}".format(numero_commande = numero_commande, objets = objets)
        
        output_lines.append(output_line)

# Imprimer toutes les lignes de sortie en une seule fois
for line in output_lines:
    print(line)