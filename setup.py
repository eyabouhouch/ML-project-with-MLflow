import setuptools

# Lire le contenu du fichier README.md pour l'utiliser comme long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Définir les métadonnées du projet
__version__ = "0.0.0"
REPO_NAME = "ML-Project-with-MLflow"
AUTHOR_USER_NAME = "eyabouhouch"  
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "eyabouhouch214@gmail.com"  

# Configuration du setup
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Un petit package Python pour une application ML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)