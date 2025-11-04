# Test de Régression MongoDB

Ce projet contient des tests unitaires et de régression pour vérifier que les données stockées dans MongoDB ne changent pas de manière inattendue après des modifications du code.

---

## Description

- **Objectif** : Assurer l'intégrité des données dans MongoDB pour les clients (`Client`) après chaque modification du code.  
- **Tests inclus** :  
  - Test de régression MongoDB (`test_regression.py`)  
  - Vérification des champs `nom`, `age`, `niveau` et `_id`.  
- **Workflow CI/CD** : GitHub Actions exécute automatiquement les tests sur chaque `push` ou `pull request` sur la branche `main`.

---

## Prérequis

- Python 3.11 ou supérieur
- MongoDB (Docker ou local)
- pip
- GitHub Actions pour CI/CD (optionnel)

---

## Installation des dépendances

```bash
python -m pip install --upgrade pip
pip install pymongo unittest2
