import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    cde = line.split(',')

    # On teste si la ligne est bien remplie avec les 9 colonnes
    if len(cde) < 8:
        # Si le format n'est pas bon, alors on n'exécute pas les lignes suivantes
        status = "AN"
        print('%s\t%s' % (status, line))
        continue
    status = "OK"

    # Définir les en-têtes:
    code = cde[0].strip('"')
    total_points = cde[1].strip('"')
    total_lignes = cde[2].strip('"')
    year = cde[3].strip('"')
    villecli = cde[4].strip('"')
    cpcli = cde[5].strip('"')
    Nbcolis = cde[6].strip('"')
    timbrecli = cde[7].strip('"')
    timbrecde = cde[8].strip('"')

    # Convertir les points et la quantité en nombre flottant
    try:
        timbrecli = float(timbrecli)
    except ValueError:
        continue

    # Vérifier si timbrecli est " " ou "NULL"
    if timbrecli not in [' ', 'NULL', 0]:
        continue

    # Vérifier si le département est 53, 61 ou 28
    if cpcli not in ['53', '61', '28']:
        continue  # On passe à la ligne suivante

    # Afficher les informations sous forme de tabulation
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(code, total_points, total_lignes, year, villecli, Nbcolis, cpcli, timbrecde))

