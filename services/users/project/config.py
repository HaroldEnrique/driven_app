# services/users/project/config.py

class BaseConfig:
    """Configuración base"""

    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Configuración de desarrollo"""

    pass

class TestingConfig(BaseConfig):
    """Configuración de Testing"""

    TESTING = True

class ProductionConfig(BaseConfig):
    """Configuración de producción"""

    pass
