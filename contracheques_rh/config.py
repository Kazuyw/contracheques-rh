import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "troque-esta-chave")
    APP_PASSWORD = os.getenv("APP_PASSWORD", "leviémelhor")
    
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.office365.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER", "")
    SMTP_PASS = os.getenv("SMTP_PASS", "")
    SMTP_SENDER = os.getenv("SMTP_SENDER", SMTP_USER)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_PLANILHAS = os.path.join(BASE_DIR, "uploads", "planilhas")
    UPLOAD_PDFS = os.path.join(BASE_DIR, "uploads", "pdfs")
    LOG_FILE = os.path.join(BASE_DIR, "logs", "envios.log")
