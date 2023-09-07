import sys

departements_num = { '53': 'MAYENNE',
                '72': 'SARTHE',
                '49': 'MAINE ET LOIRE'
}

for place, line in enumerate(sys.stdin):
    if place != 0: 
        line = line.strip()
        words = line.split(',')

        if len(words) < 25:
            print("AN\t%s" % line)
            continue

        if words[15] != "NULL" and words[7] != "NULL": 
            code_postal_client = words[4].strip('"')[:2]
            date_commande_str = words[7].strip('"').split(' ')[0]
            annee_commande = words[7].strip('"').split('-')
            code_objet = words[14].strip('"')
            quantite_objet = int(words[15].strip('"'))
            lib_objet = str(words[17].strip('"'))
            taille_objet = str(words[18].strip('"'))

            if len(annee_commande) >= 1 and annee_commande[0].isdigit():
            # enlève les lignes avec date manquante ou pas bon format
                annee_commande = int(annee_commande[0])
            else:
                continue 
            if annee_commande > 2003:

                if taille_objet != "NULL":
                    lib_unique_objet = code_objet + ' - ' + lib_objet + ' - ' + taille_objet
                else:
                    lib_unique_objet = code_objet + ' - ' + lib_objet

                if code_postal_client in departements_num:
                    nom_departement = departements_num[code_postal_client]
                    departements = '%s(%s)' % (nom_departement, code_postal_client)
                    print("OK\t%s\t%s\t%s\t%s" % (departements, annee_commande, lib_unique_objet, quantite_objet))
