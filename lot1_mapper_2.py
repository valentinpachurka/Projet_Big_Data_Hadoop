import sys


for place, line in enumerate(sys.stdin):
    if place != 0: 
        line = line.strip()
        words = line.split(',')

        if len(words) < 25:
            print("AN\t%s" % line)
            continue

        if words[7] != '"datcde"': 
            codeclient = words[0].strip('"')
            nomclient = words[2].strip('"')
            prenomclient = words[3].strip('"')
            codepostalclient = words[4].strip('"')[:2]
            villeclient = words[5].strip('"')
            codecommande = words[6].strip('"')
            datecommande_str = words[7].strip('"').split("-")
            nbcolis = words[10].strip('"')

            # enlève les lignes avec date manquante ou pas bon format
            if len(datecommande_str) >= 1 and datecommande_str[0].isdigit():
                anneecommande = int(datecommande_str[0])
            else:
                continue 
        
            # Vérifier si nbcolis peut être converti en int (entier)
            try:
                nbcolis_int = int(nbcolis)
            except ValueError:
                continue
            
            # Comparer les dates
            if anneecommande >= 2008:
                print("OK\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (codeclient, nomclient, prenomclient, codepostalclient, villeclient, codecommande, anneecommande, nbcolis))

