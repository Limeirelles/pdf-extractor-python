import os
from extrair_pdf import extrair_texto
from docx import Document
import config

def salvar_docx(pdf_path, docx_filename):
    """Extrai texto de um PDF e salva em um arquivo DOCX."""
    texto = extrair_texto(pdf_path)

    # Definir caminho do arquivo DOCX dinamicamente
    docx_path = os.path.join(config.PDF_FOLDER, docx_filename)

    doc = Document()
    doc.add_paragraph(texto)
    doc.save(docx_path)
    
    print(f"Texto salvo em {docx_path}!")

# Teste:
converter_docword = salvar_docx(config.PDF_FILE, "texto_extraido.docx")