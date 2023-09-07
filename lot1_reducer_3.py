import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime

# Créez un espace de stockage pour les données des clients
clients_data = {}


# Parcourez chaque ligne de l'entrée
for line in sys.stdin:
    # Nettoyez la ligne et divisez-la en morceaux séparés par une tabulation
    line = line.strip()
    mapper = line.split('\t')

    # Ignorez les lignes vides ou celles commençant par 'AN'
    if len(mapper) == 0 or mapper[0] == 'AN':
        continue

    else:
        # Récupérez les informations importantes à partir de la ligne
        departements = mapper[1]
        annee_commande = int(mapper[2])
        lib_unique_objet = mapper[3]
        quantite_objet = int(mapper[4])

        if lib_unique_objet in clients_data:
            if departements in clients_data[lib_unique_objet]:
                if annee_commande in clients_data[lib_unique_objet][departements]:
                    clients_data[lib_unique_objet][departements][annee_commande] += quantite_objet
                else:
                    clients_data[lib_unique_objet][departements][annee_commande] = quantite_objet
            else:
                clients_data[lib_unique_objet][departements] = {annee_commande: quantite_objet}
        else:
            clients_data[lib_unique_objet] = {
                departements: {annee_commande: quantite_objet}
            }


# Liste de dates de 2004 à 2021
date_range = [datetime(year, 1, 1) for year in range(2004, 2022)]

# Créez un fichier PDF pour stocker nos graphiques
pdf_filename = '/datavolume1/rapport_croissance.pdf'
pdf = PdfPages(pdf_filename)

# Pour chaque objet client, générez des graphiques
for lib_unique_objet, departements_data in clients_data.items():
    # Créez une nouvelle page dans le PDF pour cet objet client
    plt.figure(figsize=(12, 15))
    plt.suptitle("Courbes de croissance pour {x}".format(x=lib_unique_objet))

    i = 1  # Compteur pour les sous-graphiques

    # Pour chaque département lié à cet objet client, générez un sous-graphique
    for departement, data_points in departements_data.items():
        plt.subplot(3, 1, i)
        plt.title("Département {x}".format(x=departement))
        plt.xlabel("Temps")
        plt.ylabel("Quantité d'objets")
        
        # Fixez les limites de l'axe vertical de 0 à 13
        plt.ylim(0, 503)

        # Créez une liste de quantités correspondant à la liste de dates complète
        quantite = [data_points.get(date.year, 0) for date in date_range]

        # Tracez le graphique avec des points
        plt.plot(date_range, quantite, marker='o')

        # Ajoutez les valeurs correspondantes à chaque point du graphique
        for x, y in zip(date_range, quantite):
            plt.annotate(str(y), (x, y), textcoords="offset points", xytext=(0,10), ha='center', va='bottom')
        i += 1

    # Ajustez la disposition des sous-graphiques pour une meilleure apparence
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    # Sauvegardez cette page du PDF
    pdf.savefig()
    # Fermez le graphique actuel
    plt.close()
# Fermez le fichier PDF complet
pdf.close()

# print("Graphiques générés avec succès dans un fichier PDF unique.")

# Créez un fichier PDF pour stocker nos graphiques
pdf_filename = '/datavolume1/rapport_croissance_2.pdf'
pdf = PdfPages(pdf_filename)

# Pour chaque objet client, générez des graphiques
for lib_unique_objet, departements_data in clients_data.items():
    # Créez une nouvelle page dans le PDF pour cet objet client
    plt.figure(figsize=(12, 15))
    plt.suptitle("Courbes de croissance pour {x}".format(x=lib_unique_objet))

    i = 1  # Compteur pour les sous-graphiques

    # Pour chaque département lié à cet objet client, générez un sous-graphique
    for departement, data_points in departements_data.items():
        plt.subplot(3, 1, i)
        plt.title("Département {x}".format(x=departement))
        plt.xlabel("Temps")
        plt.ylabel("Quantité d'objets")

        # Créez une liste de quantités correspondant à la liste de dates complète
        quantite = [data_points.get(date.year, 0) for date in date_range]

        # Tracez le graphique avec des points
        plt.plot(date_range, quantite, marker='o')

        # Ajoutez les valeurs correspondantes à chaque point du graphique
        for x, y in zip(date_range, quantite):
            plt.annotate(str(y), (x, y), textcoords="offset points", xytext=(0,10), ha='center', va='bottom')
        i += 1

    # Ajustez la disposition des sous-graphiques pour une meilleure apparence
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    # Sauvegardez cette page du PDF
    pdf.savefig()
    # Fermez le graphique actuel
    plt.close()
# Fermez le fichier PDF complet
pdf.close()