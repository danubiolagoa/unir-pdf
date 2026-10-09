# Unir PDF

Aplicativo simples para unir vários arquivos PDF em um só, escolhendo a ordem e o nome do arquivo final.
Roda inteiramente no navegador: **os arquivos nunca saem do seu computador**.

## Recursos

- Adicione quantos PDFs quiser (arrastar e soltar ou clicar para escolher)
- Defina a ordem arrastando os itens, pelos botões ↑ ↓ ou com "Ordenar A–Z"
- Tamanho, orientação e rotação de cada página são preservados
- Nome do arquivo final editável, com sugestões baseadas nos arquivos de entrada
- Funciona offline

## Como usar

1. Baixe o arquivo [`Unir-PDF.html`](Unir-PDF.html) (arquivo único, com tudo embutido).
2. Dê dois cliques para abrir no navegador (Chrome, Edge ou Firefox).
3. Adicione os PDFs, ajuste a ordem, confira o nome e clique em **Unir PDFs**.

Para compartilhar com colegas, basta enviar o `Unir-PDF.html`.

## Limitações

- PDFs protegidos por senha podem não ser lidos.
- Marcadores (bookmarks) e campos de formulário dos PDFs originais podem não ser mantidos no arquivo unido.

## Estrutura

| Arquivo | Descrição |
|---------|-----------|
| `index.html` | Código-fonte do app (usa `pdf-lib.min.js` local) |
| `pdf-lib.min.js` | Biblioteca [pdf-lib](https://github.com/Hopding/pdf-lib) 1.17.1 (MIT) |
| `Unir-PDF.html` | Versão em arquivo único, gerada por `build.ps1` |
| `build.ps1` | Gera `Unir-PDF.html` embutindo a biblioteca no `index.html` |
| `unir_pdf.py` | Versão alternativa de janela desktop (Python + tkinter + pypdf) |

## Desenvolvimento

Depois de alterar o `index.html`, gere novamente a versão única:

```powershell
./build.ps1
```

Versão Python (opcional):

```
pip install -r requirements.txt
python unir_pdf.py
```

## Licença

O código deste projeto é distribuído sob a licença MIT. A biblioteca pdf-lib é MIT, de seus autores.
