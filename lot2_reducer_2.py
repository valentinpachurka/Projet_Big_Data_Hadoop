import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Lire les lignes d'entrée depuis STDIN (standard input)
data = []
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Diviser la ligne en éléments
    code, total_points, total_lignes, year, villecli, Nbcolis, cpcli, timbrecde = line.split('\t')

    total_points = float(total_points)
    total_lignes = int(total_lignes)
    moyenne_points_commande = total_points / total_lignes

    data.append(
        [code, total_points, moyenne_points_commande, int(total_lignes), int(year), villecli, int(cpcli), int(Nbcolis),
         float(timbrecde)])
    print("OK;OK")

# Créer un DataFrame pandas avec les résultats
columns = ['Code', 'Total Points', 'Moyenne Points', 'Total Lignes', 'Year', 'Ville Client', 'Code Postal', 'Nb Colis', 'Timbrecde']
df = pd.DataFrame(data, columns=columns)

# Trier les données et conserver les 5 premières lignes
df_sorted = df.sort_values(by='Total Points', ascending=False).head(5)

# Afficher les résultats triés
# print(df_sorted)

# Enregistrer le DataFrame au format Excel
output_excel_file = '/datavolume1/resultats_2_2.xlsx'
df_sorted.to_excel(output_excel_file, index=False)

# Générer un graphe pie avec les départements et leur part dans les commandes
departements = df_sorted['Code Postal'].value_counts()

# Créer une nouvelle figure
plt.figure()

# Créer le graphe pie
plt.pie(departements.values, labels=departements.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Répartition des commandes par département")

# Enregistrer le graphe au format PDF
output_pdf_file = '/datavolume1/resultat_2_2.pdf'
with PdfPages(output_pdf_file) as pdf:
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF

# Fermez le graphique actuel
plt.close()

# Fermez le fichier PDF complet
# pdf.close()