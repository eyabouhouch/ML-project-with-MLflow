import os
import yaml
from typing import Any
from omegaconf import OmegaConf

# Fonction pour charger un fichier de configuration YAML
def load_config(file_path: str) -> Any:
    """
    Charge un fichier YAML et renvoie son contenu sous forme d'objet OmegaConf.
    
    :param file_path: Le chemin du fichier de configuration.
    :return: L'objet de configuration.
    """
    try:
        config = OmegaConf.load(file_path)
        return config
    except Exception as e:
        print(f"Erreur lors du chargement de la configuration : {e}")
        raise

# Fonction pour créer un répertoire si nécessaire
def create_dir_if_not_exists(directory: str):
    """
    Crée un répertoire si celui-ci n'existe pas déjà.
    
    :param directory: Le chemin du répertoire à vérifier/créer.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Le répertoire {directory} a été créé.")
    else:
        print(f"Le répertoire {directory} existe déjà.")

# Fonction pour sauvegarder des données dans un fichier YAML
def save_to_yaml(data: Any, file_path: str):
    """
    Sauvegarde des données dans un fichier YAML.
    
    :param data: Les données à sauvegarder (peut être un dictionnaire, une liste, etc.).
    :param file_path: Le chemin du fichier de destination.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)
            print(f"Les données ont été sauvegardées dans {file_path}.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde dans le fichier YAML : {e}")
        raise

# Exemple de fonction de validation pour la configuration (en cas d'utilisation de types de données spécifiques)
def validate_config(config: Any):
    """
    Effectue une validation de la configuration (par exemple, vérifier que certains champs sont présents).
    
    :param config: La configuration à valider.
    """
    if not config.get('model_name'):
        raise ValueError("Le champ 'model_name' est manquant dans la configuration.")
    print("La configuration est valide.")
