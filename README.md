  Milla Contract Generator

  Projeto de automação de contratos imobiliários desenvolvido em Python, com integração planejada ao Microsoft Power Automate Desktop, para reduzir tarefas manuais e otimizar processos administrativos.

  Desenvolvido no contexto da Milla Imóveis e Corretagem de Seguros.
  ## Tecnologias utilizadas
  - **Python** — lógica de programação e geração de documentos.
  - **Microsoft Word** — modelo do contrato em formato `.docx`.
  - **Power Automate Desktop** — automação do fluxo de execução e organização dos documentos.
  - **Git e GitHub** — versionamento e documentação do projeto.
  ## Funcionalidades
  - Coleta de dados de compradores e vendedores.
  - Coleta de informações do imóvel.
  - Coleta de valores e condições de pagamento.
  - Preenchimento automatizado de um modelo de contrato Word.
  - Geração de documentos `.docx` com data e hora no nome.
  - Integração com Power Automate Desktop para automatizar etapas do processo.
  ## Estrutura do projeto
  ```text
  milla-contract-generator/
  ├── templates/
  │   └── contrato_compra_venda.docx
  ├── output/
  ├── power-automate/
  │   └── Milla-Contract-Generator.txt
  ├── main.py
  ├── contract_generator.py
  ├── validators.py
  ├── .gitignore
  └── README.md
  ```
  A pasta `power-automate/` receberá o arquivo exportado do fluxo do Power Automate Desktop após a conclusão da automação. Até lá, não é necessário adicionar nenhum arquivo nessa pasta.
  ## Como funciona
  ### 1. Geração do contrato
  O script `main.py` solicita os dados pelo terminal e utiliza as funções do projeto para gerar o documento.
  O modelo do contrato fica na pasta `templates/`, e os documentos gerados são salvos em `output/`.
  Os arquivos seguem o padrão:

  `contrato_AAAAMMDD_HHMMSS.docx`
  ### 2. Automação com Power Automate Desktop
  O fluxo **Milla - Gerar Contrato** está sendo desenvolvido para:
  1. Executar o script Python.
  2. Localizar o contrato recém-gerado.
  3. Identificar o arquivo correto.
  4. Mover o documento para a pasta de destino.
  A execução do Python pelo Power Automate Desktop já foi testada. A seleção segura do contrato mais recente e a movimentação automática ainda precisam ser finalizadas.
  ## Como executar
  ### Pré-requisitos
  - Windows.
  - Python instalado.
  - Modelo Word disponível em `templates/contrato_compra_venda.docx`.
  - Dependências Python utilizadas pelo projetotaladas.

### Executar o gerador
Abra o terminal na pasta do projeto e execute:
bash
python main.py
Responda às perguntas exibidas no terminal e verifique o contrato gerado na pasta `output/`.

## Aviso
Este projeto automatiza a geração de documentos, mas não substitui a revisão jurídica. Os contratos devem ser conferidos pelos responsáveis antes de serem utilizados em negociações reais.
