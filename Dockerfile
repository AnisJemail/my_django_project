# Dockerfile
FROM python:3.10-slim

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Commande de lancement (à adapter selon ton projet)
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]


