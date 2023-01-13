# Cette métaclasse utilise un dictionnaire _instances pour stocker les instances de chaque classe qui l'utilise.
# Lorsque l'on appelle une classe qui utilise cette métaclasse (par exemple GameEnv), la méthode __call__ est appelée.
# Cette méthode vérifie si une instance de la classe a déjà été créée, et si c'est le cas, elle retourne cette instance.
# Sinon, elle crée une nouvelle instance de la classe en appelant super().__call__(*args, **kwargs)
# et la stocke dans _instances.

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]