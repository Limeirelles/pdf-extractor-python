import os
from extrair_pdf import extrair_texto
import config



def salvar_txt(pdf_path, txt_filename):
    """Extrai texto de um PDF e salva em um arquivo TXT."""
    texto = extrair_texto(pdf_path)

    # Definir o caminho do arquivo TXT dinamicamente
    txt_path = os.path.join(config.PDF_FOLDER, txt_filename)

    with open(txt_path, "w", encoding="utf-8") as file:
        file.write(texto)
    
    print(f"Texto salvo em {txt_path}!")


# Teste:
# Teste:
converter_texto = salvar_txt(config.PDF_FILE, "texto_extraido.txt")


