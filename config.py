import os

# Definir caminho da pasta dos arquivos PDF
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(BASE_DIR, "arquivos")

# Nome do arquivo PDF a ser processado
PDF_FILE = os.path.join(PDF_FOLDER, "o_pequeno_principe.pdf")