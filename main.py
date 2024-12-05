from src.mlProject import logger

if __name__ == "__main__":
    logger.info("Test du logger : Ce message sera enregistré dans le terminal et dans running_logs.log.")
    logger.error("Ceci est un message d'erreur pour tester la journalisation.")
