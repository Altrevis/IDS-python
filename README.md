# Détecteur d'Intrusion (IDS) en Python

## Description

Ce projet est un **Détecteur d'Intrusion (IDS)** simplifié développé en **Python** avec l'utilisation de **Flask** pour l'affichage des alertes sur une page web. Le programme analyse le trafic réseau à la recherche de **scans de ports** (via des paquets TCP) et affiche les alertes en temps réel sur une interface web. Ce système de détection fonctionne en arrière-plan et alerte dès qu'une tentative de scan est détectée.

Le système utilise **Scapy** pour capturer les paquets réseau et **Flask** pour afficher les alertes sur une page web dynamique.

## Fonctionnalités

- **Détection de scan de ports** : Le programme analyse les paquets réseau à la recherche de scans de ports et génère des alertes lorsque des tentatives de connexion sont détectées.
- **Interface web avec Flask** : Les alertes sont affichées en temps réel sur une page web simple via Flask. Le frontend utilise du JavaScript pour actualiser les alertes toutes les 2 secondes.
- **Données en temps réel** : Le frontend interroge le backend Flask pour obtenir les dernières alertes sous forme de JSON et les affiche sans avoir besoin de recharger la page.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les dépendances nécessaires :

- **Python 3.x**  
- **Scapy** pour la capture de paquets réseau
- **Flask** pour l'application web

### Installation des dépendances

1. **Installer Scapy** :
   ```bash
   sudo apt-get install python3-scapy
