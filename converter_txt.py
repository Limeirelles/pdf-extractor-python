from extrair_pdf import extrair_texto

def salvar_txt(pdf_path, txt_path):
    texto = extrair_texto(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as file:
        file.write(texto)

# Teste:
converter_texto = salvar_txt("C:\\Users\\onmmk\\OneDrive\\Projetos_Dev\\projeto_pdf\\arquivos\\o_pequeno_principe.pdf", "resultado.txt")
print("Texto salvo em resultado.txt!")

