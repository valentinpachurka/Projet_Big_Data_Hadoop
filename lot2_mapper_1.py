import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    cde = line.split(',')

    # On teste si la ligne est bien remplie avec les 25 colonnes
    if len(cde) < 25:
        # Si le format n'est pas bon, alors on n'exécute pas les lignes suivantes
        status = "AN"
        print('%s\t%s' % (status, line))
        continue
    status = "OK"

    # Définir les en-têtes:
    cpcli = cde[4].strip('"')
    villecli = cde[5].strip('"')
    codecde = cde[6].strip('"')
    datecde = cde[7].strip('"')
    timbrecli = cde[8].strip('"')
    timbrecde = cde[9].strip('"')
    Nbcolis = cde[10].strip('"')
    qte = cde[15].strip('"')
    points = cde[20].strip('"')

    # Vérifier si le code de commande est ' ' ou 'NULL', et si c'est le cas, passer à la ligne suivante
    if codecde in [' ', 'NULL']:
        continue

    # Vérifier si timbrecde est " " ou "NULL"
    if timbrecde in [' ', 'NULL']:
        continue

    # Vérifier si la quantité  est ' ' ou 'NULL', et si c'est le cas, passer à la ligne suivante
    if qte in [' ', 'NULL', 0]:
        continue

    # Vérifier si points est 'NULL' ou ' ', si c'est le cas, passer à la ligne suivante
    if points in ['NULL', ' ']:
        continue

    try:
        points = float(points)
    except ValueError:
        continue

    # Extraire la date complète si elle n'est pas vide
    if datecde:
        # Extraire l'année de la date
        year = datecde.split('-')[0]

        # Vérifier si l'année est entre 2006 et 2016 et si elle est un nombre
        if year.isdigit() and 2006 <= int(year) <= 2016 and points >= 0.0 :

            # Extraire les deux premiers chiffres du code postal (cpcli)
            cpcli = cpcli[:2] if len(cpcli) >= 2 else ''

            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(codecde, points, qte, year, villecli, Nbcolis, cpcli,
                                                              timbrecli, timbrecde))
