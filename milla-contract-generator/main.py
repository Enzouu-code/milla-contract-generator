
from pathlib import Path
from datetime import datetime
from contract_generator import gerar_contrato


BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "templates" / "contrato_compra_venda.docx"
OUTPUT_DIR = BASE_DIR / "output"


def perguntar(mensagem):
    return input(f"{mensagem}: ").strip()


def coletar_dados():
    dados = {}

    print("\n--- DADOS DOS VENDEDORES ---")

    campos_vendedores = {
        "[NOME_VENDEDORA]": "Nome da vendedora",
        "[NACIONALIDADE_VENDEDORA]": "Nacionalidade da vendedora",
        "[PROFISSAO_VENDEDORA]": "Profissão da vendedora",
        "[CPF_VENDEDORA]": "CPF da vendedora",
        "[RG_VENDEDORA]": "RG da vendedora",
        "[NOME_VENDEDOR]": "Nome do vendedor",
        "[NACIONALIDADE_VENDEDOR]": "Nacionalidade do vendedor",
        "[PROFISSAO_VENDEDOR]": "Profissão do vendedor",
        "[CPF_VENDEDOR]": "CPF do vendedor",
        "[RG_VENDEDOR]": "RG do vendedor",
        "[LOCALIZACAO_VENDEDORES]": "Endereço dos vendedores",
    }

    for marcador, mensagem in campos_vendedores.items():
        dados[marcador] = perguntar(mensagem)

    print("\n--- DADOS DOS COMPRADORES ---")

    campos_compradores = {
        "[NOME_COMPRADORA]": "Nome da compradora",
        "[NACIONALIDADE_COMPRADORA]": "Nacionalidade da compradora",
        "[PROFISSAO_COMPRADORA]": "Profissão da compradora",
        "[CPF_COMPRADORA]": "CPF da compradora",
        "[RG_COMPRADORA]": "RG da compradora",
        "[NOME_COMPRADOR]": "Nome do comprador",
        "[NACIONALIDADE_COMPRADOR]": "Nacionalidade do comprador",
        "[PROFISSAO_COMPRADOR]": "Profissão do comprador",
        "[CPF_COMPRADOR]": "CPF do comprador",
        "[RG_COMPRADOR]": "RG do comprador",
        "[LOCALIZACAO_COMPRADORES]": "Endereço dos compradores",
    }

    for marcador, mensagem in campos_compradores.items():
        dados[marcador] = perguntar(mensagem)

    print("\n--- DADOS DO IMÓVEL ---")

    campos_imovel = {
        "[TIPO_IMOVEL]": "Tipo do imóvel",
        "[RUA_IMOVEL]": "Rua e número do imóvel",
        "[BAIRRO_IMOVEL]": "Bairro do imóvel",
        "[CIDADE_IMOVEL]": "Cidade do imóvel",
        "[NUMERO_MATRICULA]": "Número da matrícula",
        "[INSCRICAO_IMOBILIARIA]": "Inscrição imobiliária",
    }

    for marcador, mensagem in campos_imovel.items():
        dados[marcador] = perguntar(mensagem)

    print("\n--- VALORES E PAGAMENTO ---")

    campos_pagamento = {
        "[VALOR_TOTAL]": "Valor total da venda",
        "[TOTAL_POR_ESCRITO]": "Valor total por extenso",
        "[VALOR_LIQUIDO]": "Valor líquido",
        "[LIQUIDO_POR_ESCRITO]": "Valor líquido por extenso",
        "[VALOR_FINANCIAMENTO]": "Valor do financiamento",
        "[FINANCIAMENTO_POR_ESCRITO]": "Financiamento por extenso",
        "[PRAZO_DOCUMENTACAO]": "Prazo para entregar a documentação",
        "[VALOR_SINAL]": "Valor do sinal",
        "[SINAL_POR_ESCRITO]": "Valor do sinal por extenso",
        "[PRAZO_SINAL]": "Data ou prazo para pagamento do sinal",
        "[VALOR_RESTANTE]": "Valor restante",
        "[VALOR_POR_RESTANTE]": "Valor restante por extenso",
    }

    for marcador, mensagem in campos_pagamento.items():
        dados[marcador] = perguntar(mensagem)

    print("\n--- DADOS BANCÁRIOS DO VENDEDOR ---")

    campos_bancarios = {
        "[BANCO_VENDEDOR]": "Banco",
        "[AGENCIA_VENDEDOR]": "Agência",
        "[CONTA_CORRENTE]": "Conta corrente",
    }

    for marcador, mensagem in campos_bancarios.items():
        dados[marcador] = perguntar(mensagem)

    print("\n--- COMISSÃO E ENTREGA DAS CHAVES ---")

    campos_finais = {
        "[TEMPO_PRAZO]": "Prazo para entrega das chaves",
        "[VALOR_COMISSAO]": "Valor da comissão",
        "[COMISSAO_POR_ESCRITO]": "Comissão por extenso",
        "[CIDADE]": "Cidade de assinatura do contrato",
    }

    for marcador, mensagem in campos_finais.items():
        dados[marcador] = perguntar(mensagem)

    data_padrao = datetime.now().strftime("%d/%m/%Y")
    data_assinatura = input(
        f"Data da assinatura [{data_padrao}]: "
    ).strip()

    dados["[DATA_ASSINATURA]"] = data_assinatura or data_padrao

    # Corrige o marcador que está escrito com erro no modelo Word.
    dados["[NOME_COMRPADORA]"] = dados["[NOME_COMPRADORA]"]

    return dados


def main():
    print("=" * 45)
    print("       MILLA CONTRACT GENERATOR")
    print("=" * 45)

    if not TEMPLATE_PATH.exists():
        print("\nErro: modelo de contrato não encontrado.")
        print(f"Caminho esperado: {TEMPLATE_PATH}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dados = coletar_dados()

    print("\nGerando o contrato...")

    nome_arquivo = f"contrato_{datetime.now():%Y%m%d_%H%M%S}.docx"
    caminho_saida = OUTPUT_DIR / nome_arquivo

    try:
        gerar_contrato(TEMPLATE_PATH, caminho_saida, dados)
    except Exception as erro:
        print(f"\nErro ao gerar o contrato: {erro}")
        return

    print("\nProcesso finalizado.")


if __name__ == "__main__":
    main()
