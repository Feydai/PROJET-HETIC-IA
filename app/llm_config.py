class LLMConfig:
    """
    Classe pour gérer les configurations de LLM, notamment la température.
    """
    def __init__(self):
        self.temperature = 0.7  # Température par défaut

    def set_temperature(self, value):
        """
        Définit la température pour le LLM.
        """
        if not (0.0 <= value <= 1.5):
            raise ValueError("La température doit être entre 0.0 et 1.5.")
        self.temperature = value
        print(f"Température mise à jour : {self.temperature}")

    def get_temperature(self):
        """
        Récupère la température actuelle.
        """
        return self.temperature


# Instance unique pour gérer la configuration
llm_config = LLMConfig()
