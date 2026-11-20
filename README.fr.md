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
