SOC Incident Management Engine

EN:
# SOC Real-Time Incident Detection & Response Engine

## Project Overview

This project implements a lightweight Security Operations Center (SOC) monitoring and incident management solution using Wazuh and Python.

The system monitors web server activity through Wazuh, detects suspicious behavior using custom detection rules, and processes security alerts through a Python-based incident engine.

The engine correlates related alerts, evaluates incident severity using a risk-scoring mechanism, enriches incidents with MITRE ATT&CK context, and sends email notifications to the analyst when predefined risk conditions are met.

The project was developed as a practical cybersecurity home lab to explore security monitoring, detection engineering, alert correlation, and incident management.

## Project Objectives

- Deploy a centralized security monitoring environment using Wazuh.
- Monitor Linux web server activity and collect security events.
- Develop custom detection rules for suspicious web activity.
- Build a Python engine to retrieve and correlate security alerts.
- Implement risk-based incident prioritization.
- Enrich detected incidents with MITRE ATT&CK information.
- Generate structured incident records in JSON format.
- Notify the analyst through email when significant incidents are detected.

FR:
# Moteur de détection et de réponse aux incidents en temps réel (SOC)

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
