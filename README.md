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

## Reflexão Teórica sobre a Análise e Tratamento dos Dados

A análise dos dados demonstrou a importância da etapa de diagnóstico
antes da aplicação de qualquer processo de tratamento. A identificação
de valores ausentes, inconsistências cadastrais e informações
incompletas permitiu compreender a qualidade inicial da base e
direcionar as estratégias de correção. Esse processo evidencia que a
preparação dos dados é uma etapa fundamental em projetos de análise,
pois dados inconsistentes podem comprometer interpretações, indicadores
e decisões posteriores.

O tratamento realizado buscou preservar a integridade das informações
originais, criando uma nova versão dos dados processados sem modificar a
base bruta. A substituição das categorias ausentes por uma classificação
padronizada e a imputação das dimensões físicas utilizando valores
médios dos registros válidos representam técnicas de limpeza e
padronização utilizadas em processos reais de preparação de dados. A
utilização da média como estratégia de correção foi aplicada devido à
pequena quantidade de valores ausentes identificados, evitando a perda
de registros e mantendo a consistência do conjunto analisado.

A análise dos pedidos permitiu avaliar uma hipótese de negócio
relacionada aos pedidos sem data de entrega. Os resultados demonstraram
que a ausência dessa informação não representava necessariamente um
cancelamento, evidenciando a importância de validar suposições
utilizando os próprios dados. Dessa forma, o projeto reforça a
necessidade de combinar técnicas de tratamento, análise exploratória e
interpretação dos resultados para transformar dados brutos em
informações confiáveis para apoio à tomada de decisão.

## Como Executar

Clone o repositório:

``` bash
git clone <URL_DO_REPOSITORIO>
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
