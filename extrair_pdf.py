import PyPDF2

def extrair_texto(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        texto = "\n".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
    return texto


texto_extraido = extrair_texto("C:\\Users\\onmmk\\OneDrive\\Projetos_Dev\\projeto_pdf\\arquivos\\o_pequeno_principe.pdf")
print(texto_extraido)  # Agora podemos usar o resultado como quisermos!