import sys

status = None

# input comes from STDIN (standard input)
for place, line in enumerate(sys.stdin):
    if place != 0:
    # On retire les espaces avant et après la ligne
        line = line.strip()

        # Chaque ligne se compose de 25 colonnes : 
        # codecli   genrecli    nomcli  prenomcli   cpcli
        # villecli  codcde    datcde  timbrecli   timbrecde
        # Nbcolis   cheqcli   barchive    bstock  codobj
        # qte   Colis libobj  Tailleobj   Poidsobj
        # points  indispobj libcondit prixcond    puobj

        # On découpe cette ligne d'informations en fonction des tabulations
        infos = line.split(',')

        # On teste si la ligne est bien remplie avec les 25 colonnes
        if len(infos) < 25:
            # Si le format n'est pas bon, alors on n'exécute pas les lignes suivantes
            status = "AN"
            print('%s\t%s' % (status, line))
            continue
        status = "OK"

        # On récupère les infos qui nous intéresse :
        # Le nombre de commande, 
        # la ville, le département (pour filtrer surla Mayenne (53) )
        # codobj, libobj, qte
        nb_com = infos[10].strip('"')
        ville_brut = infos[5].strip('"')
        if "SAINT" in ville_brut:
            ville = ville_brut.replace("SAINT", "ST")
        else:
            ville = ville_brut
        cmde = infos[6].strip('"')
        codobj = infos[14].strip('"')
        libobj = infos[17].strip('"')
        tailleobj = infos[18].strip('"')
        if infos[15] != "NULL":
            qte = int(infos[15].strip('"').strip('"'))
        else:
            continue
        # On découpe le code postal pour récupérer les 2 premiers chiffres
        dep_all = infos[4].strip('"')
        dep = dep_all[0:2]
        # On découpe la date pour récupérer l'année, en fonction du "-"
        date_split = infos[7].strip('"').split("-")
        if len(date_split) >= 1 and date_split[0].isdigit():
            annee = int(date_split[0])
        else:
            continue
        # On récupère les informations qui ne concernent que la Mayenne (53) 
        # et depuis 2010
        if  annee >= 2010 and dep == "53":
            print('%s,%s,%s,%s,%s,%s,%s,%s,%s' % (status, ville, cmde, annee, codobj, libobj, nb_com, qte, tailleobj))