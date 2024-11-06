import os
import sys

# Obtenez les hashs de commit à partir des variables d'environnement
badhash = os.getenv("BAD_COMMIT")
goodhash = os.getenv("GOOD_COMMIT")

if not badhash or not goodhash:
    print("Erreur : Les variables BAD_COMMIT et GOOD_COMMIT doivent être définies.")
    sys.exit(1)

# Démarrer le bisect
os.system(f"git bisect start {badhash} {goodhash}")

# Exécuter le test avec git bisect
# Remplacez 'run_test.sh' par le script ou commande de test spécifique
result = os.system("git bisect run python manage.py test")

# Terminer le bisect
os.system("git bisect reset")

# Gestion de sortie en fonction du résultat
if result != 0:
    print("Erreur pendant l'exécution de git bisect")
    sys.exit(1)

print("git bisect terminé avec succès.")