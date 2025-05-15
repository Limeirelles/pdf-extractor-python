

# Extração de Texto de PDFs com Python 📄🔍

Este projeto permite extrair texto de arquivos PDF e salvá-los automaticamente em `.txt` ou `.docx`.  
O objetivo é facilitar a conversão de documentos em texto legível e acessível para análises e edição.

## 🛠 Tecnologias utilizadas:
- **Python** 🐍
- **PyPDF2** (extração de texto)
- **python-docx** (exportação para Word)
- **GitHub** (controle de versão)
- **Virtual Environment** (`venv`) para isolamento de dependências

---

## 🚀 Como usar:

### 1️⃣ Clone este repositório:
```bash
git clone https://github.com/Limeirelles/pdf-extractor-python.git

cd pdf-extractor-python

python -m venv venv  # Criação do ambiente virtual
venv\Scripts\activate  # Ativação no Windows
source venv/bin/activate  # Ativação no Linux/macOS

Com o ambiente virtual ativo, instale as bibliotecas necessárias:
pip install -r requirements.txt


Caso não tenha o arquivo requirements.txt, instale manualmente:
pip install PyPDF2 python-docx

📂 Estrutura do projeto
/pdf-extractor-python
   ├── extrair_pdf.py    # Código para extrair o texto do PDF
   ├── converter_txt.py  # Código para salvar o texto extraído em um arquivo .txt
   ├── converter_docx.py # Código para exportar o texto para Word (.docx)
   ├── README.md         # Documentação do projeto
   ├── .gitignore        # Arquivos que devem ser ignorados pelo Git
   ├── requirements.txt  # Lista de pacotes do projeto
   ├── venv/             # Ambiente virtual Python (não versionado)

📝 Exemplos de execução
🔹 Extrair texto do PDF
Execute o script de extração: python extrair_pdf.py

Saída esperada:
Página 1:
Este é um exemplo de extração de texto de um arquivo PDF.

🔹 Converter para .txt
python converter_txt.py
Isso criará um arquivo resultado.txt contendo o texto extraído.

🔹 Converter para .docx
python converter_docx.py
Isso criará um documento resultado.docx com o conteúdo extraído do PDF.

🛠 Melhorias futuras:
✔ Adicionar interface gráfica para facilitar o uso.
✔ Criar suporte para múltiplos PDFs simultaneamente.
✔ Melhorar formatação do texto ao exportar para .docx.

📌 Observações:
- Certifique-se de configurar o caminho do PDF corretamente antes de rodar os scripts.
- O ambiente virtual (venv) ajuda a evitar conflitos de dependências.
- Contribuições e sugestões são bem-vindas! 🚀✨

💡 Gostou do projeto? Faça um fork, contribua ou deixe uma estrela! 🌟
📢 Me siga no www.linkedin.com/in/olimpiomeirelles 😃













