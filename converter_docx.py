from extrair_pdf import extrair_texto
from docx import Document 

def salvar_docx(pdf_path, docx_path):
    texto = extrair_texto(pdf_path)
    doc = Document()
    doc.add_paragraph(texto)
    doc.save(docx_path)

# Teste:
converter_docword = salvar_docx("C:\\Users\\onmmk\\OneDrive\\Projetos_Dev\\projeto_pdf\\arquivos\\o_pequeno_principe.pdf", "resultado.docx")
print("Texto salvo em resultado.docx!")
