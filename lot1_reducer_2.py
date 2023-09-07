import sys
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


clients_data = {}

# Parcours des lignes en entrée
for line in sys.stdin:
    line = line.strip()
    mapper = line.split('\t')

    # Ignorez les lignes vides ou celles commençant par 'AN'
    if len(mapper) == 0 or mapper[0] == 'AN':
        continue

    else:
        codeclient = mapper[1]
        nomclient = mapper[2]
        prenomclient = mapper[3]
        codepostalclient = mapper[4]
        villeclient = mapper[5]
        codecommande = mapper[6]
        anneecommande = int(mapper[7])
        nbcolis = int(mapper[8])

        # Gestion des données client
        # Si le codeclient existe dans le dictionnaire, ajouter la commande associée
        if codeclient in clients_data:
            if codecommande not in clients_data[codeclient]['commandes']:
                clients_data[codeclient]['commandes'].append(codecommande)
                clients_data[codeclient]['nbcolis'] += nbcolis

            if codecommande not in clients_data[codeclient]['nbcolis_par_commande']:
                clients_data[codeclient]['nbcolis_par_commande'][codecommande] = nbcolis


        # Sinon, créer une nouvelle entrée pour le client
        else:
            clients_data[codeclient] = {"codeclient" :codeclient,
                                        'nom': nomclient,
                                        'prenom': prenomclient,
                                        'codepostal': codepostalclient,
                                        'ville': villeclient,
                                        'commandes': [codecommande], 
                                        'nbcolis': nbcolis,
                                        'nbcolis_par_commande': {codecommande: nbcolis}
                                        }

# Calcul de l'écart type du nombre de colis par commande par client
for data in clients_data.values():
    colis_per_commande = list(data['nbcolis_par_commande'].values())

    if len(colis_per_commande) > 1:
        data['ecart_type_colis_par_commande'] = statistics.stdev(colis_per_commande)
    else:
        data['ecart_type_colis_par_commande'] = 0


# Trier les clients en fonction du nombre de commandes uniques (dans l'ordre décroissant)
sorted_clients = sorted(clients_data.values(), key=lambda x: len(x['commandes']), reverse=True)

# Création du graphique PDF avec les tableaux pour chaque ville
pdf_pages = PdfPages("/datavolume1/rapport_clients_fideles.pdf")
fig, axs = plt.subplots(10, 1, figsize=(8, 15))

# Ajuster l'espace vertical entre les tableaux
plt.subplots_adjust(hspace=0)  

# Vous pouvez ajuster le nombre de clients ici
for ax, client in zip(axs, sorted_clients[:10]):  
    ax.axis('off')
    ax.margins(0, 0)
    ax.table(cellText=[
        ["Client", "Nombre de commandes", "Nombre de colis", "Moyenne colis/commande", "Écart type colis/commande"],
        ["{} - {} {}".format(client['codeclient'], client['nom'], client['prenom']), 
                        len(client['commandes']), 
                        client['nbcolis'],
         "{:.2f}".format(client['nbcolis'] / len(client['commandes'])),
         "{:.2f}".format(client['ecart_type_colis_par_commande'])]
        ], colLabels=None, 
           cellLoc='center', 
           loc='center', 
           fontsize=8)  # Augmenter la taille du tableau

    # Diminuer la taille du titre
    ax.set_title('{} ({})'.format(client['ville'],client['codepostal']), fontsize=7, y=0.7) 

# Enregistrer le graphe au format PDF
pdf_pages.savefig(fig, bbox_inches='tight')
# Fermer le PDF après la création
pdf_pages.close()  
