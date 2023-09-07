import sys
import pandas as pd

# Initialisation d'un dictionnaire pour stocker les détails de chaque commande
commandes = {}

# Lire les lignes d'entrée depuis STDIN (standard input)
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Diviser la ligne en éléments
    codecde, points, qte, year, villecli, Nbcolis, cpcli, timbrecli, timbrecde = line.split('\t')

    # Convertir les points et la quantité en nombre flottant
    try:
        points = float(points)
        timbrecde = float(timbrecde)
        timbrecli = float(timbrecli)
        qte = float(qte)
        Nbcolis = int(Nbcolis)

    except ValueError:
        continue

    if codecde in commandes:
        commandes[codecde]['points'] += points * qte
        commandes[codecde]['total_lignes'] += 1
    else:
        commandes[codecde] = {'points': points * qte,
                                    'commande': {
                                        'year': year,
                                        'villecli': villecli,
                                        'Nbcolis': Nbcolis,
                                        'cpcli': cpcli,
                                        'timbrecli': timbrecli,
                                        'timbrecde': timbrecde,
                                    }, 'total_lignes': 1}

# Trier les commandes par somme des points dans l'ordre décroissant
commandes_triees = sorted(commandes.items(), key=lambda x: x[1]['points'], reverse=True)

# Sélection des 100 meilleures commandes
meilleures_commandes = commandes_triees[:100]

# Créez un DataFrame pandas avec les résultats
data = []

# Calculer le total des points ainsi que le total de ligne
total_points = 0
total_lignes = 0
for code, details in meilleures_commandes:
    total_points = details['points']
    total_lignes = details['total_lignes']

    cde = details['commande']
    year = cde['year']
    villecli = cde['villecli']
    Nbcolis = cde['Nbcolis']
    cpcli = cde['cpcli']
    timbrecli = cde['timbrecli']
    timbrecde = cde['timbrecde']

    data.append([code,  total_points, total_lignes,year, villecli, cpcli, Nbcolis, timbrecli, timbrecde])

    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.1f}".format(code, total_points, total_lignes, year, villecli, cpcli, Nbcolis, timbrecli, timbrecde))

columns = ['Code',  'Total Points','Total Lignes','Year', 'Ville Client','Code Postal', 'Nb Colis','Timbrecli', 'Timbrecde']

df = pd.DataFrame(data, columns=columns)

# Enregistrez le DataFrame au format Excel
output_file = '/datavolume1/resultats_2_1.xlsx'
df.to_excel(output_file, index=False)

# Enregistrez le DataFrame au format CSV
output_csv_file = '/datavolume1/data_2_1.csv'
df.to_csv(output_csv_file, index=False)