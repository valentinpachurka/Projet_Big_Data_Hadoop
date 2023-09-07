# Projet_Hadoop_Big_Data
Projet Big Data pour la Fromagerie du Fil Rouge

Ce projet vise à répondre aux besoins de la Fromagerie du Fil Rouge, un client possédant un datawarehouse depuis 2004 et représenté par un fichier CSV fourni. L'objectif est d'extraire des informations pertinentes à l'aide de jobs de traitement de données (Mapper-Reducer) pour répondre aux exigences du client. Le projet est structuré en plusieurs lots pour atteindre ces objectifs.

Lot 1: Analyse de Commandes par Ville et Objet

Contexte
La Fromagerie souhaite obtenir des statistiques détaillées sur les commandes passées par les clients, en se concentrant sur les données disponibles depuis 2010 dans le département de la Mayenne (53).

Objectifs

Calculer le nombre de commandes par ville dans le département 53, regroupé par objet (avec une quantité supérieure à 5), et ce pour chaque année depuis 2010.
Identifier les 10 clients les plus fidèles depuis 2008. Pour chacun de ces clients, calculer le nombre moyen et l'écart type du nombre de colis envoyés par ville, avec une comparaison au niveau du département. Générer un graphe au format PDF pour visualiser ces données.
Créer une courbe de croissance par objet pour les départements de la Mayenne (53), de la Sarthe (72) et du Maine-et-Loir (49). Générer un graphe au format PDF pour visualiser cette évolution.

Lot 2: Analyse des Meilleures Commandes et Segmentation

Contexte
Le client souhaite obtenir des statistiques plus spécifiques en se concentrant sur les 100 meilleures commandes entre 2006 et 2016, ainsi qu'une segmentation basée sur les départements 53, 61 et 28.

Objectifs

Identifier les 100 meilleures commandes entre 2006 et 2016, en fournissant des détails tels que la ville, le nombre de colis et la somme des "timbrecde".
Sélectionner 5% des commandes précédentes basées uniquement sur les départements 53, 61 et 28, en incluant uniquement les "timbrecli" non renseignés ou à 0. Fournir des informations similaires aux points 1, et générer un graphique de type "pie" au format PDF pour représenter cette segmentation.
Exporter les résultats des points 1 et 2 vers des fichiers Excel pour une analyse plus approfondie.

Lot 3: Mise en Place d'une Base NoSQL et Moteur de Recherche

Objectifs

Implémenter une base de données NoSQL pour stocker le contenu du fichier CSV.
Mettre en œuvre un moteur de recherche en utilisant Power BI pour interroger le Data Warehouse.
Fournir les résultats des Lot 1 et Lot 2 sous forme de données brutes (sans graphiques) pour répondre aux besoins du client.
Ce projet Big Data pour la Fromagerie du Fil Rouge vise à exploiter les données existantes et à fournir des analyses pertinentes pour prendre des décisions éclairées et améliorer les performances commerciales. Les différents lots permettront de répondre aux besoins spécifiques du client tout en utilisant des technologies adaptées pour le stockage, le traitement et la visualisation des données.
