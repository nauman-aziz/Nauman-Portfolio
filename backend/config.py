import os

class Config:
    # Default base URL, can be overridden by specific configurations.
    BASE_URL = os.environ.get("BASE_URL", "https://my-portfolio-backend-ten.vercel.app/")

class DevelopmentConfig(Config):
    BASE_URL = "http://localhost:5000"
    DEBUG = True  # Additional development configurations can be added.

class ProductionConfig(Config):
    BASE_URL = "https://my-portfolio-backend-ten.vercel.app/"
    DEBUG = False
