# Mini Projeto 01 - Análise e Tratamento de Dados com Python

## Sobre o Projeto

Projeto desenvolvido em Python para análise, diagnóstico e tratamento de
dados utilizando arquivos CSV.

O projeto processa dois datasets:

-   `olist_products_dataset.csv`
-   `olist_orders_dataset.csv`

O fluxo implementado contempla:

-   carregamento dos dados;
-   diagnóstico de inconsistências;
-   tratamento de valores ausentes;
-   normalização de categorias;
-   tratamento de datas;
-   análise de regras de negócio;
-   geração de relatório final.

## Estrutura do Projeto

    MiniProjeto-01/
    ├── dados/
    │   ├── olist_products_dataset.csv
    │   └── olist_orders_dataset.csv
    ├── main.py
    ├── funcoes.py
    ├── README.md
    └── .gitignore

## Tecnologias Utilizadas

-   Python 3.x

Bibliotecas:

-   csv
-   datetime
-   re
-   unicodedata

## Fluxo do Projeto

    Carregamento
          ↓
    Diagnóstico
          ↓
    Tratamento
          ↓
    Validação
          ↓
    Relatório Final

## Tratamento dos Dados

### Categorias

A função `limpar_categoria()` realiza:

-   remoção de espaços;
-   conversão para minúsculas;
-   remoção de caracteres especiais;
-   remoção de acentuação.

Categorias vazias são substituídas por:

    sem categoria

Resultado encontrado:

    610 categorias vazias corrigidas

### Dimensões

Foram avaliados:

-   peso;
-   comprimento;
-   altura;
-   largura.

Valores ausentes foram substituídos utilizando a média dos valores
válidos.

Resultados:

    Peso médio: 2276.47 g
    Comprimento médio: 30.82 cm
    Altura média: 16.94 cm
    Largura média: 23.20 cm

### Datas

As datas de aprovação dos pedidos foram convertidas de:

    YYYY-MM-DD HH:MM:SS

para:

    DD/MM/YYYY

## Análise de Pedidos

Foi analisada a hipótese:

> Pedidos sem data de entrega são necessariamente pedidos cancelados.

Resultado:

    Pedidos sem data de entrega: 2965
    Pedidos cancelados sem data de entrega: 619
    Pedidos sem data com outros status: 2346

Conclusão:

A hipótese foi rejeitada, pois nem todos os pedidos sem data de entrega
estavam cancelados.

## Resultados Finais

    Produtos processados: 32951
    Pedidos processados: 99441
    Categorias vazias corrigidas: 610
    Valores dimensionais corrigidos: 8
    Total de valores ausentes tratados: 618
    Pedidos cancelados identificados: 625

## Reflexão Teórica

A aplicação de uma lógica de programação estruturada na etapa de limpeza dos dados é fundamental para garantir que futuras análises e modelos de Inteligência Artificial sejam desenvolvidos sobre informações confiáveis. Dados incompletos, inconsistentes ou com padrões incorretos podem introduzir vieses no processo de aprendizado, fazendo com que os modelos reproduzam distorções existentes na base de treinamento. A identificação de valores ausentes, inconsistências dos dados e informações incompletas permitem compreender a qualidade inicial da base e direcionar as estratégias de correção. Esse processo evidencia que apreparação dos dados é uma etapa fundamental em projetos de análise, pois dados inconsistentes podem comprometer interpretações, indicadores e decisões posteriores.

No projeto desenvolvido, a identificação e tratamento de categorias vazias, valores dimensionais ausentes e padronização das informações representam etapas importantes para reduzir ruídos e melhorar a qualidade dos dados utilizados.

Além disso, uma preparação inadequada dos dados pode contribuir para problemas como overfitting, pois o modelo pode aprender características específicas ou inconsistências presentes na base ao invés de identificar padrões reais do comportamento dos dados. A limpeza, normalização e validação das informações permitem construir conjuntos de dados mais representativos, aumentando a capacidade de generalização dos modelos e reduzindo a influência de informações incorretas ou tendenciosas nas previsões futuras.


## Como Executar

Clone o repositório:

``` bash
git clone https://github.com/FCASSINI/Mini_Projeto_Machine_Learning_T3.git
```

Execute:

``` bash
python main.py
```

## Conceitos Aplicados

-   manipulação de arquivos CSV;
-   listas e dicionários;
-   funções;
-   modularização;
-   tratamento de strings;
-   expressões regulares;
-   manipulação de datas;
-   tratamento de dados ausentes;
-   validação de resultados.

## Autor

Felipe Antonio Cassini

Projeto desenvolvido para fins acadêmicos utilizando Python.
