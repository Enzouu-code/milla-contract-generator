
from pathlib import Path
from docx import Document


def substituir_nos_paragrafos(paragrafos, dados):
    for paragrafo in paragrafos:
        for marcador, valor in dados.items():
            texto = paragrafo.text

            if marcador not in texto:
                continue

            # Se o marcador estiver inteiro em um único trecho,
            # substitui sem alterar a formatação desse trecho.
            substituido = False

            for run in paragrafo.runs:
                if marcador in run.text:
                    run.text = run.text.replace(marcador, str(valor))
                    substituido = True

            # Se o marcador estiver dividido entre vários trechos,
            # reconstrói o parágrafo usando a formatação do primeiro.
            if not substituido and marcador in paragrafo.text:
                texto_novo = paragrafo.text.replace(
                    marcador, str(valor)
                )

                if paragrafo.runs:
                    paragrafo.runs[0].text = texto_novo

                    for run in paragrafo.runs[1:]:
                        run.text = ""
                else:
                    paragrafo.add_run(texto_novo)


def substituir_nas_tabelas(tabelas, dados):
    for tabela in tabelas:
        for linha in tabela.rows:
            for celula in linha.cells:
                substituir_nos_paragrafos(celula.paragraphs, dados)
                substituir_nas_tabelas(celula.tables, dados)


def gerar_contrato(caminho_modelo, caminho_saida, dados):
    caminho_modelo = Path(caminho_modelo)
    caminho_saida = Path(caminho_saida)

    if not caminho_modelo.exists():
        raise FileNotFoundError(
            f"Modelo não encontrado: {caminho_modelo}"
        )

    documento = Document(caminho_modelo)

    substituir_nos_paragrafos(documento.paragraphs, dados)
    substituir_nas_tabelas(documento.tables, dados)

    for secao in documento.sections:
        substituir_nos_paragrafos(secao.header.paragraphs, dados)
        substituir_nas_tabelas(secao.header.tables, dados)

        substituir_nos_paragrafos(secao.footer.paragraphs, dados)
        substituir_nas_tabelas(secao.footer.tables, dados)

    documento.save(caminho_saida)

    print(f"\nContrato gerado com sucesso: {caminho_saida}")
