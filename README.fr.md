# Moteur de gestion des incidents SOC
[🇬🇧 Read in English](README.md)

## Présentation du projet

Ce projet met en œuvre une solution légère de surveillance et de gestion des incidents pour un centre opérationnel de sécurité (SOC), reposant sur Wazuh et Python.

Le système surveille l'activité des serveurs web via Wazuh, détecte les comportements suspects à l'aide de règles de détection personnalisées et traite les alertes de sécurité par le biais d'un moteur de gestion des incidents développé en Python.

Ce moteur corrèle les alertes associées, évalue la gravité des incidents grâce à un mécanisme de notation des risques, enrichit les incidents avec des informations issues du référentiel MITRE ATT&CK et envoie des notifications par e-mail à l'analyste lorsque des seuils de risque prédéfinis sont atteints.

Ce projet a été conçu comme un laboratoire pratique de cybersécurité, permettant d'explorer la surveillance de la sécurité, l'ingénierie de détection, la corrélation d'alertes et la gestion des incidents.

## Objectifs du projet

- Déployer un environnement centralisé de surveillance de la sécurité à l'aide de Wazuh.
- Surveiller l'activité des serveurs web sous Linux et collecter les événements de sécurité.
- Développer des règles de détection personnalisées pour identifier les activités web suspectes.
- Concevoir un moteur en Python permettant de récupérer et de corréler les alertes de sécurité.
- Mettre en place une priorisation des incidents basée sur le niveau de risque.
- Enrichir les incidents détectés avec des informations issues du référentiel MITRE ATT&CK.
- Générer des enregistrements d'incidents structurés au format JSON.
- Notifier l'analyste par e-mail lors de la détection d'incidents significatifs.

## Architecture du système

<img width="3776" height="378" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/d8fc3f4a-6773-45c7-ad36-ca3370786ce5" />

## Technologies utilisées

| Technologie | Rôle |
|---|---|
| **Wazuh** | Supervision de la sécurité et génération d'alertes |
| **Python** | Corrélation des alertes, calcul du score de risque et automatisation |
| **OpenSearch** | Stockage et récupération des alertes via Wazuh Indexer |
| **Linux Mint** | Environnement du serveur web surveillé |
| **Nginx** | Serveur web et génération des journaux d'accès |
| **Windows 10** | Environnement d'exécution du moteur Python |
| **SSH** | Établissement d'un tunnel sécurisé entre Windows et Wazuh Indexer |
| **MITRE ATT&CK** | Classification et enrichissement des activités détectées |
| **SMTP / Gmail** | Envoi de notifications par e-mail |
| **JSON** | Stockage structuré des incidents |

## Règles de détection personnalisées

Deux règles personnalisées ont été développées dans Wazuh afin d'identifier les activités web suspectes.

### Règle 100100 — Détection de l'énumération Web

- **Objectif :** Détecter les tentatives potentielles d'énumération de répertoires et de fichiers web.
- **Logique de détection :** Identifie un nombre élevé de réponses HTTP 404 provenant d'une même adresse IP source dans une fenêtre de 60 secondes, avec un nombre important d'URL distinctes demandées.
- **Niveau de sévérité :** 10.
- **MITRE ATT&CK :** Reconnaissance — Wordlist Scanning (T1595.003).

### Règle 100101 — Détection des User-Agent suspects

- **Objectif :** Identifier les requêtes générées par des outils couramment utilisés pour le scan et l'énumération web.
- **Logique de détection :** Recherche des chaînes User-Agent suspectes associées à des outils tels que :
  - ffuf
  - Gobuster
  - Feroxbuster
  - Dirbuster
  - Dirb
  - Wfuzz
  - Nikto
- **Niveau de sévérité :** 8.
- **MITRE ATT&CK :** Reconnaissance — Wordlist Scanning (T1595.003).

Les alertes générées par ces règles sont ensuite récupérées et traitées par le moteur de gestion des incidents développé en Python.

*Remarque : Le mapping MITRE ATT&CK apporte un contexte comportemental, mais ne constitue pas une preuve qu'une attaque a eu lieu.*

## Corrélation des incidents et évaluation des risques avec Python

Un moteur de gestion des incidents développé en Python récupère les alertes de sécurité depuis Wazuh Indexer et les traite automatiquement.

### Récupération des alertes

- Établit une connexion avec Wazuh Indexer via un tunnel SSH.
- Interroge les alertes de sécurité à l'aide de l'API OpenSearch.
- Récupère périodiquement les alertes associées aux règles de détection personnalisées.

### Corrélation des incidents

Le moteur regroupe les alertes liées en fonction de :
- L'adresse IP source.
- L'agent surveillé ciblé.
- Une fenêtre de corrélation de cinq minutes.

Cette approche permet de regrouper plusieurs alertes liées dans un seul incident, au lieu de traiter chaque alerte individuellement.

### Évaluation des risques

Chaque incident reçoit un score de risque calculé en fonction de plusieurs facteurs, notamment :
- Le niveau de sévérité et le type de règle de détection.
- Le nombre d'alertes associées.
- Le nombre d'URL distinctes demandées.

Ce score permet de prioriser les incidents selon leur niveau de risque potentiel.

### Gestion des incidents

Pour chaque incident, le moteur :
- Génère un enregistrement d'incident unique.
- L'enrichit avec le contexte MITRE ATT&CK.
- Enregistre les informations dans `incidents.json`.
- Suit les alertes déjà traitées dans `processed_alerts.json` afin d'éviter les doublons.
- Déclenche une notification par e-mail lorsque le seuil de risque configuré est atteint.
