# SOC Incident Management Engine

**Language / Langue:** English | Français

- [English](#english)
- [Français](#français)

---

# English

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

## System Architecture

<img width="3776" height="378" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/e945453c-02be-410b-85ee-96a3eb7e3c8a" />



